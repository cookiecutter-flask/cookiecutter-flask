cookiecutter-flask
==================

A Flask template for cookiecutter_.

.. _cookiecutter: https://github.com/audreyr/cookiecutter

Features
--------

- Twitter Bootstrap 3 and starter templates
- Flask-SQLAlchemy with basic User model
- Flask-WTForms with login and registration forms
- Procfile for deploying to a PaaS (e.g. Heroku)
- nose for testing
- A simple ``manage.py`` script.
- Easily switch between development and production environments through the MYFLASKAPP_ENV system  variable.

Screenshots
-----------

.. image:: https://dl.dropboxusercontent.com/u/1693233/github/cookiecutter-flask-01.png
    :target: https://dl.dropboxusercontent.com/u/1693233/github/cookiecutter-flask-01.png
    :alt: Home page

.. image:: https://dl.dropboxusercontent.com/u/1693233/github/cookiecutter-flask-02.png.png
    :target: https://dl.dropboxusercontent.com/u/1693233/github/cookiecutter-flask-02.png.png
    :alt: Registration form

Using this template
-------------------
::

    $ pip install cookiecutter
    $ cookiecutter https://github.com/sloria/cookiecutter-flask.git

You will be asked about your basic info (name, project name, etc.). This info will be used in your new project.


License
-------
BSD licensed.

