FROM python:3.7-alpine

RUN apk update \
    && apk upgrade \
    && apk add --no-cache git

RUN pip install \
    cookiecutter==1.6.0

ENTRYPOINT [ "python", "-m", "cookiecutter" ]
