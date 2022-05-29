import os

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))



# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '!*ndp-(t$)0cgpl!q4bh^t^o%&*z8!=&g-*e+bocov1h#5zsux'

DEBUG = False

ALLOWED_HOSTS = ["127.0.0.1"]

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'NewDb',
        'USER': 'userdb',
        'PASSWORD': '1234567',
        'HOST': 'localhost',
        'PORT': '5432'
    }
}

STATICFILES_DIRS = (
os.path.join(BASE_DIR, 'static'),
)
STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')