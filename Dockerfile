FROM python:3.8-slim-buster

RUN pip install \
    cookiecutter==1.6.0

RUN useradd -m sid
USER sid

ENTRYPOINT [ "python", "-m", "cookiecutter" ]
