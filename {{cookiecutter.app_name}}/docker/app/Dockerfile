FROM python:3.6

COPY ./src/requirements /app/requirements

# install environment dependencies
RUN pip install -r /requirements/prod.txt

COPY ./src /app
COPY ./docker/app/entrypoint /app
