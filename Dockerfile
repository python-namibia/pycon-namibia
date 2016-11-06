# <DOCKER_FROM>  # Warning: text inside the DOCKER_FROM tags is auto-generated. Manual changes will be overwritten.
FROM aldryn/base-project:py3-3.18
# </DOCKER_FROM>

# <DOCKER_BUILD>  # Warning: text inside the DOCKER_BUILD tags is auto-generated. Manual changes will be overwritten.

# python requirements
# -------------------
ENV PIP_INDEX_URL=${PIP_INDEX_URL:-https://wheels.aldryn.net/v1/aldryn-extras+pypi/aldryn-baseproject-py3/+simple/} \
    WHEELSPROXY_URL=${WHEELSPROXY_URL:-https://wheels.aldryn.net/v1/aldryn-extras+pypi/aldryn-baseproject-py3/}
COPY requirements.* /app/
COPY addons-dev /app/addons-dev/
RUN pip-reqs compile && \
    pip-reqs resolve && \
    pip install \
        --no-index --no-deps \
        --requirement requirements.urls

# add full sourcecode
# -------------------
COPY . /app

# collectstatic
# -------------
RUN DJANGO_MODE=build python manage.py collectstatic --noinput

# </DOCKER_BUILD>

