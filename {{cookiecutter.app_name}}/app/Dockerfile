FROM python:3.6

COPY ./app/requirements /app/requirements
COPY ./app/package.json /app/package.json
WORKDIR /app

# install environment dependencies
RUN pip install -r requirements/prod.txt \
    && nvm install 6.10 \
    && nvm use 6.10 \
    && npm install

COPY ./app /app
