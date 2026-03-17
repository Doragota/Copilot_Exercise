import os
from pathlib import Path

# Útvonalak
BASE_DIR = Path(__file__).resolve().parent.parent
SECRET_KEY = 'django-insecure-test-key'
DEBUG = True

# --- CODESPACE BEÁLLÍTÁSOK ---
VAR_CODESPACE_NAME = os.getenv('CODESPACE_NAME')
VAR_CODESPACE_DOMAIN = '.app.github.dev'

ALLOWED_HOSTS = [
    f"{VAR_CODESPACE_NAME}-8000{VAR_CODESPACE_DOMAIN}",
    'localhost',
    '127.0.0.1',
    '.github.dev'
]

# Ez is kellhet a biztonságos kapcsolathoz
CSRF_TRUSTED_ORIGINS = [
    f"https://{VAR_CODESPACE_NAME}-8000{VAR_CODESPACE_DOMAIN}"
]
# -----------------------------

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'octofit_tracker', 
    'rest_framework', # Ezt is add hozzá a Step 4 miatt!
]

DATABASES = {
    'default': {
        'ENGINE': 'djongo',
        'NAME': 'octofit_db',
    }
}