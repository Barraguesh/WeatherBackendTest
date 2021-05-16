FROM python:3.9-alpine

COPY ./requirements.txt /requirements.txt
RUN apk add --no-cache postgresql-libs && \
apk add --update --no-cache --virtual .tmp gcc libc-dev linux-headers gcc musl-dev postgresql-dev
RUN pip install -r /requirements.txt
RUN apk del .tmp

RUN mkdir /weatherAPI
COPY ./weatherAPI /weatherAPI
WORKDIR /weatherAPI

RUN mkdir -p /vol/web/

RUN adduser -D localapp
RUN chown -R localapp:localapp /vol
RUN chmod -R 755 /vol/web
USER localapp