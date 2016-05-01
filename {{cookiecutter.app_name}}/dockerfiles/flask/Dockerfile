FROM python:3.5
ENV PYTHONUNBUFFERED 1

COPY requirements /requirements
RUN pip install -r /requirements/dev.txt

RUN groupadd -r flask && useradd -r -g flask flask
COPY . /app

RUN chown -R flask /app

WORKDIR /app