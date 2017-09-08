from .base import *


# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ['*']


# DEBUG MODE

if DEBUG:  
    INTERNAL_IPS = ['127.0.0.1',]
    MIDDLEWARE+=['debug_toolbar.middleware.DebugToolbarMiddleware',]
    INSTALLED_APPS+=['debug_toolbar',]