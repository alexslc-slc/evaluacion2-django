"""
Django settings for registro_empleados project.
"""

import os
from pathlib import Path
import dj_database_url

BASE_DIR = Path(__file__).resolve().parent.parent

SECRET_KEY = os.environ.get('DJANGO_SECRET_KEY', 'django-insecure-z1@c+o^9ogkuun2v)o0re2qb_k*sa4@j3z=k9#379+a5jc$j&_')

DEBUG = os.environ.get('DEBUG', 'True') == 'True'

ALLOWED_HOSTS = ['*']

INSTALLED_APPS = [
    'unfold',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'empleados_app',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'whitenoise.middleware.WhiteNoiseMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'registro_empleados.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [BASE_DIR / 'templates'],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'registro_empleados.wsgi.application'

# Base de datos MySQL para Railway - CORREGIDO
if os.environ.get('MYSQL_URL'):
    # Usar MYSQL_URL que ya tienes en Railway
    DATABASES = {
        'default': dj_database_url.config(
            default=os.environ.get('MYSQL_URL'),
            conn_max_age=600,
            conn_health_checks=True,
        )
    }
else:
    # Fallback usando las variables individuales (CORREGIDO)
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.mysql',
            'NAME': os.environ.get('MYSQL_DATABASE', os.environ.get('MYSQLDATABASE', 'railway')),
            'USER': os.environ.get('MYSQL_USER', os.environ.get('MYSQLUSER', 'root')),
            'PASSWORD': os.environ.get('MYSQL_PASSWORD', os.environ.get('MYSQLPASSWORD', '')),
            'HOST': os.environ.get('MYSQL_HOST', os.environ.get('MYSQLHOST', 'localhost')),
            'PORT': os.environ.get('MYSQL_PORT', os.environ.get('MYSQLPORT', '3306')),
            'OPTIONS': {
                'init_command': "SET sql_mode='STRICT_TRANS_TABLES'",
                'charset': 'utf8mb4',
            }
        }
    }

AUTH_PASSWORD_VALIDATORS = [
    {'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator'},
    {'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator'},
    {'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator'},
    {'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator'},
]

UNFOLD = {
    "SITE_TITLE": "Panel de Administración",
    "SITE_HEADER": "Registro de Empleados",
    "SITE_SUBHEADER": "Sistema interno",
    "SITE_SYMBOL": "people",
}

LANGUAGE_CODE = 'es'
TIME_ZONE = 'America/Lima'
USE_I18N = True
USE_TZ = True

# Archivos estáticos
STATIC_URL = 'static/'
STATICFILES_DIRS = [BASE_DIR / "static"]
STATIC_ROOT = BASE_DIR / "staticfiles"
STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'

# Archivos multimedia
MEDIA_URL = 'media/'
MEDIA_ROOT = BASE_DIR / 'media'

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

# Configuración CSRF para Railway
CSRF_TRUSTED_ORIGINS = [
    'https://evaluacion2-django-production.up.railway.app',
    'http://evaluacion2-django-production.up.railway.app',
    'https://*.up.railway.app',
    'http://*.up.railway.app',
]
