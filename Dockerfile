# pull official base image
FROM python:3.6-alpine

# set environment variables
ENV PYTHONUNBUFFERED 1

# make directory to copy code
RUN mkdir /code

# set work directory
WORKDIR /code

# copy project
COPY . .

COPY .env.production .env

# upgrade pip to latest version
RUN pip install --upgrade pip

# install gunicorn
RUN pip install gunicorn

# install dependencies
RUN \
 apk add --no-cache postgresql-libs && \
 apk add --no-cache --virtual .build-deps gcc musl-dev postgresql-dev && \
 python3 -m pip install -r docs/requirements.txt --no-cache-dir && \
 apk --purge del .build-deps

# collect all static files in single location
#RUN python3 manage.py collectstatic --noinput

COPY ./docker-entrypoint.sh /
ENTRYPOINT ["sh","/code/docker-entrypoint.sh"]
