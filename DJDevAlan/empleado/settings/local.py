from .base import *
from pathlib import Path
import dj_database_url


# SECURITY WARNING: don't run with debug turned on in production!
BASE_DIR=Path(__file__).resolve().parent.parent
DEBUG = False

ALLOWED_HOSTS = ['mi-sitio-web-de-render.onrender.com']

#Database
# https://docs.djangoproject.com/en/5.2/ref/settings/#databases

DATABASES = {
    'default': dj_database_url.config(
        default='sqlite:///db.sqlite3'
    )
}

STATIC_URL = '/static/'
STATIC_ROOT = BASE_DIR / 'staticfiles'

STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'

MEDIA_URL='/media/'
#MEDIA_ROOT=BASE_DIR.child('media')
MEDIA_ROOT=BASE_DIR / 'media'