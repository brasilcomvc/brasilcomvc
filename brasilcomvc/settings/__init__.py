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
BASE_URL = os.environ.get('BASE_URL', '')
DATABASES = {'default': dj_database_url.config(default='sqlite:///dev.sqlite')}
DEBUG = os.environ.get('DEBUG', 'false').lower() == 'true'
DEFAULT_FROM_EMAIL = os.environ['DEFAULT_FROM_EMAIL']
EMAIL_HOST = os.environ['EMAIL_HOST']
EMAIL_HOST_PASSWORD = os.environ.get('EMAIL_HOST_PASSWORD')
EMAIL_HOST_USER = os.environ.get('EMAIL_HOST_USER')
EMAIL_PORT = os.environ.get('EMAIL_PORT', 25)
GOOGLE_API_KEY = os.environ.get('GOOGLE_API_KEY', '')
MAILING_ADDRESS = os.environ.get('MAILING_ADDRESS', '')
SECRET_KEY = os.environ['SECRET_KEY']
SNS_FACEBOOK = os.environ.get('SNS_FACEBOOK', '')
SNS_GOOGLEPLUS = os.environ.get('SNS_GOOGLEPLUS', '')
SNS_TWITTER = os.environ.get('SNS_TWITTER', '')


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
    'cities_light',
    'raven.contrib.django.raven_compat',
    'social.apps.django_app.default',
    'storages',
)

LOCAL_APPS = (
    'brasilcomvc.common',
    'brasilcomvc.accounts',
    'brasilcomvc.feedback',
    'brasilcomvc.guideline',
    'brasilcomvc.projects',
    'brasilcomvc.portal',
)

INSTALLED_APPS = DJANGO_APPS + THIRD_PARTY_APPS + LOCAL_APPS

MIDDLEWARE_CLASSES = global_settings.MIDDLEWARE_CLASSES + (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
)

TEMPLATE_CONTEXT_PROCESSORS = global_settings.TEMPLATE_CONTEXT_PROCESSORS + (
    'django.core.context_processors.request',
    'social.apps.django_app.context_processors.backends',
    'social.apps.django_app.context_processors.login_redirect',
    'brasilcomvc.common.context_processors.api_keys',
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
LOGIN_URL = reverse_lazy('accounts:login')
LOGIN_REDIRECT_URL = reverse_lazy('accounts:edit_dashboard')

AUTHENTICATION_BACKENDS = (
    'social.backends.facebook.FacebookOAuth2',
    'django.contrib.auth.backends.ModelBackend',
)

# python-social-auth
SOCIAL_AUTH_PIPELINE = (
    'social.pipeline.social_auth.social_details',
    'social.pipeline.social_auth.social_uid',
    'social.pipeline.social_auth.auth_allowed',
    'social.pipeline.social_auth.social_user',
    'social.pipeline.user.get_username',
    'social.pipeline.social_auth.associate_by_email',
    'social.pipeline.user.create_user',
    'social.pipeline.social_auth.associate_user',
    'social.pipeline.social_auth.load_extra_data',
    'brasilcomvc.accounts.pipelines.set_user_info_from_auth_provider',
)
SOCIAL_AUTH_SLUGIFY_USERNAMES = True
SOCIAL_AUTH_FACEBOOK_KEY = os.environ['FACEBOOK_APP_KEY']
SOCIAL_AUTH_FACEBOOK_SECRET = os.environ['FACEBOOK_APP_SECRET']
SOCIAL_AUTH_FACEBOOK_SCOPE = ['public_profile', 'email']
SOCIAL_AUTH_FACEBOOK_PROFILE_EXTRA_PARAMS = {'locale': 'pt_BR'}
