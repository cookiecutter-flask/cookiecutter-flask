#!/bin/bash

# Wait fot the app service to com up
/wait_for_it.sh restapp:$APP_PORT --timeout=35 --strict

# Override default config with custom nginx.conf while resolving env files.
envsubst '${APP_PORT}' < /config/nginx.conf > /etc/nginx/conf.d/default.conf

echo "Starting NGINX..."
nginx -g 'daemon off;'