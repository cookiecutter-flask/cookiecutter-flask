# coding: utf-8
# Core and 3th party packages
import signal
import time
import click
import psycopg2
import os
from django.conf import settings

# Utils Imports
from runutils import run_daemon, runbash, ensure_dir, getvar, run_cmd


def waitfordb(stopper):
    """ Wait for the database to accept connections. """
    tick = 0.1
    intervals = 100 * [10]
    for i in intervals:
        click.echo('checking connection ...')
        try:
            psycopg2.connect(host='postgres', port=5432, database="django",
                             user="postgres", password=getvar('DB_PASSWORD'))
        except Exception as e:
            click.echo('could not connect yet')
            click.echo(e)
        else:
            return

        for w in range(i):
            if stopper.stopped:
                return
            time.sleep(tick)


{%- if cookiecutter.use_translation == 'True' %}


def generate_makemessages_command(domain):
    command = ['django-admin', 'makemessages', '-d', domain]

    for lang in settings.LANGUAGES:
        if lang[0] != settings.LANGUAGE_CODE:
            command.append('-l=' + lang[0])
    return command
{%- endif %}


# INIT: WILL RUN BEFORE ANY COMMAND AND START  #
def init(stopper):
    ensure_dir('/data/logs/', owner='developer', group='developer')
    ensure_dir('/data/logs/django', owner='developer', group='developer')
    ensure_dir('/data/static', owner='developer', group='developer')
    {% if cookiecutter.use_translation == 'True' -%}
    ensure_dir('/src/locale', owner='developer', group='developer')
    {%- endif %}
    if not stopper.stopped:
        if settings.DEBUG is False:
            {%- if cookiecutter.use_react == 'True' %}
            cmd = ['django-admin', 'collectstatic', '--noinput', '-i', 'react']
            {% else %}
            cmd = ['django-admin', 'collectstatic', '--noinput']
            {% endif -%}
            run_cmd(cmd, user='developer')

        # Create db cache and other one time commands
        if os.path.isfile('/data/.init') is False:
            run_cmd(['django-admin', 'migrate'], user='developer')
            run_cmd(['django-admin', 'createcachetable', '-v', '0'],
                    user='developer')

            with open("/data/.init", "a+") as f:
                f.write(''){% if cookiecutter.use_translation == 'True' %}

        run_cmd(generate_makemessages_command('django'), user='developer')
        run_cmd(generate_makemessages_command('djangojs'), user='developer'){% endif %}


@click.group()
def run():
    pass


@run.command()
@click.argument('user', default='developer')
def shell(user):
    runbash(user)


@run.command()
def start_runserver():
    start = ['django-admin.py', 'runserver', '0.0.0.0:8000']
    run_daemon(start, signal_to_send=signal.SIGINT, user='developer',
               waitfunc=waitfordb, initfunc=init)


@run.command()
def start_uwsgi():
    """Starts the service."""
    start = ["uwsgi", "--ini", '/config/uwsgi.conf', '--post-buffering', '1']
    run_daemon(start, signal_to_send=signal.SIGQUIT, user='developer',
               waitfunc=waitfordb, initfunc=init)


if __name__ == '__main__':
    run()
