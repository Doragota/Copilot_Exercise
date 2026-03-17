import os
from pathlib import Path

# Alapbeállítások VAR használatával
VAR_BASE_DIR = Path(__file__).resolve().parent.parent
VAR_SECRET_KEY = 'django-insecure-test-key'
VAR_DEBUG = True
VAR_ALLOWED_HOSTS = []

# Alkalmazások listája
VAR_INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'octofit_tracker',
]

# MongoDB konfiguráció
VAR_DATABASES = {
    'default': {
        'ENGINE': 'djongo',
        'NAME': 'octofit_db',
    }
}

# Átadás a Django-nak
SECRET_KEY = VAR_SECRET_KEY
DEBUG = VAR_DEBUG
ALLOWED_HOSTS = VAR_ALLOWED_HOSTS
INSTALLED_APPS = VAR_INSTALLED_APPS
DATABASES = VAR_DATABASES