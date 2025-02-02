"""
Django settings for greatkart project.

Generated by 'django-admin startproject' using Django 3.1.

For more information on this file, see
https://docs.djangoproject.com/en/3.1/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/3.1/ref/settings/
"""
import os
import dj_database_url

from pathlib import Path
from decouple import config

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve(strict=True).parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/3.1/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'f^=5pd1lso=1zxm*da!r$=@%o937%zv+4n7pvtgkoiuk3tkps('
#SECRET_KEY = config('SECRET_KEY')

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True
#'web-production-7c8d.up.railway.app'
#ALLOWED_HOSTS = ['djangshop-production.up.railway.app']

ALLOWED_HOSTS = ['*']
# Application definition

INSTALLED_APPS = [
   
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.sites', 
    'category',
    'accounts',
    'store',
    'carts',
    'orders',
    'cloudinary_storage',
   
    'cloudinary','parler',
    'news',
  
    'allauth',
        'allauth.account',
    'allauth.socialaccount',
    'allauth.socialaccount.providers.google',
   
      'events',
]
SITE_ID = 2
ACCOUNT_EMAIL_REQUIRED=True ,
ACCOUNT_USERNAME_REQURIED=True
LOGIN_REDIRECT_URL = "/"
SOCIALACCOUNT_LOGIN_ON_GET =True
ACCOUNT_AUTHENTICATED_LOGIN_REDIRECTS =True
SOCIAL_AUTH_REDIRECT_IS_HTTPS = True
ACCOUNT_DEFAULT_HTTP_PROTOCOL = "https"

ROSETTA_ACCESS_CONTROL_FUNCTION = "has_rosetta_access"
ROSETTA_TRANSLATORS = ["mail@example.com", "mail@gmail.com"]
def has_rosetta_access(user):
    is_translator = (user.email in ROSETTA_TRANSLATORS)
    return user.is_authenticated() and (user.is_staff or user.is_admin or is_translator)

AUTHENTICATION_BACKENDS = [
    
    # Needed to login by username in Django admin, regardless of `allauth`
    'django.contrib.auth.backends.ModelBackend',

    # `allauth` specific authentication methods, such as login by e-mail
    'allauth.account.auth_backends.AuthenticationBackend',

]
SOCIALACCOUNT_PROVIDERS = {
   
    "google": {
        # For each OAuth based provider, either add a ``SocialApp``
        # (``socialaccount`` app) containing the required client
        # credentials, or list them here:
       
     
        # These are provider-specific settings that can only be
        # listed here:
        "SCOPE": [
            "profile",
            "email",
        ],
        "AUTH_PARAMS": {
            "access_type": "online",
        }
    },
    'facebook':
{'METHOD': 'oauth2',
'SCOPE': ['email','public_profile', 'user_friends'],
'AUTH_PARAMS': {'auth_type': 'reauthenticate'},
'FIELDS': [
'id',
'email',
'name',
'first_name',
'last_name',
'verified',
'locale',
'timezone',
'link',
'gender',
'updated_time'],
'EXCHANGE_TOKEN': True,
'LOCALE_FUNC': lambda request: 'kr_KR',
'VERIFIED_EMAIL': False,
'VERSION': 'v2.4'}}
CROS_ORIGIN_ALLOW_ALL = True

MIDDLEWARE = [
  'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
   
    'django.middleware.common.CommonMiddleware',
    
    
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    #  "whitenoise.middleware.WhiteNoiseMiddleware", 
     #'language.DefaultLanguageMiddleware',
    'django.middleware.locale.LocaleMiddleware',
    "allauth.account.middleware.AccountMiddleware",
     
]

ROOT_URLCONF = 'greatkart.urls'
STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': ['templates'],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
                'category.context_processors.menu_links',
                'carts.context_processors.counter','django.template.context_processors.i18n',
            ],
        },
    },
]

WSGI_APPLICATION = 'greatkart.wsgi.application'

AUTH_USER_MODEL= 'accounts.Account'
DEFAULT_AUTO_FIELD='django.db.models.AutoField'
# Database
# https://docs.djangoproject.com/en/3.1/ref/settings/#databases

"""DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}"""

DATABASES = {
     'default': dj_database_url.config(
         default=config('DATABASE_URL')
     )
}
"""DATABASES = {
    'default': dj_database_url.parse(
        'postgresql://admin_f26u_user:e1IHffzBbLfSBjFBvMp7t0ybBSlgkvVy@dpg-cu04db1opnds73e0iiq0-a.oregon-postgres.render.com/admin_f26u',
        conn_max_age=600,
        conn_health_checks=True,
    )
}"""

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

from django.utils.translation import gettext_lazy as _
# Internationalization
# https://docs.djangoproject.com/en/3.1/topics/i18n/


  
LANGUAGES = (
    ('en', _('English')),
    
     ('zh-hans', _('Simplified Chinese')),  
     ('zh-hant', _('Traditional Chinese')),
)

LANGUAGE_CODE = 'en'
DEFAULT_LANGUAGE = 1
TIME_ZONE = 'UTC'



USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.1/howto/static-files/

LOCALE_PATHS = [
   os.path.join(BASE_DIR, 'locale')
]

STRIPE_PUBLISHABLE_KEY = 'pk_test_51Le1xPC7VbGDnuTQKF08JQS4ago45ZtANqkhwfTQQCn9H2SmlQlSRp9uPnJNiPVNia3SvMfLFjIXfbwuMDQBRnCJ00Uw95ni84'
STRIPE_SECRET_KEY = 'sk_test_51Le1xPC7VbGDnuTQKnNun4BoSH7W9vYTIceV6CVrn8AZZy0KqhzvZkhyR1qPArmfJxF1UbfJgh34rhtOOWM0jJch00ZDazOyyS'
# Static files (CSS, JavaScript, Images)

STATIC_URL = '/static/'
#STATICFILES_DIRS = [BASE_DIR / "static",]


STATIC_ROOT = os.path.join(BASE_DIR, 'static')
# media files configuration
MEDIA_URL = '/media/'
MEDIA_ROOT = BASE_DIR /'media'

from django.contrib.messages import constants as messages
MESSAGE_TAGS = {
    messages.ERROR: 'danger',
}

CROS_ORIGIN_ALLOW_ALL = True
EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
# SMTP configuration
"""EMAIL_HOST = config('EMAIL_HOST')
EMAIL_PORT = config('EMAIL_PORT', cast=int)
EMAIL_HOST_USER = config('EMAIL_HOST_USER')
EMAIL_HOST_PASSWORD = config('EMAIL_HOST_PASSWORD')
EMAIL_USE_TLS = config('EMAIL_USE_TLS', cast=bool)


"""
CLOUDINARY_STORAGE = {
    'CLOUD_NAME': 'fahim1213456',
    'API_KEY': '554889398149233',
    'API_SECRET': 'xOh9Pctuw1UhBuRrj_XuP79ubbA'
}
DEFAULT_FILE_STORAGE = 'cloudinary_storage.storage.MediaCloudinaryStorage'