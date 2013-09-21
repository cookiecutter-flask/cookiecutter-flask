===============================
{{ cookiecutter.project_name }}
===============================

{{ cookiecutter.project_short_description}}


Quickstart
----------

::

    git clone https://github.com/{{cookiecutter.github_username}}/{{ cookiecutter.repo_name }}
    cd {{cookiecutter.repo_name}}
    pip install -r requirements/dev.txt
    export {{cookiecutter.repo_name|upper}}_ENV='dev'
    python manage.py createdb
    python manage.py runserver


Shell
-----

To open the interactive shell, run ::

    python manage.py shell

By default, you will have access to ``app``, ``models``, and ``db``.

Development / Production Environments
-------------------------------------

Configuration environements are handled through the {{cookiecutter.repo_name|upper}}_ENV system environment variable.

To switch to the development environment, set ::

    export {{cookiecutter.repo_name|upper}}_ENV="dev"

To switch to the production environment, set ::

    export {{cookiecutter.repo_name|upper}}_ENV="prod"
