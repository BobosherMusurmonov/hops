"""
Django settings for service project.

Generated by 'django-admin startproject' using Django 3.1.2.

For more information on this file, see
https://docs.djangoproject.com/en/3.1/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/3.1/ref/settings/
"""
import os
from pathlib import Path

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/3.1/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = os.environ.get('SECRET_KEY')

# SECURITY WARNING: don't run with debug turned on in production!
PRODUCTION_MODE = os.environ.get('PROD', False)
DEBUG = not PRODUCTION_MODE

ALLOWED_HOSTS = ['*']

# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.humanize',
    'core',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'hops.urls'

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

WSGI_APPLICATION = 'hops.wsgi.application'

# Database
# https://docs.djangoproject.com/en/3.1/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}

# Password validation
# https://docs.djangoproject.com/en/3.1/ref/settings/#auth-password-validators

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

LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'handlers': {
        'console': {
            'class': 'logging.StreamHandler',
        },
    },
    'root': {
        'handlers': ['console'],
        'level': 'WARNING',
    },
    'loggers': {
        'django': {
            'handlers': ['console'],
            'level': os.getenv('DJANGO_LOG_LEVEL', 'INFO'),
            'propagate': False,
        },
    },
}

# Internationalization
# https://docs.djangoproject.com/en/3.1/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'Asia/Tashkent'

USE_I18N = True

USE_L10N = True

USE_TZ = False

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.1/howto/static-files/

STATIC_URL = '/static/'
STATIC_ROOT = BASE_DIR / 'static'
CONTROL_PAGE_URL = os.environ.get('CONTROL_PAGE_URL')

MEDIA_ROOT = BASE_DIR / 'media'
MEDIA_URL = '/media/'

# HOPS-SPECIFIC CONFIGS
BOT_TOKEN = os.environ.get('BOT_TOKEN')
MAIN_GROUP_ID = int(os.environ.get('MAIN_GROUP_ID'))
TEST_GROUP_ID = int(os.environ.get('TEST_GROUP_ID'))
BOARD_GROUP_ID = int(os.environ.get('BOARD_GROUP_ID'))
TELEGRAPH_TOKEN = os.environ.get('TELEGRAPH_TOKEN')
DEV_ID = int(os.environ.get('DEV_ID'))
PROHIBITED_TOPICS = [
    {
        "name": "botlar",
        "targets": ["bot"],
        "spoilers": [
            ("🅱️", "b"),
            ("🅾️", "o"),
            ("⭕", "o"),
            ("✝️", "t"),
            ("🤖", "bot"),
            ("0", "o"),
            ("\n", "")
        ],
        "whitelist": [
            "botan", "botanik", "botqa", "hisobot", "astrobot", "yunusobot", "botiq", "botmon", "robotexnika",
            "botma", "botanika", "botqo", "botgan", "botkan", "botib", "botir", "botak", "botmon", "razrabot",
            "obrabot", "robot", "isbot", "rabot", "umrbot", "botstrap", "boot", "bootcamp", "botcamp"
        ],
        "hint": "Bu mavzuda gaplash uchun quyidagi guruhlarga kirishingiz mumkin: @botlarhaqida, @telebot_uz, "
                "@it_uz_offtopic"
    }
]
