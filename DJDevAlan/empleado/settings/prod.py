"""
Configuración para Render (Producción)
"""
from pathlib import Path
import os
import dj_database_url
from .base import *  # Importa configuración base

BASE_DIR = Path(__file__).resolve().parent.parent.parent

# ======================
# SEGURIDAD
# ======================
DEBUG = False

ALLOWED_HOSTS = [
    '.onrender.com',
    'localhost',
    '127.0.0.1',
]

# ======================
# BASE DE DATOS
# ======================
# OPCIÓN 1: Usando DATABASE_URL de Render
DATABASE_URL = os.environ.get('DATABASE_URL')

if DATABASE_URL:
    DATABASES = {
        'default': dj_database_url.parse(
            DATABASE_URL, 
            conn_max_age=600,
            ssl_require=True
        )
    }
else:
    # OPCIÓN 2: Configuración manual de emergencia
    print("⚠️ ADVERTENCIA: DATABASE_URL no encontrada. Usando configuración manual.")
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.postgresql',
            'NAME': 'postgres',
            'USER': 'patito_db_user',
            'PASSWORD': '0088F0AACWKG9V1STXMec...',  # Tu contraseña
            'HOST': 'dkg.d5f8hvgglnc7l3h5d9g4',
            'PORT': '5432',
            'CONN_MAX_AGE': 600,
            'OPTIONS': {
                'sslmode': 'require',
            }
        }
    }

# ======================
# STATIC FILES
# ======================
STATIC_URL = '/static/'
STATIC_ROOT = BASE_DIR / 'staticfiles'
STATICFILES_DIRS = [
    BASE_DIR / 'empleado' / 'static',
]

# WhiteNoise para servir archivos estáticos
STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'

# Añade WhiteNoise al MIDDLEWARE
MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'whitenoise.middleware.WhiteNoiseMiddleware',  # ¡ESTO ES CLAVE!
    # ... resto de middlewares
]

# ======================
# MEDIA FILES
# ======================
MEDIA_URL = '/media/'
MEDIA_ROOT = BASE_DIR / 'media'

# ======================
# CONFIGURACIONES ADICIONALES
# ======================
SECURE_SSL_REDIRECT = True
SESSION_COOKIE_SECURE = True
CSRF_COOKIE_SECURE = True
SECURE_BROWSER_XSS_FILTER = True
SECURE_HSTS_SECONDS = 31536000
SECURE_HSTS_INCLUDE_SUBDOMAINS = True
SECURE_HSTS_PRELOAD = True

CSRF_TRUSTED_ORIGINS = [
    'https://*.onrender.com',
    'https://*.onrender.com',
]