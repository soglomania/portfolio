from .base import *
from corsheaders.defaults import default_headers

DEBUG = False

CORS_ALLOW_HEADERS = default_headers + (
    'Cache-Control',
    'Referer',
    'Accept-Language'
)

CORS_ORIGIN_ALLOW_ALL = False

CORS_ORIGIN_WHITELIST = (
    "http://sogloarcadius.com",
    "https://sogloarcadius.com",
    "http://api.sogloarcadius.com",
    "https://api.sogloarcadius.com"
)

CSRF_TRUSTED_ORIGINS = (
    "sogloarcadius.com",
    "api.sogloarcadius.com",
)

ALLOWED_HOSTS = ['*']