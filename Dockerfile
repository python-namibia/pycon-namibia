# <DOCKER_FROM>  # Warning: text inside the DOCKER_FROM tags is auto-generated. Manual changes will be overwritten.
FROM aldryn/base-project:latest
# </DOCKER_FROM>

# <DOCKER_BUILD>  # Warning: text inside the DOCKER_BUILD tags is auto-generated. Manual changes will be overwritten.

# python requirements
# -------------------
COPY requirements.in /app/
COPY addons-dev /app/addons-dev/
RUN pip-compile -v && pip install -r requirements.txt

# add full sourcecode and collectstatic
# -------------------------------------
COPY . /app
RUN DJANGO_MODE=build python manage.py collectstatic --noinput

# </DOCKER_BUILD>

