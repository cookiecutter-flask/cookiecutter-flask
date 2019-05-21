#!/usr/bin/env sh

function auto_pipenv_shell {
    if [ -f "Pipfile" ] ; then
        source "$(pipenv --venv)/bin/activate"
    fi
}
