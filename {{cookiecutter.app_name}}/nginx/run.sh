#!/bin/bash

# Ensure logs directory exists
mkdir -p  /data/logs/nginx

# Wait fot the app service to com up
/wait_for_it.sh app:$APP_PORT --timeout=35 --strict

# Override default config with custom nginx.conf while resolving env files.
envsubst '${APP_PORT}' < /config/nginx.conf > /etc/nginx/nginx.conf

echo "Starting NGINX..."
nginx