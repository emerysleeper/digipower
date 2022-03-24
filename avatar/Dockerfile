#Set up the Linux working directory
FROM python:3.9.4-alpine
WORKDIR /usr/src/app


#Set env variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1
ENV IS_CONTAINER 1

#Requirements
COPY ./req.txt /usr/src/app/req.txt

RUN apk --update add libxml2-dev libxslt-dev libffi-dev gcc musl-dev libgcc openssl-dev curl
RUN apk add jpeg-dev zlib-dev freetype-dev lcms2-dev openjpeg-dev tiff-dev tk-dev tcl-dev

#Dependencies
RUN set -eux \
    && apk add --no-cache --virtual .build-deps build-base \
        libressl-dev libffi-dev gcc musl-dev python3-dev \
    && pip install --upgrade pip setuptools wheel \
    && pip install -r /usr/src/app/req.txt \
    && rm -rf /root/.cache/pip

COPY . /usr/src/app/