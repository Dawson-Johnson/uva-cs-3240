"""
Django settings for mysite project.

Generated by 'django-admin startproject' using Django 4.2.18.

For more information on this file, see
https://docs.djangoproject.com/en/4.2/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/4.2/ref/settings/
"""
import os
from pathlib import Path

from django.contrib import admin
from django.urls import path, include
import dj_database_url  # helps to parse Heroku database url
from dotenv import load_dotenv

load_dotenv()

# Get the project base directory
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/4.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-b69fr(b7(7s@+m1c)#1tx6uokx=a)yecn-=jhk3m+leda@#&p4'
if os.getenv("SECRET_KEY"):
    SECRET_KEY = os.getenv("SECRET_KEY")
ACCOUNT_EMAIL_VERIFICATION = "none"
# SECURITY WARNING: don't run with debug turned on in production!
IS_HEROKU_APP = "DYNO" in os.environ and "CI" not in os.environ
# Redirect all non-HTTPS requests to HTTPS. This requires that:
# 1. Your app has a TLS/SSL certificate, which all `*.herokuapp.com` domains do by default.
#    When using a custom domain, you must configure one. See:
#    https://devcenter.heroku.com/articles/automated-certificate-management
# 2. Your app's WSGI web server is configured to use the `X-Forwarded-Proto` headers set by
#    the Heroku Router (otherwise you may encounter infinite HTTP 301 redirects). See this
#    app's `gunicorn.conf.py` for how this is done when using gunicorn.
#
# For maximum security, consider enabling HTTP Strict Transport Security (HSTS) headers too:
# https://docs.djangoproject.com/en/5.1/ref/middleware/#http-strict-transport-security
SECURE_SSL_REDIRECT = IS_HEROKU_APP
CSRF_COOKIE_SECURE = IS_HEROKU_APP
SESSION_COOKIE_SECURE = IS_HEROKU_APP
SECURE_HSTS_SECONDS = 3600 if IS_HEROKU_APP else 0
SECURE_HSTS_INCLUDE_SUBDOMAINS = IS_HEROKU_APP
SECURE_HSTS_PRELOAD = IS_HEROKU_APP
DEBUG = not IS_HEROKU_APP

if IS_HEROKU_APP:
    # On Heroku, it's safe to use a wildcard for `ALLOWED_HOSTS`, since the Heroku router performs
    # validation of the Host header in the incoming HTTP request. On other platforms you may need to
    # list the expected hostnames explicitly in production to prevent HTTP Host header attacks. See:
    # https://docs.djangoproject.com/en/5.1/ref/settings/#std-setting-ALLOWED_HOSTS
    ALLOWED_HOSTS = ["*"]
    SITE_ID = 37
else:
    ALLOWED_HOSTS = [".localhost", "127.0.0.1", "[::1]", "0.0.0.0", "[::]"]
    SITE_ID = 4

# Application definition

INSTALLED_APPS = [
    'home',
    'catalog',
    'collection',
    'libpanel',
    'bootstrap5',
    "whitenoise.runserver_nostatic",
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.sites',  # Required for django-allauth
    'allauth',
    'allauth.account',
    'allauth.socialaccount',
    'allauth.socialaccount.providers.google',
    'storages',
]

AUTHENTICATION_BACKENDS = [
    'django.contrib.auth.backends.ModelBackend',
    'allauth.account.auth_backends.AuthenticationBackend',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    "whitenoise.middleware.WhiteNoiseMiddleware",
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'allauth.account.middleware.AccountMiddleware'
]

# Google Login Stuff
LOGIN_URL = '/accounts/login/'
LOGIN_REDIRECT_URL = '/'
LOGOUT_REDIRECT_URL = '/'
SOCIALACCOUNT_PROVIDERS = {
    'google': {
        'SCOPE': ['email', 'profile'],
        'AUTH_PARAMS': {'access_type': 'online'}
    }
}

ROOT_URLCONF = 'mysite.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [BASE_DIR / "templates"],  # Ensure Django looks for custom templates
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.template.context_processors.media',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'mysite.wsgi.application'

# Database
# https://docs.djangoproject.com/en/4.2/ref/settings/#databases
if os.getenv('DATABASE_URL'):
    DATABASES = {
        'default': dj_database_url.parse(os.getenv('DATABASE_URL'))
    }
else:
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.sqlite3',
            'NAME': BASE_DIR / 'db.sqlite3',
        }
    }

# Password validation
# https://docs.djangoproject.com/en/4.2/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/4.2/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'America/New_York'

USE_I18N = True

USE_TZ = True

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.2/howto/static-files/

STATIC_URL = 'static/'
MEDIA_URL = 'media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')

# Default primary key field type
# https://docs.djangoproject.com/en/4.2/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

STATIC_ROOT = BASE_DIR / "staticfiles"

# Check if AWS credentials are available
if os.getenv("AWS_ACCESS_KEY_ID") and os.getenv("AWS_SECRET_ACCESS_KEY") and os.getenv("AWS_STORAGE_BUCKET_NAME"):
    # Use S3 storage if AWS credentials are provided
    AWS_ACCESS_KEY_ID = os.getenv("AWS_ACCESS_KEY_ID")
    AWS_SECRET_ACCESS_KEY = os.getenv("AWS_SECRET_ACCESS_KEY")
    DEFAULT_FILE_STORAGE = 'storages.backends.s3boto3.S3Boto3Storage'
    AWS_STORAGE_BUCKET_NAME = os.getenv("AWS_STORAGE_BUCKET_NAME")
    AWS_DEFAULT_ACL = None
    AWS_S3_CUSTOM_DOMAIN = f'{AWS_STORAGE_BUCKET_NAME}.s3.amazonaws.com'
    AWS_S3_FILE_OVERWRITE = False
    AWS_S3_REGION_NAME = 'us-east-2'
else:
    # Use local file storage if AWS credentials are not provided
    DEFAULT_FILE_STORAGE = 'django.core.files.storage.FileSystemStorage'
    # The media files will be stored in the MEDIA_ROOT directory
    # which is already defined above
