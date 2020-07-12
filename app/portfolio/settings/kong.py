from .base import *

DEBUG = False

CORS_ORIGIN_ALLOW_ALL = False

CORS_ORIGIN_WHITELIST = [
    "http://sogloarcadius.fr",
    "https://sogloarcadius.fr",
    "http://api.sogloarcadius.fr",
    "https://api.sogloarcadius.fr",
]

CORS_ALLOW_HEADERS = [
    'accept',
    'accept-encoding',
    'authorization',
    'content-type',
    'dnt',
    'origin',
    'user-agent',
    'x-csrftoken',
    'x-requested-with',
    'cache-control',
    'accept-language',
]

CSRF_TRUSTED_ORIGINS = [
    '.sogloarcadius.fr',
]

ALLOWED_HOSTS = ["*"]

