FROM python:3.10.0b3-slim-buster

COPY requirements.txt requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

COPY cookiecutter_spec.py /cookiecutter_spec.py
ENTRYPOINT [ "python", "/cookiecutter_spec.py" ]
