FROM python:3.6

COPY ./app/requirements /app/requirements
WORKDIR /app

# install environment dependencies
RUN pip install -r requirements/prod.txt

COPY ./app /app
