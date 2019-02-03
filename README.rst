cookiecutter-flask
==================

A Flask template for cookiecutter_.

.. _cookiecutter: https://github.com/audreyr/cookiecutter

.. image:: https://travis-ci.org/sloria/cookiecutter-flask.svg?branch=master
    :target: https://travis-ci.org/sloria/cookiecutter-flask
    :alt: Build Status

.. image:: https://img.shields.io/badge/calver-YY.MINOR.MICRO-22bfda.svg
    :target: http://calver.org
    :alt: CalVer


Use it now
----------
::

    $ pip install cookiecutter
    $ cookiecutter https://github.com/sloria/cookiecutter-flask.git

You will be asked about your basic info (name, project name, app name, etc.). This info will be used in your new project.

Features
--------

- Bootstrap 4 and Font Awesome 4 with starter templates
- Flask-SQLAlchemy with basic User model
- Easy database migrations with Flask-Migrate
- Configuration in environment variables, as per `The Twelve-Factor App <https://12factor.net/config>`_
- Flask-WTForms with login and registration forms
- Flask-Login for authentication
- Flask-Bcrypt for password hashing
- Procfile for deploying to a PaaS (e.g. Heroku)
- pytest and Factory-Boy for testing (example tests included)
- Flask's Click CLI configured with simple commands
- CSS and JS minification using webpack
- npm support for frontend package management
- Caching using Flask-Cache
- Useful debug toolbar
- Utilizes best practices: `Blueprints <http://flask.pocoo.org/docs/blueprints/>`_ and `Application Factory <http://flask.pocoo.org/docs/patterns/appfactories/>`_ patterns

Screenshots
-----------

.. image:: https://user-images.githubusercontent.com/2379650/45271508-917f1c00-b475-11e8-9153-7f7385707a8b.png
    :alt: Home page

.. image:: https://user-images.githubusercontent.com/2379650/45271517-a9ef3680-b475-11e8-8de6-fbf3d9cab199.png
    :alt: Registration form



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

MIT licensed.

Changelog
---------

18.0.0 (09/09/2018)
*******************

- Use CalVer (``YY.MINOR.MICRO``).
- Upgrade to Bootstrap 4. Thanks `@adawalli <https://github.com/adawalli>`_ and `@Hiyorimi <https://github.com/Hiyorimi>`_.
- Use environment variables for configuration.
- Add support for Pipenv.
- Upgrade Python and Node dependencies.

0.13.0 (06/25/2017)
*******************

- Use webpack for building front-end assets. Front-end dependencies are
  installed with NPM. Remove Flask-Assets and bower.json. Thanks
  `@wroberts <https://github.com/wroberts>`_.

0.12.0 (11/06/2016)
*******************

- Update Python dependencies.

0.11.1 (11/06/2016)
*******************

- Correctly pass first parameter to ``Flask`` according to the 0.11 `docs <http://flask.pocoo.org/docs/0.11/api/#application-object>`_. Thanks `@aliavni <https://github.com/aliavni>`_.
- Remove setuptools and wheel as dependencies to fix deployment on Heroku. Thanks `@Cabalist <https://github.com/Cabalist>`_.
- Make User.password a Binary field for compatibility with new versions of bcrypt. Thanks again `@Cabalist <https://github.com/Cabalist>`_.

0.11.0 (09/10/2016)
*******************

- Use the FLASK_DEBUG system environment variable, instead of MYFLASKAPP_ENV, to control different configs for development and production environments

0.10.1 (08/28/2016)
*******************

- Fix ``invoke test`` command.

0.10.0 (08/28/2016)
*******************

- Update to Flask 0.11.
- Use Click instead of Flask-Script for CLI commands.

0.9.0 (03/06/2016)
******************

- Update stale requirements.
- Add CSRF protection.
- Run ``lint`` commmand on Travis builds.
- Test against Python 3.5.

0.8.0 (11/09/2015)
******************

- Update stale requirements.
- Add ``lint``, ``clean``, and ``urls`` management commands.
- Add isort.

Thanks @andreoliw for these contributions.

0.7.0 (04/14/2015)
******************

- Update extension import style to flask_* as per `mitsuhiko/flask#1135 <https://github.com/mitsuhiko/flask/issues/1135>`_
- Update stale requirements (Werkzeug, Flask-WTF, WTForms, Flask-Bcrypt, Flask-DebugToolbar, Flask-Migrate, Bootstrap, jQuery). Thanks @bsmithgall for notifying me of the critical patch to Flask-Migrate.

0.6.0 (12/01/2014)
******************

- Test the cookiecutter on Travis. Thanks @joshfriend.
- Update stale requirements (Flask-WTF, Flask-Migrate, Flask-DebugToolbar)

0.5.0 (09/29/2014)
******************

- Fix .travis.yml.
- Update stale requirements (Flask-WTF, WTForms, Flask-SQLAlchemy, jquery, Bootstrap)

0.4.3 (07/27/2014)
******************

- Add ``BaseFactory`` class.
- Add compat.py module.
- Tests pass on Python 3.

0.4.2 (07/27/2014)
******************

- Update factories to factory-boy >= 2.4.0 syntax.
- Update stale requirements.

0.4.1 (06/07/2014)
******************

- Update stale requirements (Werkzeug 0.9.6, WTForms 2.0)
- Fix unmatched div tag in home.html (thanks `@level09 <https://github.com/level09>`_ )


0.4.0 (04/19/2014)
******************

- Add ReferenceCol for less verbose foreign key columns.
- Add SurrogatePK mixin for adding integer primary key to a model.
- Add base Model class that has CRUD convenience methods.
- Fix setting BCrypt encryption complexity. Tests are much faster.
- Add Role model to show ReferenceCol usage.
- Switch to pytest.
- Upgrade all out-of-date requirements.
- More test examples.
- Remove "year" from cookiecutter.json (just change LICENSE if necessary).

0.3.2 (02/26/2014)
******************

- Fix static assets.

0.3.1 (02/20/2014)
******************

- Update default year in cookiecutter.json. Thanks @Omeryl
- Correct testing of redirects in webtests. Thanks @Widdershin
- Fix POST action in nav form. Thanks @Widdershin.
- Update Bootstrap (3.1.1) and jQuery (2.1.0)
- Optional support for bower.
- Minified assets aren't used in dev environment.


0.3.0 (12/08/2013)
******************

- More modular organization: each blueprint contains its own view, models, and forms in a directory. There is still a single directory for templates and static assets.
- Use Flask-Bcrypt for password hashing.
- Flask-Login for authentication.
- Simple test setup. Just create a subclass of ``DbTestCase``.
- Flask-Testing support.
- Use Factory-Boy for test factories.
- Use WebTest for functional testing.
- Add Flask-Debugtoolbar.
- Migrations using Flask-Migrate.
- Caching using Flask-Cache.
- Add error page templates (404, 401, 500)
- Add Font Awesome 4.0.3 for icons.

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
