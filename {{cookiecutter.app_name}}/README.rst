===============================
{{ cookiecutter.project_name }}
===============================

{{ cookiecutter.project_short_description}}


Quickstart
----------

First, set your app's secret key as an environment variable. For example,
add the following to ``.bashrc`` or ``.bash_profile``.

.. code-block:: bash

    export {{cookiecutter.app_name | upper}}_SECRET='something-really-secret'

Run the following commands to bootstrap your environment ::

    git clone https://github.com/{{cookiecutter.github_username}}/{{cookiecutter.app_name}}
    cd {{cookiecutter.app_name}}
    pip install -r requirements/dev.txt
    npm install
    npm start  # run the webpack dev server and flask server using concurrently

You will see a pretty welcome screen.

In general, before running shell commands, set the ``FLASK_APP`` and
``FLASK_DEBUG`` environment variables ::

    export FLASK_APP=autoapp.py
    export FLASK_DEBUG=1

Once you have installed your DBMS, run the following to create your app's
database tables and perform the initial migration ::

    flask db init
    flask db migrate
    flask db upgrade
    npm start


Deployment
----------

To deploy::

    export FLASK_DEBUG=0
    npm run build   # build assets with webpack
    flask run       # start the flask server

In your production environment, make sure the ``FLASK_DEBUG`` environment
variable is unset or is set to ``0``, so that ``ProdConfig`` is used.


Shell
-----

To open the interactive shell, run ::

    flask shell

By default, you will have access to the flask ``app``.


Running Tests
-------------

To run all tests, run ::

    flask test


Migrations
----------

Whenever a database migration needs to be made. Run the following commands ::

    flask db migrate

This will generate a new migration script. Then run ::

    flask db upgrade

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

Deploying to Heroku::

In order to deploy this to Heroku you need to do a few extra things.  First off, make sure you have already gone through
the Quickstart above as you will need to run some commands locally to get your migrations initialized before pushing that
to Heroku.  Also, make sure you have ran git init to initialize your git repo.  Heroku uses git to deploy and when you run
heroku create below it will add the git remote for you new app.

First, in order to build the static assets using webpack, you need to add a postinstall script to the package.json.  This
is the preferred approach to building static assets on Heroku.  To do this, simply update the package.json "scripts" section
with the following::

    "postinstall": "npm run build"

Next, in order to run db migrations as part of the deployment, update the Procfile to look like::


    release: flask db upgrade
    web: gunicorn total_life_challenge.app:create_app\(\) -b 0.0.0.0:$PORT -w 3

You will also need to update your SQLALCHEMY_DATABASE_URI in the Production config to the following::

    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL')

At this point you are ready to create the Heroku app, to do this we not only need to create it but also need to ensure
we have the nodejs and python buildpacks installed.  We will also add Postgres as well.  To do this, assuming you already
have the Heroku CLI installed, run the following::

    heroku create
    heroku buildpacks:add --index=1 heroku/nodejs
    heroku buildpacks:add --index=1 heroku/python
    heroku addons:create heroku-postgresql:hobby-dev

Finally, before we deploy we need to set the FLASK_APP environment variable on the app we just created so that the flask
commands work properly.  To do this, go to your Heroku Dashboard and select the App we created above with heroku create.
Once there, click on Settings > Reveal Config Vars and add the following::

    Key: FLASK_APP Value: autoapp.py

Now we are ready to deploy the app.  Simply do the following::

    git add .
    git commit -m"Added heroku configuration"
    git push heroku master

Once that is done, you should see your app successfully deployed in the console.  You can now run the following to open
the app in a browser::

    heroku open

At this point you should have a fully functional application using a postgres database.
