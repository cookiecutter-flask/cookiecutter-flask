# cookiecutter-flask

A Flask template for [cookiecutter](https://github.com/audreyr/cookiecutter). (Supports Python ≥ 3.8)

![Build Status](https://github.com/cookiecutter-flask/cookiecutter-flask/workflows/Build%20Status/badge.svg)
![CodeQL](https://github.com/cookiecutter-flask/cookiecutter-flask/workflows/CodeQL/badge.svg)
[![CalVer](https://img.shields.io/badge/calver-YY.MINOR.MICRO-22bfda.svg)](http://calver.org)

See [this repo](https://github.com/jamescurtin/demo-cookiecutter-flask) for an example project generated from the most recent version of the template.

## Use it now

### Docker **(This is the preferred method for creating a new project)**

```bash
$ git clone https://github.com/cookiecutter-flask/cookiecutter-flask.git
$ cd cookiecutter-flask

# Basic usage (You will be prompted to provide basic information about your application)
$ ./cookiecutter-docker.sh
    full_name [Steven Loria]:
    ...
# The repository for your flask app will be created in a directory with the name
# chosen in "package import name" question (default ./my_flask_app/)

# Additional arguments are available
$ ./cookiecutter-docker.sh --help
    Usage: ./cookiecutter-docker.sh [OPTIONS]

Options:
    -b, --build    Build Docker image before running cookiecutter
    -h, --help     Show this message and exit
```

### Standard

If using standard instructions, Python ≥ 3.8 is required. A virtual environment is recommended (like `virtualenv`).

```bash
pip3 install cookiecutter
cookiecutter https://github.com/cookiecutter-flask/cookiecutter-flask.git
```

You will be asked about your basic info (name, project name, app name, etc.). This info will be used in your new project.

## Configure and Run

After you have generated the project code, a few more steps must be taken before your new app will run. The README of the generated project shows you how to configure and run the application. (You can see the [template README here](https://github.com/cookiecutter-flask/cookiecutter-flask/blob/master/%7B%7Bcookiecutter.app_name%7D%7D/README.md)).

## Features

- Bootstrap 5 and Font Awesome 6 with starter templates
- Flask-SQLAlchemy with basic User model
- Easy database migrations with Flask-Migrate
- Configuration in environment variables, as per [The Twelve-Factor App](https://12factor.net/config)
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
- Utilizes best practices: [Blueprints](http://flask.pocoo.org/docs/blueprints/) and [Application Factory](http://flask.pocoo.org/docs/patterns/appfactories/) patterns

## Screenshots

![Home page](https://user-images.githubusercontent.com/2379650/45271508-917f1c00-b475-11e8-9153-7f7385707a8b.png "Home page")

![Home page](https://user-images.githubusercontent.com/2379650/45271517-a9ef3680-b475-11e8-8de6-fbf3d9cab199.png "Registration form")

## Inspiration

- [Structuring Flask Apps](http://charlesleifer.com/blog/structuring-flask-apps-a-how-to-for-those-coming-from-django/)
- [Flask-Foundation](https://github.com/JackStouffer/Flask-Foundation) by [@JackStouffer](https://github.com/JackStouffer)
- [flask-bones](https://github.com/cburmeister/flask-bones) by [@cburmeister](https://github.com/cburmeister)
- [flask-basic-registration](https://github.com/mjhea0/flask-basic-registration) by [@mjhea0](https://github.com/mjhea0)
- [Flask Official Documentation](http://flask.pocoo.org/docs/)

## License

MIT licensed.

## Changelog

### Unreleased

- Update all node dependencies to latest versions
- Switch to using Github Actions for template CI
- Remove support for Node 10 as a Cookiecutter option
- Refactored Docker image to use multistage builds more efficiently
- Projects generated with the template use Github actions for CI
- Upgrade Webpack to 5.x
- Dropped Python 3.6 through 3.10 support
- Added Python 3.12, and 3.13 support
- Added Node 20 and 22 LTS
- Removed Node 12, 14, 16, and 18 LTS

### 18.0.0 (09/09/2018)

- Use CalVer (`YY.MINOR.MICRO`).
- Upgrade to Bootstrap 4. Thanks [@adawalli](https://github.com/adawalli) and [@Hiyorim](https://github.com/Hiyorimi).
- Use environment variables for configuration.
- Add support for Pipenv.
- Upgrade Python and Node dependencies.

### 0.13.0 (06/25/2017)

- Use webpack for building front-end assets. Front-end dependencies are
  installed with NPM. Remove Flask-Assets and bower.json. Thanks
  [@wroberts](https://github.com/wroberts).

### 0.12.0 (11/06/2016)

- Update Python dependencies.

### 0.11.1 (11/06/2016)

- Correctly pass first parameter to `Flask` according to the 0.11 [docs](http://flask.pocoo.org/docs/0.11/api/#application-object). Thanks [@aliavni](https://github.com/aliavni).
- Remove setuptools and wheel as dependencies to fix deployment on Heroku. Thanks [@Cabalist](https://github.com/Cabalist).
- Make User.password a Binary field for compatibility with new versions of bcrypt. Thanks again [@Cabalist](https://github.com/Cabalist).

### 0.11.0 (09/10/2016)

- Use the FLASK_DEBUG system environment variable, instead of MYFLASKAPP_ENV, to control different configs for development and production environments

### 0.10.1 (08/28/2016)

- Fix `invoke test` command.

### 0.10.0 (08/28/2016)

- Update to Flask 0.11.
- Use Click instead of Flask-Script for CLI commands.

### 0.9.0 (03/06/2016)

- Update stale requirements.
- Add CSRF protection.
- Run `lint` command on Travis builds.
- Test against Python 3.5.

### 0.8.0 (11/09/2015)

- Update stale requirements.
- Add `lint`, `clean`, and `urls` management commands.
- Add isort.

Thanks @andreoliw for these contributions.

### 0.7.0 (04/14/2015)

- Update extension import style to flask_* as per [mitsuhiko/flask#1135](https://github.com/mitsuhiko/flask/issues/1135).
- Update stale requirements (Werkzeug, Flask-WTF, WTForms, Flask-Bcrypt, Flask-DebugToolbar, Flask-Migrate, Bootstrap, jQuery). Thanks @bsmithgall for notifying me of the critical patch to Flask-Migrate.

### 0.6.0 (12/01/2014)

- Test the cookiecutter on Travis. Thanks @joshfriend.
- Update stale requirements (Flask-WTF, Flask-Migrate, Flask-DebugToolbar)

### 0.5.0 (09/29/2014)

- Fix .travis.yml.
- Update stale requirements (Flask-WTF, WTForms, Flask-SQLAlchemy, jquery, Bootstrap)

### 0.4.3 (07/27/2014)

- Add `BaseFactory` class.
- Add compat.py module.
- Tests pass on Python 3.

### 0.4.2 (07/27/2014)

- Update factories to factory-boy >= 2.4.0 syntax.
- Update stale requirements.

### 0.4.1 (06/07/2014)

- Update stale requirements (Werkzeug 0.9.6, WTForms 2.0)
- Fix unmatched div tag in home.html (thanks [@level09](https://github.com/level09))

### 0.4.0 (04/19/2014)

- Add ReferenceCol for less verbose foreign key columns.
- Add SurrogatePK mixin for adding integer primary key to a model.
- Add base Model class that has CRUD convenience methods.
- Fix setting BCrypt encryption complexity. Tests are much faster.
- Add Role model to show ReferenceCol usage.
- Switch to pytest.
- Upgrade all out-of-date requirements.
- More test examples.
- Remove "year" from cookiecutter.json (just change LICENSE if necessary).

### 0.3.2 (02/26/2014)

- Fix static assets.

### 0.3.1 (02/20/2014)

- Update default year in cookiecutter.json. Thanks @Omeryl
- Correct testing of redirects in webtests. Thanks @Widdershin
- Fix POST action in nav form. Thanks @Widdershin.
- Update Bootstrap (3.1.1) and jQuery (2.1.0)
- Optional support for bower.
- Minified assets aren't used in dev environment.

### 0.3.0 (12/08/2013)

- More modular organization: each blueprint contains its own view, models, and forms in a directory. There is still a single directory for templates and static assets.
- Use Flask-Bcrypt for password hashing.
- Flask-Login for authentication.
- Simple test setup. Just create a subclass of `DbTestCase`.
- Flask-Testing support.
- Use Factory-Boy for test factories.
- Use WebTest for functional testing.
- Add Flask-Debugtoolbar.
- Migrations using Flask-Migrate.
- Caching using Flask-Cache.
- Add error page templates (404, 401, 500)
- Add Font Awesome 4.0.3 for icons.

### 0.2.0 (09/21/2013)

- Add manage.py script
- Add Flask-Assets for CSS and JS bundling+minification
- Use different configs for development and production environments, controlled by the MYFLASKAPP_ENV system environment variable
- Use Blueprints and application factory pattern. The `simple` branch does not use these.

### 0.1.0 (08/20/2013)

- First iteration
- Bootstrap 3 final
- Working User model and registration
