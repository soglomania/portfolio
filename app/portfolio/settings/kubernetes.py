from .base import *

DEBUG = False

CORS_ORIGIN_ALLOW_ALL = False

CORS_ORIGIN_WHITELIST = [
    "http://sogloarcadius.com",
    "https://sogloarcadius.com",
    "https://api.sogloarcadius.com",
    "http://api.sogloarcadius.com",
    "http://sogloarcadius.fr",
    "https://sogloarcadius.fr",
    "https://api.sogloarcadius.fr",
    "http://api.sogloarcadius.fr",
]

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
]

ALLOWED_HOSTS = ['*']