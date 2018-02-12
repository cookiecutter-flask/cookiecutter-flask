FROM python:3.6

COPY . /{{cookiecutter.app_name}}
WORKDIR /{{cookiecutter.app_name}}

# install environment dependencies
RUN pip install -r /requirements/prod.txt
