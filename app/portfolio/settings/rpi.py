from .base import *

ALLOWED_HOSTS = ['*']

DEBUG = False

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
    '.sogloarcadius.rpi',
]



