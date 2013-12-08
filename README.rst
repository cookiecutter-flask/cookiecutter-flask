cookiecutter-flask
==================

A Flask template for cookiecutter_.

.. _cookiecutter: https://github.com/audreyr/cookiecutter

Features
--------

- Twitter Bootstrap 3 and starter templates
- Flask-SQLAlchemy with basic User model
- Flask-WTForms with login and registration forms
- Flask-Login for authentication
- Procfile for deploying to a PaaS (e.g. Heroku)
- Flask-Testing, Flask-Webtest, nose, and Factory-Boy for testing
- A simple ``manage.py`` script.
- CSS and JS minification using Flask-Assets
- Utilizes best practices: `Blueprints <http://flask.pocoo.org/docs/blueprints/>`_ and `Application Factory <http://flask.pocoo.org/docs/patterns/appfactories/>`_ patterns

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

Blueprints? App factories?
--------------------------

If you prefer not to use blueprints or an application factory, check out the ``simple`` branch which has the older structure without these patterns. Note, however, only the ``master`` branch will be actively maintained.

Inspiration
-----------

- `Building Websites in Python with Flask <http://maximebf.com/blog/2012/10/building-websites-in-python-with-flask/>`_
- `Getting Bigger with Flask <http://maximebf.com/blog/2012/11/getting-bigger-with-flask/>`_
- `Structuring Flask Apps <http://charlesleifer.com/blog/structuring-flask-apps-a-how-to-for-those-coming-from-django/>`_
- `Flask-Foundation <https://github.com/JackStouffer/Flask-Foundation>`_ by `@JackStouffer <https://github.com/JackStouffer>`_
- `flask-bones <https://github.com/cburmeister/flask-bones>`_ by `@cburmeister <https://github.com/cburmeister>`_
- `flask-basic-registration <https://github.com/mjhea0/flask-basic-registration>`_ by `@mjhea0 <https://github.com/mjhea0>`_
- `Flask Official Documentation <http://flask.pocoo.org/docs/>`_


License
-------
BSD licensed.

Changelog
---------

0.3.0
*****

- More modular organization: each blueprint contains its own view, models, and forms in a directory. There is still a single directory for templates and static assets.
- Use Flask-Bcrypt for password hashing.
- Flask-Login for authentication.
- Simple test setup. Just create a subclass of ``DbTestCase``.
- Flask-Testing support.
- Use Factory-Boy for test factories.
- Use WebTest for functional testing.

0.2.0 (09/21/2013)
******************
- Add manage.py script
- Add Flask-Assets for CSS and JS bundling+minification
- Use different configs for development and production environments, controlled by the MYFLASKAPP_ENV system environment variable
- Use Blueprints and application factory pattern. The ``simple`` branch does not use these.

0.1.0 (08/20/2013)
******************
- First iteration
- Bootstrap 3 final
- Working User model and registration


