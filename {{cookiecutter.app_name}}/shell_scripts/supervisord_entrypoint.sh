#!/usr/bin/env sh
set -e

{%- if cookiecutter.use_pipenv == "True" %}
source ./shell_scripts/auto_pipenv.sh
auto_pipenv_shell
{%- endif %}

if [ $# -eq 0 ] || [ "${1#-}" != "$1" ]; then
  set -- supervisord "$@"
fi

exec "$@"
