===============================
{{ cookiecutter.project_name }}
===============================

{{ cookiecutter.project_short_description}}


Quickstart
----------

.. code-block:: bash

    git clone https://github.com/{{cookiecutter.github_username}}/{{cookiecutter.app_name}}
    cd {{cookiecutter.app_name}}
    docker-compose build
    docker-compose up -d
    docker exec myflaskapp_app_1 flask db init
    docker exec myflaskapp_app_1 flask db migrate
    docker exec myflaskapp_app_1 flask db upgrade

Where myflaskapp_app_1 is the name of the app container created, or you can check the name of your
container name by following the following:

.. code-block:: bash

    docker ps


Deployment
----------

To deploy to Production::

.. code-block:: bash
    cd {{cookiecutter.app_name}}
    docker-compose -f docker-compose.yml -f docker-compose-prod.yaml build
    docker-compose -f docker-compose.yml -f docker-compose-prod.yaml up -d
    docker exec myflaskapp_app_1 flask db init
    docker exec myflaskapp_app_1 flask db migrate
    docker exec myflaskapp_app_1 flask db upgrade

To do live development::

.. code-block:: bash
    cd {{cookiecutter.app_name}}
    docker-compose -f docker-compose.yml -f docker-compose-dev.yaml build
    docker-compose -f docker-compose.yml -f docker-compose-dev.yaml up -d
    docker exec myflaskapp_app_1 flask db init
    docker exec myflaskapp_app_1 flask db migrate
    docker exec myflaskapp_app_1 flask db upgrade

Shell
-----

To open the interactive shell from the host machine, run ::

    docker exec -it myflaskapp_app_1 flask shell

By default, you will have access to the flask ``app``.


Running Tests
-------------

To run all tests on the host machine, run ::

    docker exec -it myflaskapp_app_1 flask test


Migrations
----------

Whenever a database migration needs to be made. Run the following commands ::

    docker exec -it myflaskapp_app_1 flask db migrate

This will generate a new migration script. Then run ::

    docker exec -it myflaskapp_app_1 flask db upgrade

To apply the migration.

For a full migration command reference, run ``flask db --help``.


Asset Management
----------------

Files placed inside the ``assets`` directory and its subdirectories
(excluding ``js`` and ``css``) will be copied by webpack's
``file-loader`` into the ``static/build`` directory, with hashes of
their contents appended to their names.  For instance, if you have the
file ``assets/img/favicon.ico``, this will get copied into something
like
``static/build/img/favicon.fec40b1d14528bf9179da3b6b78079ad.ico``.
You can then put this line into your header::

    <link rel="shortcut icon" href="{{ "{{" }}asset_url_for('img/favicon.ico') {{ "}}" }}">

to refer to it inside your HTML page.  If all of your static files are
managed this way, then their filenames will change whenever their
contents do, and you can ask Flask to tell web browsers that they
should cache all your assets forever by including the following line
in your ``settings.py``::

    SEND_FILE_MAX_AGE_DEFAULT = 31556926  # one year
