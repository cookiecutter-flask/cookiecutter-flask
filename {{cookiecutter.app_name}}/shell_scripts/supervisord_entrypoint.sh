#!/usr/bin/env sh
set -e

npm run build

{%- if cookiecutter.use_pipenv == "yes" %}
source ./shell_scripts/auto_pipenv.sh
auto_pipenv_shell
{%- endif %}

if [ $# -eq 0 ] || [ "${1#-}" != "$1" ]; then
  set -- supervisord "$@"
fi

exec "$@"
