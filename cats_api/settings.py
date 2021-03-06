import logging
import os
from os import environ as env
from pathlib import Path
from prettyconf import config

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/4.0/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-io5suwnlq_ye%q^_&w(ur==yj=d#$4jab@((sbz46^92-mbh(y'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ['cats-api', 'localhost']


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'cats',
    'django_filters',
    'rest_framework',
    'drf_yasg2',
    'django_prometheus',
]

MIDDLEWARE = [
    'django_prometheus.middleware.PrometheusBeforeMiddleware',
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'request_logging.middleware.LoggingMiddleware',
    'whitenoise.middleware.WhiteNoiseMiddleware',
    'django_prometheus.middleware.PrometheusAfterMiddleware',
]

# Logging
REQUEST_LOGGING_HTTP_4XX_LOG_LEVEL = logging.WARNING
REQUEST_LOGGING_ENABLE_COLORIZE = config("LOG_COLORIZE", default=False, cast=config.boolean)
LOG_LEVEL = config("LOG_LEVEL", default="INFO")
LOG_FORMAT = config("LOG_FORMAT", default="logger")
LOGGING = {
    "version": 1,
    "disable_existing_loggers": False,
    "formatters": {
        "json": {
            "()": "pythonjsonlogger.jsonlogger.JsonFormatter",
            "format": "%(levelname)s %(name)s %(module)s %(message)s %(asctime)s",
        },
        "simple": {
            "format": "[{levelname}] name:{name} module:{module} message:{message}",
            "style": "{",
        },
    },
    "handlers": {
        "console": {"level": "INFO", "class": "logging.StreamHandler", "formatter": "simple"},
        "console_json": {"level": "INFO", "class": "logging.StreamHandler", "formatter": "json"},
        'logger': {'level': 'INFO', 'class': 'logging.handlers.RotatingFileHandler', 'filename': './logs/test.log', 'formatter': 'simple'},
    },
    "root": {
        "handlers": [LOG_FORMAT],
        "level": LOG_LEVEL,
    },
    "loggers": {
        "django": {
            "handlers": [LOG_FORMAT],
            "level": LOG_LEVEL,
            "propagate": False,
        },
    },
}


ROOT_URLCONF = 'cats_api.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'cats_api.wsgi.application'


# Database
# https://docs.djangoproject.com/en/4.0/ref/settings/#databases

DB_HOST = env.get('DB_HOST', 'localhost')

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'cats_api',
        'USER': 'postgres',
        'PASSWORD': 'admin',
        'HOST': DB_HOST,
    }
}


# Password validation
# https://docs.djangoproject.com/en/4.0/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]


# Internationalization
# https://docs.djangoproject.com/en/4.0/topics/i18n/

LANGUAGE_CODE = 'pt-br'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
STATIC_URL = '/static/'
MEDIA_URL = '/media/'
STATIC_ROOT = os.path.join(BASE_DIR, 'static')
STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'

# Default primary key field type
# https://docs.djangoproject.com/en/4.0/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'
