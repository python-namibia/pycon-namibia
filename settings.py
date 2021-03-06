# -*- coding: utf-8 -*-

INSTALLED_ADDONS = [
    # <INSTALLED_ADDONS>  # Warning: text inside the INSTALLED_ADDONS tags is auto-generated. Manual changes will be overwritten.
    'aldryn-addons',
    'aldryn-django',
    'aldryn-sso',
    'aldryn-django-cms',
    'aldryn-background-image',
    'aldryn-bootstrap3',
    'aldryn-newsblog',
    'aldryn-style',
    'djangocms-file',
    'djangocms-googlemap',
    'djangocms-link',
    'djangocms-picture',
    'djangocms-snippet',
    'djangocms-text-ckeditor',
    'djangocms-video',
    'django-filer',
    # </INSTALLED_ADDONS>
]

import aldryn_addons.settings
aldryn_addons.settings.load(locals())


# all django settings can be altered here

INSTALLED_APPS.extend([
    'axes',
])

MIDDLEWARE_CLASSES.extend([
    # add your own middlewares here
])

CKEDITOR_SETTINGS = {}

CKEDITOR_SETTINGS['stylesSet'] = [
    {
        'name': 'Speaker',
        'element': 'h3',
        'attributes': { 'class': 'speaker' },
     },
    {
        'name': 'Talk Title',
        'element': 'p',
        'attributes': { 'class': 'talk-title' },
     },
]
#     'language': '{{ language }}',
#     'toolbar_CMS': [
#         ['Undo', 'Redo'],
#         ['cmsplugins', '-', 'ShowBlocks'],
#         ['Format', 'Styles'],
#     ],
#     'skin': 'moono',
# }
