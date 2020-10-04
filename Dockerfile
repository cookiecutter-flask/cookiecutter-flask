FROM python:3.8-slim-buster

RUN pip install --no-cache-dir \
    cookiecutter==1.7.2

RUN useradd -m sid
USER sid

ENTRYPOINT [ "python", "-m", "cookiecutter" ]
