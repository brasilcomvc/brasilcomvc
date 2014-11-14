# coding: utf-8
'''
Main project settings

ATTENTION: DON'T SET ENVIRONMENT-SPECIFIC VALUES IN THIS MODULE. Instead, set
them into your .env file as it will be used by Foreman for local deployment.
'''

import os

from django.core.urlresolvers import reverse_lazy
from django.conf import global_settings

import dj_database_url

from .staticfiles import *


# Env-specific

ALLOWED_HOSTS = os.environ.get('ALLOWED_HOSTS', '*').split(',')
DATABASES = {'default': dj_database_url.config(default='sqlite:///dev.sqlite')}
DEBUG = os.environ.get('DEBUG', 'false').lower() == 'true'
SECRET_KEY = os.environ['SECRET_KEY']


# Application definition

DJANGO_APPS = (
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.humanize',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
)

THIRD_PARTY_APPS = (
    'pipeline',
)

LOCAL_APPS = (
    'brasilcomvc.common',
    'brasilcomvc.accounts',
)

INSTALLED_APPS = DJANGO_APPS + THIRD_PARTY_APPS + LOCAL_APPS

MIDDLEWARE_CLASSES = global_settings.MIDDLEWARE_CLASSES + (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
)

TEMPLATE_CONTEXT_PROCESSORS = global_settings.TEMPLATE_CONTEXT_PROCESSORS + (
    'django.core.context_processors.request',
)

TEMPLATE_DEBUG = DEBUG

ROOT_URLCONF = 'brasilcomvc.urls'

WSGI_APPLICATION = 'brasilcomvc.wsgi.application'


# Internationalization

LANGUAGE_CODE = 'pt-br'
TIME_ZONE = 'America/Sao_Paulo'
USE_I18N = True
USE_L10N = True
USE_TZ = True


# Misc

SITE_ID = 1


# Authentication
AUTH_USER_MODEL = 'accounts.User'
LOGIN_URL = reverse_lazy('login')
LOGIN_REDIRECT_URL = reverse_lazy('profile')
