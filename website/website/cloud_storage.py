
# custom_storages.py
#Utils to handle Amazon S3 Storage for Django app

from django.conf import settings
from storages.backends.s3boto import S3BotoStorage

class StaticStorage(S3BotoStorage):
    location = settings.STATICFILES_LOCATION
    
class MediaStorage(S3BotoStorage):
    location = settings.MEDIAFILES_LOCATION