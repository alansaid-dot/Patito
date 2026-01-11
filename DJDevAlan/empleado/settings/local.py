import os
from .base import *
import dj_database_url

DEBUG = False
ALLOWED_HOSTS = ['.onrender.com']

# DATABASE - Para Render
DATABASE_URL = os.environ.get('DATABASE_URL')
if DATABASE_URL:
    DATABASES = {
        'default': dj_database_url.parse(DATABASE_URL, conn_max_age=600, ssl_require=True)
    }
else:
    # Solo falla durante el build, no durante runtime
    import sys
    if 'collectstatic' not in ' '.join(sys.argv) and 'migrate' not in ' '.join(sys.argv):
        DATABASES = {
            'default': {
                'ENGINE': 'django.db.backends.dummy',
            }
        }


STATIC_URL = '/static/'
STATIC_ROOT = BASE_DIR / 'staticfiles'

STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'

MEDIA_URL='/media/'
#MEDIA_ROOT=BASE_DIR.child('media')
MEDIA_ROOT=BASE_DIR / 'media'