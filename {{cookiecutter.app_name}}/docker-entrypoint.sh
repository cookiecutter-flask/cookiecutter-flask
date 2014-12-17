#!/bin/bash
set -e

python manage.py create_all

exec "$@"