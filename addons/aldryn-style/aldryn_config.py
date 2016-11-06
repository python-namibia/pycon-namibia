# -*- coding: utf-8 -*-
import re
from aldryn_client import forms


CLASS_NAME_FORMAT = re.compile(r'^\w[\w_-]*$')


class ClassNamesField(forms.CharField):

    def clean(self, value):
        value = super(ClassNamesField, self).clean(value)
        class_names = filter(bool, map(lambda x: x.strip(), value.split(',')))
        for class_name in class_names:
            if not CLASS_NAME_FORMAT.match(class_name):
                raise forms.ValidationError(u'%s is not a proper class name.' % (class_name, ))
        return u", ".join(class_names)


class Form(forms.BaseForm):

    class_names = ClassNamesField('Class names', max_length=255)

    def to_settings(self, data, settings):
        settings['ALDRYN_STYLE_CLASS_NAMES'] = [
            (class_name, class_name) for class_name in set(
                filter(bool, map(lambda x: x.strip(), data['class_names'].split(','))))]
        return settings
