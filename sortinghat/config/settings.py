#
# SortingHat basic settings file.
#
# This file defines the required settings to run SortingHat.
# Due to SortingHat is a Django based app, this settings are
# based on the configuration file generated by Django by
# default.
#
# Please check the next links for details about the configuration
# in a production environment:
#
# https://docs.djangoproject.com/en/3.1/howto/deployment/checklist/
# https://docs.djangoproject.com/en/3.1/ref/settings/
#

import os


BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

SILENCED_SYSTEM_CHECKS = [
    'django_mysql.E016'
]

#
# General app parameters
#

#
# You must never enable debug in production.
#
# https://docs.djangoproject.com/en/3.1/ref/settings/#std:setting-DEBUG
#

DEBUG = os.environ.get('SORTINGHAT_DEBUG', 'False').lower() in ('true', '1')

#
# ALLOWED_HOST protects the site against CSRF attacks.
# If DEBUG is set to False, you will need to configure this parameter,
# with the host you are using to serve SortingHat.
#
# https://docs.djangoproject.com/en/3.1/ref/settings/#allowed-hosts
#

if 'SORTINGHAT_ALLOWED_HOST' in os.environ:
    ALLOWED_HOSTS = os.environ['SORTINGHAT_ALLOWED_HOST'].split(',')
else:
    ALLOWED_HOSTS = [
        '127.0.0.1',
        'localhost',
    ]

#
# The secret key must be a large random value and it must be kept secret.
#
# https://docs.djangoproject.com/en/3.1/ref/settings/#secret-key
#

SECRET_KEY = os.environ['SORTINGHAT_SECRET_KEY']

#
# Application definition - DO NOT MODIFY
#

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'corsheaders',
    'django_rq',
    'graphene_django',
    'sortinghat.core',
]

ROOT_URLCONF = 'sortinghat.app.urls'

WSGI_APPLICATION = 'sortinghat.app.wsgi.application'

MIDDLEWARE = [
    'corsheaders.middleware.CorsMiddleware',
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

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

#
# Graphene - DO NOT MODIFY
#

GRAPHENE = {
    'SCHEMA': 'sortinghat.core.schema',
    'MIDDLEWARE': [
        'graphql_jwt.middleware.JSONWebTokenMiddleware',
    ],
}


#
# Authentication - DO NOT MODIFY
#

AUTHENTICATION_BACKENDS = [
    'django.contrib.auth.backends.ModelBackend',
    'graphql_jwt.backends.JSONWebTokenBackend',
]

#
# Password validation
#
# https://docs.djangoproject.com/en/3.1/ref/settings/#auth-password-validators
#

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

#
# Cross-Origin Resource Sharing (CORS)
#
# You'll HAVE TO configure the origins that are authorized to make
# cross-site HTTP requests. Check the following link to understand
# the possibilities and parameters you can use.
#
# https://github.com/adamchainz/django-cors-headers#configuration
#

if 'SORTINGHAT_CORS_ALLOWED_ORIGINS' in os.environ:
    CORS_ALLOWED_ORIGINS = os.environ['SORTINGHAT_CORS_ALLOWED_ORIGINS'].split(',')
else:
    CORS_ALLOWED_ORIGINS = [
        'http://localhost:8080',
    ]

CORS_ALLOW_CREDENTIALS = True

#
# Static files (CSS, JavaScript, Images)
#
# https://docs.djangoproject.com/en/3.2/howto/static-files/
#

STATIC_URL = '/'

# UI static files will be copied to the next path when
# 'collectstatic' is run.
# If you are serving these files in a dedicated server, you will
# need to copy them to their final destination.

STATIC_ROOT = os.path.join(BASE_DIR, 'static')

# MEDIA_URL is only needed when DEBUG is set to True.
# Modify this URL if you want to run the server in developer mode.

MEDIA_URL = 'http://media.localhost/'

#
# Internationalization
#
# https://docs.djangoproject.com/en/3.1/topics/i18n/
#
#

LANGUAGE_CODE = 'en-us'
USE_I18N = True
USE_L10N = True

#
# Time Zone
#

USE_TZ = True
TIME_ZONE = 'UTC'

#
# SortingHat Logging
#
# https://docs.djangoproject.com/en/3.1/topics/logging/#configuring-logging
#

LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'formatters': {
        'simple': {
            'format': '[{asctime}] {message}',
            'style': '{',
        },
        'verbose': {
            'format': '[{asctime} - {levelname} - {name}:{lineno}] {message}',
            'style': '{',
        },
    },
    'handlers': {
        'console': {
            'class': 'logging.StreamHandler',
            'formatter': 'verbose',
        },
    },
    'root': {
        'handlers': ['console'],
        'level': 'INFO',
    },
}

#
# SortingHat database
#
# You MUST set the database parameters in order to run
# SortingHat.
#

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'HOST': os.environ.get('SORTINGHAT_DB_HOST', '127.0.0.1'),
        'PORT': os.environ.get('SORTINGHAT_DB_PORT', 3306),
        'USER': os.environ.get('SORTINGHAT_DB_USER', 'root'),
        'PASSWORD': os.environ.get('SORTINGHAT_DB_PASSWORD', ''),
        'NAME': os.environ.get('SORTINGHAT_DB_DATABASE', 'sortinghat_test'),
        'OPTIONS': {'charset': 'utf8mb4'},
    }
}

#
# SortingHat workers
#
# SortingHat uses RQ to run background and async jobs.
# You'll HAVE TO set the next parameters in order to run
# them in the background. If not, set ASYNC to 'False'.
#
# Take into account RQ uses Redis database. You have more
# info about these parameters on the following link:
#
# https://github.com/rq/django-rq
#

RQ_QUEUES = {
    'default': {
        'HOST': os.environ.get('SORTINGHAT_REDIS_HOST', '127.0.0.1'),
        'PORT': os.environ.get('SORTINGHAT_REDIS_PORT', 6379),
        'PASSWORD': os.environ.get('SORTINGHAT_REDIS_PASSWORD', ''),
        'ASYNC': os.environ.get('SORTINGHAT_WORKERS_ASYNC', True),
        'DB': os.environ.get('SORTINGHAT_REDIS_DB', 0),
    }
}

#
# SortingHat Core parameters
#

# Require authentication when using the API.
# You shouldn't deactivate this option unless you are debugging
# the system or running it in a trusted and safe environment.

SORTINGHAT_AUTHENTICATION_REQUIRED = True

#
# API default page size
#

SORTINGHAT_API_PAGE_SIZE = 10

#
# genderize.io token, used only for gender recommendations
#

SORTINGHAT_GENDERIZE_API_KEY = os.environ.get('SORTINGHAT_GENDERIZE_API_KEY', None)