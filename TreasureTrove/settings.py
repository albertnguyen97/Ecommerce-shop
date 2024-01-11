"""
Django settings for TreasureTrove project.

Generated by 'django-admin startproject' using Django 4.2.7.

For more information on this file, see
https://docs.djangoproject.com/en/4.2/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/4.2/ref/settings/
"""
from django.urls import reverse_lazy
from pathlib import Path


# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/4.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-*kqq!agaw@7me-8$_&2d6v@!(ld5w*c47qq7mnc(ez9y_exdp='

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ['mysite.website', 'localhost', '127.0.0.1']

EMAIL_HOST = 'smtp.gmail.com'
EMAIL_HOST_USER = 'chaunm.hmc@gmail.com'
EMAIL_HOST_PASSWORD = 'zwdn eyqh rpsy vsex'
EMAIL_PORT = 587
EMAIL_USE_TLS = True

EMAIL_BACKEND = 'django_ses.SESBackend'
AWS_ACCESS_KEY_ID = 'AKIAQKRB5Q5IKJ4AWIXN'
AWS_SECRET_ACCESS_KEY = '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'

# Additionally, if you are not using the default AWS region of us-east-1,
# you need to specify a region, like so:
AWS_SES_REGION_NAME = 'ap-southeast-2'
AWS_SES_REGION_ENDPOINT = 'email.ap-southeast-2.amazonaws.com'

# If you want to use the SESv2 client
USE_SES_V2 = True
SITE_ID = 1
# Application definition

INSTALLED_APPS = [
    'account.apps.AccountConfig',
    'shop.apps.ShopConfig',
    'cart.apps.CartConfig',
    'orders',
    'payment.apps.PaymentConfig',
    'jet.dashboard',
    'jet',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'social_django',
    'django_extensions',
    'easy_thumbnails',

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

ROOT_URLCONF = 'TreasureTrove.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [BASE_DIR / 'templates']
        ,
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
                'cart.context_processors.cart',
            ],
        },
    },
]

WSGI_APPLICATION = 'TreasureTrove.wsgi.application'

# Database
# https://docs.djangoproject.com/en/4.2/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'treasuretrovedb',
        'USER': 'treasureadmin',
        'PASSWORD': 'Chaubau123@',
        'HOST': 'localhost',
        'PORT': '3306',
    }
}

# Password validation
# https://docs.djangoproject.com/en/4.2/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/4.2/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_TZ = True

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.2/howto/static-files/

STATIC_URL = 'static/'

# Default primary key field type
# https://docs.djangoproject.com/en/4.2/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

LOGIN_REDIRECT_URL = 'shop'
LOGIN_URL = 'login'
LOGOUT_URL = 'logout'


MEDIA_URL = 'media/'
MEDIA_ROOT = BASE_DIR / 'media'

AUTHENTICATION_BACKENDS = [
    'django.contrib.auth.backends.ModelBackend',
    'account.authentication.EmailAuthBackend',
    'social_core.backends.facebook.FacebookOAuth2',
]

SOCIAL_AUTH_FACEBOOK_KEY = 'XXX' # Facebook App ID
SOCIAL_AUTH_FACEBOOK_SECRET = 'XXX' # Facebook App Secret
SOCIAL_AUTH_FACEBOOK_SCOPE = ['email']

CART_SESSION_ID = 'cart'

ABSOLUTE_URL_OVERRIDES = {
    'auth.user': lambda u: reverse_lazy('user_detail',
                                        args=[u.username])
}

REDIS_HOST = 'localhost'
REDIS_PORT = 6379
REDIS_DB = 0
STRIPE_PUBLISHABLE_KEY = 'pk_test_51OPJO9KsjShnriJD1tfY2E8Z8liNekMvIHuxePVR1l7slZgbgE2EnP9LaBDksXmqlZHXAG5moIi2DLCR9YqYwAjV00QFKJM3vF' # Publishable key
STRIPE_SECRET_KEY = 'sk_test_51OPJO9KsjShnriJDmhfeGRdRcc4uajOreynoRZtJo9MpBtnEMGYjF2W1B1qj0tQdyFDiw6FaR5WdE2PdUIdlsSGE007bv0tn1Q'      # Secret key
STRIPE_API_VERSION = '2023-10-16'

STRIPE_WEBHOOK_SECRET = 'whsec_d52b6cf3812d2a6dd6305fc7d407a7758128f49ea5badfa97ade354ebaf50e5c'

STATIC_ROOT = BASE_DIR / 'static'

