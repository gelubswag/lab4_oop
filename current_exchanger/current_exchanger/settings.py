"""
Django settings for current_exchanger project.

Generated by 'django-admin startproject' using Django 5.1.3.

For more information on this file, see
https://docs.djangoproject.com/en/5.1/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/5.1/ref/settings/
"""

from pathlib import Path
from datetime import timedelta
from dotenv import dotenv_values
import requests
# Application definition

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent

ENV = dotenv_values(str(BASE_DIR) + "/.env")

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/5.1/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = ENV['SECRET_KEY']

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    
    'api',
    'currency',
    
    'rest_framework',
    'rest_framework_simplejwt',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'corsheaders.middleware.CorsMiddleware',
]

REST_FRAMEWORK = {
    'DEFAULT_AUTHENTICATION_CLASSES': (
        'rest_framework_simplejwt.authentication.JWTAuthentication',
        'rest_framework.authentication.BasicAuthentication',
        'rest_framework.authentication.SessionAuthentication',
    ),
}

ROOT_URLCONF = 'current_exchanger.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [
            BASE_DIR / 'templates',
            ],
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

WSGI_APPLICATION = 'current_exchanger.wsgi.application'


# Database
# https://docs.djangoproject.com/en/5.1/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}


# Password validation
# https://docs.djangoproject.com/en/5.1/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/5.1/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/5.1/howto/static-files/

STATIC_URL = 'static/'

# Default primary key field type
# https://docs.djangoproject.com/en/5.1/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

SIMPLE_JWT = {
    'ACCESS_TOKEN_LIFETIME': timedelta(seconds=int(ENV['ACCESS_TOKEN_LIFETIME'])),
    'REFRESH_TOKEN_LIFETIME': timedelta(seconds=int(ENV['REFRESH_TOKEN_LIFETIME'])),
    'UPDATE_LAST_LOGIN': bool(int(ENV['UPDATE_LAST_LOGIN'])),
    'ROTATE_REFRESH_TOKENS': bool(int(ENV['ROTATE_REFRESH_TOKENS'])),
    'BLACKLIST_AFTER_ROTATION': bool(int(ENV['BLACKLIST_AFTER_ROTATION'])),
    
    'ALGORITHM': ENV['ALGORITHM'],
    'SIGNING_KEY': SECRET_KEY,
    'VERIFYING_KEY': ENV['VERIFYING_KEY'],
    'AUDIENCE': ENV['AUDIENCE'],
    'ISSUER': ENV['ISSUER'],
    'JWK_URL': ENV['JWK_URL'],
    'LEEWAY': int(ENV['LEEWAY']),
    'AUTH_HEADER_TYPES' : (ENV["AUTH_HEADER_TYPES"],),
    'AUTH_HEADER_NAME': ENV['AUTH_HEADER_NAME'],
    'USER_ID_FIELD': ENV['USER_ID_FIELD'],
    'USER_AUTHENTICATION_RULE': ENV['USER_AUTHENTICATION_RULE'],
    'AUTH_TOKEN_CLASSES': (ENV['AUTH_TOKEN_CLASSES'],),
    'TOKEN_TYPE_CLAIM': ENV['TOKEN_TYPE_CLAIM'],
    'JTI_CLAIM': ENV['JTI_CLAIM'],
    
    'SLIDING_TOKEN_REFRESH_EXP_CLAIM': ENV['SLIDING_TOKEN_REFRESH_EXP_CLAIM'],
    'SLIDING_TOKEN_LIFETIME': timedelta(seconds=int(ENV['SLIDING_TOKEN_LIFETIME'])),
    'SLIDING_TOKEN_REFRESH_LIFETIME': timedelta(seconds=int(ENV['SLIDING_TOKEN_REFRESH_LIFETIME'])),

}



AVAILABLE_CURRENCIES = list(requests.request(ENV['EXTERNAL_API_METHOD'], ENV['EXTERNAL_API_URL']).json()['Valute'].values())[0:]

for i in AVAILABLE_CURRENCIES:
    i['UID'] = i['ID']
    del i['ID']




LOGIN_URL = 'auth/login/'

