from .base import *


# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

#TODO: put domain name Ex : ".sogloarcadius.xyz"
ALLOWED_HOSTS = ['.sogloarcadius.xyz', 'app']



if DEBUG:  
    MIDDLEWARE+=['debug_toolbar.middleware.DebugToolbarMiddleware',]
    INSTALLED_APPS+=['debug_toolbar',]
    settings_logger.critical('starting server in debug mode')
    settings_logger.info('allowed_hosts: {}'.format(str(ALLOWED_HOSTS)))