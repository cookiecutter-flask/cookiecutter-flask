FROM python:3.9.13-slim-buster

COPY requirements.txt requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

COPY cookiecutter_spec.py /cookiecutter_spec.py
ENTRYPOINT [ "python", "/cookiecutter_spec.py" ]
