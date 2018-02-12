FROM python:3.6

COPY ./requirements /{{cookiecutter.app_name}}/requirements
WORKDIR /{{cookiecutter.app_name}}

# install environment dependencies
RUN pip install -r ./requirements/prod.txt

COPY ./{{cookiecutter.app_name}} /{{cookiecutter.app_name}}
