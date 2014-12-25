FROM python:3.4.2-wheezy

MAINTAINER {{ cookiecutter.full_name }}

RUN echo "deb http://http.debian.net/debian wheezy main" > /etc/apt/sources.list && \
	apt-get update && \
	apt-get install -y python-psycopg2

RUN pip install gunicorn==19.1.1

COPY . /{{cookiecutter.app_name}}

RUN pip install -r /{{cookiecutter.app_name}}/requirements/prod.txt

WORKDIR /{{cookiecutter.app_name}}

ENV {{cookiecutter.app_name | upper}}_ENV prod

ENTRYPOINT ["/{{cookiecutter.app_name}}/docker-entrypoint.sh"]

EXPOSE 8000
CMD gunicorn -b 0.0.0.0:8000 -w 2 {{cookiecutter.app_name}}.app:create_app\(\) 2>&1
