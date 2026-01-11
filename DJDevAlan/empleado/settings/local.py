from .base import *
from pathlib import Path
import dj_database_url


# SECURITY WARNING: don't run with debug turned on in production!
BASE_DIR=Path(__file__).resolve().parent.parent
DEBUG = False

ALLOWED_HOSTS = ['mi-sitio-web-de-render.onrender.com']

#Database
# https://docs.djangoproject.com/en/5.2/ref/settings/#databases

database_url = os.environ.get('DATABASE_URL')

if not database_url:
    raise ValueError("DATABASE_URL no está configurada")

DATABASES = {
    'default': dj_database_url.parse(database_url, conn_max_age=600, ssl_require=True)
}


STATIC_URL = '/static/'
STATIC_ROOT = BASE_DIR / 'staticfiles'

STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'

MEDIA_URL='/media/'
#MEDIA_ROOT=BASE_DIR.child('media')
MEDIA_ROOT=BASE_DIR / 'media'