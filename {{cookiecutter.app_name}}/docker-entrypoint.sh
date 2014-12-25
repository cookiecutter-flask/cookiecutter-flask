#!/bin/bash
set -e

# Wait for database to start up
sleep 2

python manage.py create_all

exec "$@"
