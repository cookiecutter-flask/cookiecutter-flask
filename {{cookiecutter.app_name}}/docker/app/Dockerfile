FROM python:3.6

COPY ./requirements /{{cookiecutter.app_name}}/requirements

# install environment dependencies
RUN pip install -r /{{cookiecutter.app_name}}/requirements/prod.txt

COPY ./{{cookiecutter.app_name}} /{{cookiecutter.app_name}}
COPY ./docker/app/entrypoint /
