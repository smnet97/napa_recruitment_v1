"""
Django settings for napa_recruitment project.

Generated by 'django-admin startproject' using Django 3.1.6.

For more information on this file, see

For the full list of settings and their values, see
"""

from pathlib import Path
import environ
from django.contrib import messages
import os

env = environ.Env(
    DEBUG=(bool, False)
)

environ.Env.read_env()

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent

# Quick-start development settings - unsuitable for production

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = env('SECRET_KEY')

# SECURITY WARNING: don't run with debug turned on in production!

SITE_DOMAIN = env('SITE_DOMAIN', default='localhost:8080')
DEBUG = env('DEBUG', cast=bool)
ALLOWED_HOSTS = env('ALLOWED_HOSTS', cast=list)

# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'main',
    'user',
    'student',
    'crispy_forms',
    'debug_toolbar',
    'django_select2',

]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'django.middleware.locale.LocaleMiddleware',
    'debug_toolbar.middleware.DebugToolbarMiddleware',
]

ROOT_URLCONF = 'napa_recruitment.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [
            BASE_DIR / 'napa_recruitment' / 'templates',
            os.path.join(BASE_DIR, 'templates'),
        ],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
                'django.template.context_processors.media',
                'django_settings_export.settings_export',
                'napa_recruitment.globals.title',
            ],
        },
    },
]

WSGI_APPLICATION = 'napa_recruitment.wsgi.application'

# Database

DATABASES = {
    'default': env.db()
}

# Password validation

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

LANGUAGE_CODE = 'ru'


TIME_ZONE = 'Asia/Tashkent'

USE_I18N = True

USE_L10N = True

USE_TZ = False

# Static files (CSS, JavaScript, Images)

STATIC_URL = '/static/'

STATIC_ROOT = BASE_DIR / 'static'

# STATICFILES_DIRS = [BASE_DIR, "static"]

MEDIA_URL = '/media/'
MEDIA_ROOT = BASE_DIR / 'media'

AUTH_USER_MODEL = 'user.User'

CRISPY_TEMPLATE_PACK = 'bootstrap4'

SETTINGS_EXPORT = [
    'LANGUAGES'
]

LANGUAGES = [
    ('ru', "ru"),
    ('uz', "uz")
]

INTERNAL_IPS = [
    '127.0.0.1',
]

MESSAGE_TAGS = {
    messages.INFO: 'alert alert-info',
    messages.SUCCESS: 'alert alert-success',
}


SMS_USERNAME = env('SMS_USERNAME')
SMS_PASSWORD = env('SMS_PASSWORD')

