"""
Django settings for baker_street project.

For more information on this file, see
https://docs.djangoproject.com/en/1.7/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.7/ref/settings/
"""

import os

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(__file__))

BROKER_URL = 'django://'
# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.7/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'mv&ziq89ix8y2cqty*rx8qqwqhtaq1vcx#rovyj)u4r7q_za*d'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

TEMPLATE_DEBUG = True


# Application definition

INSTALLED_APPS = (
    'corsheaders',
    'suit',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'rest_framework',
    'rest_framework.authtoken',
    'django_extensions',
    'compressor',
    'baker_street',
    'djcelery',
    'kombu.transport.django',
)

MIDDLEWARE_CLASSES = (
    'corsheaders.middleware.CorsMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.auth.middleware.SessionAuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
)

ROOT_URLCONF = 'baker_street.urls'
CELERY_ALWAYS_EAGER = True

WSGI_APPLICATION = 'baker_street.wsgi.application'


# Database
# https://docs.djangoproject.com/en/1.7/ref/settings/#databases

# Parse database configuration from $DATABASE_URL
if 'DATABASE_URL' not in os.environ:
    raise Exception("""
    You must add a DATABASE_URL environment variable.
    e.g.
        export DATABASE_URL="postgres://localhost/[YOUR_DATABASE_NAME]"
    """)

import dj_database_url
DATABASES = {
    'default': dj_database_url.config()
}

# Internationalization
# https://docs.djangoproject.com/en/1.7/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'America/Toronto'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.7/howto/static-files/
# https://devcenter.heroku.com/articles/django-assets

# Static asset configuration
STATIC_ROOT = 'staticfiles'  # i.e. baker-street/staticfiles/
STATIC_URL = '/static/'


# Simplified static file serving.
# https://warehouse.python.org/project/whitenoise/

STATICFILES_STORAGE = 'whitenoise.django.GzipManifestStaticFilesStorage'


STATICFILES_FINDERS = (
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
    'compressor.finders.CompressorFinder',
)

# http://django-compressor.readthedocs.org/en/latest/settings/#django.conf.settings.COMPRESS_PRECOMPILERS
# COMPRESS_PRECOMPILERS = (
#     ('text/x-scss', '/usr/bin/env bundle exec sass --scss --sourcemap=none {infile} {outfile}'),
# )

# Templates
# https://docs.djangoproject.com/en/1.7/ref/settings/#template-dirs

# TEMPLATE_DIRS = (
#     os.path.join(BASE_DIR, 'templates'),
# )

# Suit
# http://django-suit.readthedocs.org/en/develop/
from django.conf.global_settings import TEMPLATE_CONTEXT_PROCESSORS as TCP
TEMPLATE_CONTEXT_PROCESSORS = TCP + (
    'django.core.context_processors.request',
)


# Heroku configuration
# https://devcenter.heroku.com/articles/getting-started-with-django

# Honor the 'X-Forwarded-Proto' header for request.is_secure()
SECURE_PROXY_SSL_HEADER = ('HTTP_X_FORWARDED_PROTO', 'https')

# Allow all host headers
ALLOWED_HOSTS = ['*']


# Django Suit configuration
# http://django-suit.readthedocs.org/en/develop/configuration.html
SUIT_CONFIG = {
    # header
    'ADMIN_NAME': 'Baker Street',
}


# Django REST Framework
# http://www.django-rest-framework.org/api-guide/settings

REST_FRAMEWORK = {
    'DEFAULT_AUTHENTICATION_CLASSES': (
        'rest_framework.authentication.SessionAuthentication',
        'rest_framework.authentication.TokenAuthentication',
    ),
    'DEFAULT_RENDERER_CLASSES': (
        'rest_framework.renderers.JSONRenderer',
        'rest_framework.renderers.BrowsableAPIRenderer',
    ),
    'PAGINATE_BY': 10,
}


# Custom user model
AUTH_USER_MODEL = 'baker_street.User'

# Allow requests from any origin
CORS_ORIGIN_ALLOW_ALL = True
