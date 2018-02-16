FROM python:3.6

COPY ./app/requirements /app/requirements
WORKDIR /app
RUN pip install -r ./requirements/prod.txt
COPY ./app /app

# install node and npm
ENV NVM_DIR /usr/local/nvm
ENV NODE_VERSION 6.12
ENV NODE_PATH $NVM_DIR/v$NODE_VERSION/lib/node_modules
ENV PATH $NVM_DIR/versions/node/v$NODE_VERSION/bin:$PATH
RUN curl -o- https://raw.githubusercontent.com/creationix/nvm/v0.33.8/install.sh | bash \
    && . $NVM_DIR/nvm.sh \
    && nvm install $NODE_VERSION \
    && nvm alias default $NODE_VERSION \
    && nvm use default \
    && npm install \
    && npm run build