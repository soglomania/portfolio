from .base import *

ALLOWED_HOSTS = ['*']

CORS_ORIGIN_ALLOW_ALL = True

CORS_ALLOW_HEADERS = [
    'accept',
    'accept-encoding',
    'accept-language',
    'authorization',
    'content-type',
    'dnt',
    'origin',
    'user-agent',
    'x-csrftoken',
    'x-requested-with',
    'cache-control',
]

CSRF_TRUSTED_ORIGINS = [
    '.sogloarcadius.com',
    '.sogloarcadius.fr',
    'localhost.com',
    'localhost.fr',
    'localhost',
]

CONSOLE_LOGS = True
if CONSOLE_LOGS:
    LOGGING['loggers']['']['handlers'] += ['console']


DEBUG = True
if DEBUG:  
    INTERNAL_IPS = ['127.0.0.1',]
    MIDDLEWARE+=['debug_toolbar.middleware.DebugToolbarMiddleware',]
    INSTALLED_APPS+=['debug_toolbar',]
    #settings_logger.critical('starting server in debug mode')
    #settings_logger.info('allowed_hosts: {}'.format(str(ALLOWED_HOSTS)))