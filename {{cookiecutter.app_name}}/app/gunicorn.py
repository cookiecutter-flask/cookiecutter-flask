import os

LOGS_DIR = '/data/logs'

if not os.path.exists(LOGS_DIR):
    os.makedirs(LOGS_DIR)

bind = '0.0.0.0:{}'.format(os.environ.get('APP_PORT', 5000))
workers = 4
reload = True
umask = 0o007
accesslog = os.path.join(LOGS_DIR, 'gunicorn_access.log')
errorlog = os.path.join(LOGS_DIR, 'gunicorn_error.log')
loglevel = 'info'
forwarded_allow_ips = 'nginx'
