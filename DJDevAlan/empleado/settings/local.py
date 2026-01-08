from .base import *
from pathlib import Path

# SECURITY WARNING: don't run with debug turned on in production!
BASE_DIR=Path(__file__).resolve().parent.parent
DEBUG = True

ALLOWED_HOSTS = []

#Database
# https://docs.djangoproject.com/en/5.2/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}

STATIC_URL = '/static/'
STATICFILES_DIRS=[BASE_DIR.parent / 'static']

MEDIA_URL='/media/'
#MEDIA_ROOT=BASE_DIR.child('media')
MEDIA_ROOT=BASE_DIR / 'media'