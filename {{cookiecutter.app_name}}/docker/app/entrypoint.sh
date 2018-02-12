#!/bin/bash

echo "Waiting for postgres..."

# Wait fot the app service to com up
/wait_for_it.sh postgres:5432 --timeout=35 --strict

echo "PostgreSQL started"

gunicorn --config restapp/config/gunicorn.py "restapp.app:create_app()"
