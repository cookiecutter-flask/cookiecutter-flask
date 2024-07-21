# ================================== BUILDER ===================================
ARG INSTALL_PYTHON_VERSION=${INSTALL_PYTHON_VERSION:-PYTHON_VERSION_NOT_SET}
ARG INSTALL_NODE_VERSION=${INSTALL_NODE_VERSION:-NODE_VERSION_NOT_SET}

FROM node:${INSTALL_NODE_VERSION}-bullseye-slim AS node
FROM python:${INSTALL_PYTHON_VERSION}-slim-bullseye AS builder

WORKDIR /app

COPY --from=node /usr/local/bin/ /usr/local/bin/
COPY --from=node /usr/lib/ /usr/lib/
# See https://github.com/moby/moby/issues/37965
RUN true
COPY --from=node /usr/local/lib/node_modules /usr/local/lib/node_modules

{%- if cookiecutter.use_pipenv == "True" %}
COPY ["Pipfile", "shell_scripts/auto_pipenv.sh", "./"]
RUN pip install --no-cache pipenv
RUN pipenv install
{%- else %}
COPY requirements requirements
RUN pip install --no-cache -r requirements/prod.txt
{%- endif %}

COPY package.json ./
RUN npm install

COPY webpack.config.js autoapp.py ./
COPY {{cookiecutter.app_name}} {{cookiecutter.app_name}}
COPY assets assets
COPY .env.example .env
RUN npm run-script build

# ================================= PRODUCTION =================================
FROM python:${INSTALL_PYTHON_VERSION}-slim-bullseye as production

WORKDIR /app

RUN useradd -m sid
RUN chown -R sid:sid /app
USER sid
ENV PATH="/home/sid/.local/bin:${PATH}"

COPY --from=builder --chown=sid:sid /app/{{ cookiecutter.app_name }}/static /app/{{ cookiecutter.app_name }}/static

{%- if cookiecutter.use_pipenv == "True" %}
COPY ["Pipfile", "shell_scripts/auto_pipenv.sh", "./"]
RUN pip install --no-cache pipenv
RUN pipenv install
{%- else %}
COPY requirements requirements
RUN pip install --no-cache --user -r requirements/prod.txt
{%- endif %}

COPY supervisord.conf /etc/supervisor/supervisord.conf
COPY supervisord_programs /etc/supervisor/conf.d

COPY . .

EXPOSE 5000
ENTRYPOINT ["/bin/bash", "shell_scripts/supervisord_entrypoint.sh"]
CMD ["-c", "/etc/supervisor/supervisord.conf"]


# ================================= DEVELOPMENT ================================
FROM builder AS development

{%- if cookiecutter.use_pipenv == "True" %}
RUN pipenv install --dev
{%- else %}
RUN pip install --no-cache -r requirements/dev.txt
{%- endif %}
EXPOSE 2992
EXPOSE 5000
CMD [ {% if cookiecutter.use_pipenv == 'True' %}"pipenv", "run", {% endif %}"npm", "start" ]
