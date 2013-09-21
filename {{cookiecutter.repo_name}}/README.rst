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
    python manage.py createdb
    python manage.py runserver


Shell
-----

To open the interactive shell, run ::

    python manage.py shell

By default, you will have access to ``app``, ``models``, and ``db``.
