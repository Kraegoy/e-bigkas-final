

import os
from pathlib import Path
from dotenv import load_dotenv

# Load .env file
load_dotenv()




# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/5.1/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-uuky)(k2i(ifs$4wgz*e^^o&^s8jpp(b*n6lb#&#s6ee*-c(%2'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ['localhost', '127.0.0.1', '98.80.234.132', 'ebigkas.com', 'wwww.ebigkas.com']


# Application definition

INSTALLED_APPS = [
    'daphne',
    'channels',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'ebigkasAPP.apps.EbigkasappConfig',
    'ebigkasAdminAPP',
    'ebigkasLearnings',
    'storages',
    'whitenoise.runserver_nostatic',

]

CHANNEL_LAYERS = {
     'default': {
        'BACKEND': 'channels.layers.InMemoryChannelLayer',
    },
}


ASGI_APPLICATION = "ebigkasProject.asgi.application"


MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'whitenoise.middleware.WhiteNoiseMiddleware',
]

ROOT_URLCONF = 'ebigkasProject.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [
            BASE_DIR / 'templates'
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

WSGI_APPLICATION = 'ebigkasProject.wsgi.application'




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

TIME_ZONE = 'Asia/Manila'

USE_I18N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/5.1/howto/static-files/

# Add these at the end of your settings file if they aren't present
STATIC_URL = '/static/'
STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')

# Additional static directories (if needed)
STATICFILES_DIRS = [
    os.path.join(BASE_DIR, 'static'),  # Assuming you have a 'static' directory in your project
]
# Default primary key field type
# https://docs.djangoproject.com/en/5.1/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

# URL where users should be redirected to when they are not logged in
LOGIN_URL = '/login/'

# URL where users should be redirected to after they log in
LOGIN_REDIRECT_URL = '/'




AWS_ACCESS_KEY_ID = os.getenv('AWS_ACCESS_KEY_ID')
AWS_SECRET_ACCESS_KEY = os.getenv('AWS_SECRET_ACCESS_KEY')

AWS_STORAGE_BUCKET_NAME = 'ebigkas-bkt-41'
AWS_S3_CUSTOM_DOMAIN = '%s.s3.amazonaws.com' % AWS_STORAGE_BUCKET_NAME
AWS_S3_FILE_OVERWRITE = False

STORAGES = {
    
    #MEDIA FILE (IAMGE) MANAGEMENT
    "default": {
        "BACKEND": "storages.backends.s3boto3.S3StaticStorage",
    },
        
    #CSS AND JS FILE MANAGEMENT
    "staticfiles": {
        "BACKEND": "storages.backends.s3boto3.S3StaticStorage",
    },
}

MEDIA_URL = f'https://{AWS_S3_CUSTOM_DOMAIN}/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')



SESSION_COOKIE_AGE = 259200  # 3 days in seconds
SESSION_EXPIRE_AT_BROWSER_CLOSE = True

# Email configuration in settings.py
EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_PORT = 587
EMAIL_USE_TLS = True
EMAIL_HOST_USER="ebigkas1@gmail.com"
EMAIL_HOST_PASSWORD="rwno kmun mcvs twvj"
DEFAULT_FROM_EMAIL="ebigkas1@gmail.com"
