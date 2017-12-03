from .base import *


# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True
ALLOWED_HOSTS = ['*']

CONSOLE_LOGS = True

if CONSOLE_LOGS:
    # Log all to the console as well. This is used while running unit tests
    LOGGING['loggers']['']['handlers'] += ['console']

# DEBUG MODE

if DEBUG:  
    INTERNAL_IPS = ['127.0.0.1',]
    MIDDLEWARE+=['debug_toolbar.middleware.DebugToolbarMiddleware',]
    INSTALLED_APPS+=['debug_toolbar',]
    settings_logger.critical('starting server in debug mode')
    settings_logger.info('allowed_hosts: {}'.format(str(ALLOWED_HOSTS)))