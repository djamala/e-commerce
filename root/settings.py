#!/usr/bin/env python
# -*- coding: utf-8 -*-


import os
import sys
from django.utils.translation import ugettext_lazy as _



APP_TITLE = "TRACK-IT"
BASE_DIR = os.path.dirname(__file__)
#  BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
#  BASE_DIR_STATIC = os.path.dirname(__file__)
LOGS_DIR = os.path.join(BASE_DIR, 'logs/')
SECRET_KEY = 'x%to5*bkwy1v)ni^8hqrrjp22wmczq6c!=2)&+qlgvka9@=w=u'
#  DEBUG = False
DEBUG = True
#  DEBUG_PROPAGATE_EXCEPTIONS = True
ADMINS = [
    ('SUPPORT MKS SOFT TECHNOLOGIES', 'mks.dev.team@gmail.com'),
]

ALLOWED_HOSTS = [
    'localhost',
    #'192.168.114.176',
    #'51.254.217.155',
]
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    #'rest_framework',
    'session_security',
    #'ckeditor',
    #'api',
    #'oauth',
    'core',
    #'website',
    #'request',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.locale.LocaleMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'request.middleware.RequestMiddleware',
    'session_security.middleware.SessionSecurityMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'root.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [
            os.path.join(BASE_DIR, 'templates')
        ],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.template.context_processors.media',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
                #'root.context_processors.root.global_settings',
            ],
        },
    },
]

WSGI_APPLICATION = 'root.wsgi.application'
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite'),
        #'ENGINE': 'django.db.backends.postgresql_psycopg2',
        #'NAME': 's-restaurant',
        #'USER': 'django',
        #'PASSWORD': 'dj@ngo123$',
        #'HOST': 'localhost',
        #  'PORT': '29588',
        #'HOST': '192.168.109.141',
        #'PORT': '5432',
        #'TEST': {
        #    'NAME': 'test-trackit',
        #}
    }
}
if 'test' in sys.argv:
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.sqlite3',
            'NAME': os.path.join(BASE_DIR, 'trackit.sqlite'),
        }
    }


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


# Managin localization and i18n
DATE_INPUT_FORMATS = ['%d/%m/%Y']
LANGUAGE = (
    ('en', _('English')),
    ('fr', _('French')),
)
LANGUAGE_CODE = 'en'
TIME_ZONE = 'UTC'
USE_I18N = True
USE_L10N = False
USE_TZ = True
USE_THOUSAND_SEPARATOR = True
LOCALE_PATHS = [
    os.path.join(BASE_DIR, 'locale'),
]

STATIC_URL = '/static/'
STATICFILES_DIRS = [
    os.path.join(BASE_DIR, 'dev_static'),
]
STATIC_ROOT = os.path.join(BASE_DIR, 'static')

MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')
if 'test' in sys.argv:
    MEDIA_ROOT = os.path.join(BASE_DIR, 'tmedia')
BARCODE_ROOT = os.path.join(MEDIA_ROOT, 'barcodes')

#  SETTINGS_EXPORT = [
#      'APP_TITLE',
#  ]

# By default, for Default_Permission_Classes is :
# rest_framework.permissions.AllowAny
REST_FRAMEWORK = {
    'DEFAULT_RENDERER_CLASSES': (
        'rest_framework.renderers.JSONRenderer',
        'rest_framework.renderers.BrowsableAPIRenderer',
    ),
    #  'DEFAULT_AUTHENTICATION_CLASSES': (
    #      'rest_framework.authentication.BasicAuthentication',
    #      'rest_framework.authentication.SessionAuthentication',
    #  ),
    #  'DEFAULT_PERMISSION_CLASSES': (
    #      'rest_framework.permissions.IsAuthenticated',
    #  ),
}
# This is for avoid url terminated by slash
#  APPEND_SLASH = False

WEBSERVICES_CONFIG_FILE = os.path.join(BASE_DIR, 'webservices.cfg')
CONFIG_DIR = os.path.join(BASE_DIR, 'conf')
# MESSAGES_FILE = os.path.join(CONFIG_DIR, 'messages.yaml')
MESSAGES_FILE = 'messages.yaml'
FIXTURE_DIRS = os.path.join(BASE_DIR, 'fixtures')
FIXTURES_FILE = os.path.join(FIXTURE_DIRS, 'db.yaml')
TEST_RUNNER = 'django_nose.NoseTestSuiteRunner'
NOSE_ARGS = ['--with-spec', '--spec-color', '--nocapture', '--nologcapture']

# Email config
EMAIL_USE_TLS = True
EMAIL_SUBJECT_PREFIX = '[ TRACK-IT ] : '
DEFAULT_FROM_EMAIL = 'cervo_electronik@yahoo.fr'
SERVER_EMAIL = 'cervo_electronik@yahoo.fr'
EMAIL_HOST = 'smtp.mail.yahoo.fr'
EMAIL_PORT = 587
EMAIL_HOST_USER = 'cervo_electronik@yahoo.fr'
EMAIL_HOST_PASSWORD = 'Alima9891$'
EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'

#  Tawkto settings (chatbox)
#  TAWKTO_ID_SITE = '5b97cac4c666d426648aa8ba'
#  TAWKTO_API_KEY = 'eed7042d85df3fb69a7773ecc72f35747898c3a8'
#  TAWKTO_IS_SECURE = True

# Sessions
SESSION_SERIALIZER = 'django.contrib.sessions.serializers.JSONSerializer'
SESSION_SAVE_EVERY_REQUEST = True
SESSION_EXPIRE_AT_BROWSER_CLOSE = True
# SESSION_COOKIE_AGE = 100
SESSION_SECURITY_WARN_AFTER = 840
SESSION_SECURITY_EXPIRE_AFTER = 900
#SESSION_SECURITY_WARN_AFTER = 60
#SESSION_SECURITY_EXPIRE_AFTER = 120
SESSION_SECURITY_INSECURE = False
# List of url names middleware should ignore
#  SESSION_SECURITY_PASSIVE_URLS =
#  SESSION_SECURITY_PASSIVE_URLS_NAMES =

# Logging (Fr. Journalisation des évènements)
""" LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'formatters': {
        'verbose': {
            'format': '[ %(levelname)s ][ %(asctime)s ][ %(module)s ][ %(process)d ][ %(thread)d ] ==> %(message)s'
        },
        'simple': {
            'format': '[ %(levelname)s ][ %(asctime)s ][ %(module)s ] ==> %(message)s'
        },
    },
    'handlers': {
        'default': {
            'level': 'INFO',
            'class': 'logging.handlers.TimedRotatingFileHandler',
            'when': 'midnight',
            'interval': 1,
            'filename': os.path.join(LOGS_DIR, 'default.log'),
            'formatter': 'verbose',
        },
        'server': {
            'level': 'INFO',
            'class': 'logging.handlers.TimedRotatingFileHandler',
            'when': 'midnight',
            'interval': 1,
            'filename': os.path.join(LOGS_DIR, 'server.log'),
            'formatter': 'verbose',
        },
        'request': {
            'level': 'DEBUG',
            'class': 'logging.handlers.TimedRotatingFileHandler',
            'when': 'midnight',
            'interval': 1,
            'filename': os.path.join(LOGS_DIR, 'request.log'),
            'formatter': 'verbose',
        },
        'db': {
            'level': 'DEBUG',
            'class': 'logging.handlers.TimedRotatingFileHandler',
            'when': 'midnight',
            'interval': 1,
            'filename': os.path.join(LOGS_DIR, 'db.log'),
            'formatter': 'simple',
        },
        'payment': {
            'level': 'DEBUG',
            'class': 'logging.handlers.TimedRotatingFileHandler',
            'when': 'midnight',
            'interval': 1,
            'filename': os.path.join(LOGS_DIR, 'payments.log'),
            'formatter': 'simple',
        },
        'template': {
            'level': 'DEBUG',
            'class': 'logging.handlers.TimedRotatingFileHandler',
            'when': 'midnight',
            'interval': 1,
            'filename': os.path.join(LOGS_DIR, 'template.log'),
            'formatter': 'simple',
        },
        'access': {
            'level': 'DEBUG',
            'class': 'logging.handlers.TimedRotatingFileHandler',
            'when': 'midnight',
            'interval': 1,
            'filename': os.path.join(LOGS_DIR, 'access.log'),
            'formatter': 'simple',
        },
        'debug': {
            'level': 'DEBUG',
            'class': 'logging.handlers.TimedRotatingFileHandler',
            'when': 'midnight',
            'interval': 1,
            'filename': os.path.join(LOGS_DIR, 'debug.log'),
            'formatter': 'verbose',
        },
        'mail_admins': {
            'level': 'ERROR',
            'class': 'django.utils.log.AdminEmailHandler',
            'formatter': 'verbose',
        }
    },
    'loggers': {
        'django': {
            'handlers': ['default'],
            'level': 'INFO',
            'propagate': True,
        },
        'django.request': {
            'handlers': ['mail_admins'],
            'level': 'ERROR',
            'propagate': True,
        },
        'django.server': {
            'handlers': ['server'],
            'level': 'DEBUG',
            'propagate': True,
        },
        'django.template': {
            'handlers': ['template'],
            'level': 'DEBUG',
            'propagate': True,
        },
        'django.db.backends': {
            'handlers': ['db'],
            'level': 'DEBUG',
            'propagate': True,
        },
        'default': {
            'handlers': ['default'],
            'level': 'DEBUG',
            'propagate': True,
        },
        'accesslog': {
            'handlers': ['access'],
            'level': 'DEBUG',
            'propagate': True,
        },
        'debug': {
            'handlers': ['debug'],
            'level': 'DEBUG',
            'propagate': True,
        },
        'payment': {
            'handlers': ['payment'],
            'level': 'DEBUG',
            'propagate': True,
        },
    },
}
 
 """
# Interface Configs
PAGE_NOT_FOUND = '404.html'
FORBIDDEN_ACCESS = '403.html'
INTERNAL_SERVER_ERROR = '500.html'


















