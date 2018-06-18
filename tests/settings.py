# -*- coding: utf-8
from __future__ import unicode_literals, absolute_import
import os
import django

import logging

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

DEBUG = False
USE_TZ = True

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = "gigq!!)$k=gvwi%j!p2s5^r!=4ypwbgp8glsb5o+yogh2lnu)p"

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.sqlite3",
        "NAME": ":memory:",
    }
}

ROOT_URLCONF = "tests.urls"

INSTALLED_APPS = [
    "django.contrib.auth",
    'django.contrib.sessions',
    "django.contrib.contenttypes",
    "simple_notifications",
]

SITE_ID = 1

if django.VERSION >= (1, 10):
    MIDDLEWARE = (
        'django.contrib.sessions.middleware.SessionMiddleware',
        'django.contrib.auth.middleware.AuthenticationMiddleware',
        'django.contrib.auth.middleware.SessionAuthenticationMiddleware',
    )
else:
    MIDDLEWARE_CLASSES = (
        'django.contrib.sessions.middleware.SessionMiddleware',
        'django.contrib.auth.middleware.AuthenticationMiddleware',
        'django.contrib.auth.middleware.SessionAuthenticationMiddleware',
    )

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'templates'), ],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
                "simple_notifications.context_processors.check_user_show_notification"
            ],
        },
    },
]

ALLOWED_HOSTS = ["*"]

logging.disable(logging.CRITICAL)

PASSWORD_HASHERS = (
    'django.contrib.auth.hashers.MD5PasswordHasher',
)
