"""
Django settings for itbook_service project.

Generated by 'django-admin startproject' using Django 4.1.5.

For more information on this file, see
https://docs.djangoproject.com/en/4.1/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/4.1/ref/settings/
"""
import os.path
from datetime import timedelta
from pathlib import Path
import pymysql
import my_settings


pymysql.install_as_MySQLdb()

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/4.1/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = my_settings.SECRET['secret']
JWT_SECRET_KEY = "django-insecure-cr)vvqzsg7##)a1e=mu1e0x#_(kyov96bdsr_1z_wfa()+niof"

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True
#'192.168.56.101','localhost','127.0.0.1','192.168.163.168', '192.168.160.98'
ALLOWED_HOSTS = ['*']
CORS_ORIGIN_WHITELIST = ['http://127.0.0.1:3000' ,'http://localhost:8000']

AUTH_USER_MODEL = 'account.UserData'

# Application definition

INSTALLED_APPS = [
    "baton",
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
    "home.apps.HomeConfig",
    "class.apps.ClassConfig",
    "chat.apps.ChatConfig",
    "major.apps.MajorConfig",
    "setting.apps.SettingConfig",
    "account.apps.UserConfig",
    "taggit_templatetags2",
    "taggit.apps.TaggitAppConfig",
    "rest_framework",
    "rest_framework.authtoken",
    'rest_framework_simplejwt',
    "corsheaders",
    'django_filters',
    'taggit_serializer',
    'channels',
    "baton.autodiscover",
]



BATON ={
    'SITE_HEADER': 'IT-BOOK',
    'SITE_TITLE': 'IT-BOOK',
    'INDEX_TITLE': 'Site administration',
    'SUPPORT HREF': "https://github.com/tukorea-work-2022-2023",
    'COPYRIGHT': "copyright © 2023 IT-BOOK",
    'POWERED_BY': '<a href-"https://github.com/tukorea-work-2022-2023">IT-BOOK</a>',
    'MENU TITLE': 'MENU TITLE',
}




REST_FRAMEWORK = {
    'DEFAULT_AUTHENTICATION_CLASSES': [
        #'rest_framework.authentication.TokenAuthentication',
        'rest_framework_simplejwt.authentication.JWTAuthentication',
    ],
    'DEFAULT_FILTER_BACKENDS': [
        'django_filters.rest_framework.DjangoFilterBackend',
    ]  # django-filter 모듈이 프로젝트 전역에 적용됨에 주의
}

SIMPLE_JWT = {
    'ACCESS_TOKEN_LIFETIME': timedelta(hours=2),
    'REFRESH_TOKEN_LIFETIME': timedelta(days=7),
    'ROTATE_REFRESH_TOKENS': False,
    'BLACKLIST_AFTER_ROTATION': True,
    'TOKEN_USER_CLASS': 'users.User',
    'ALGORITHM': 'HS256',
    'SIGNING_KEY': JWT_SECRET_KEY,
}


EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = 'smtp.gmail.com' # 메일 호스트 서버
EMAIL_PORT = 587 # gmail과 통신하는 포트
EMAIL_HOST_USER = 'chajiwon3168@gmail.com' # 발신할 이메일
EMAIL_HOST_PASSWORD = 'onbuwecilqrhkyhd' # 앱 비밀번호
EMAIL_USE_TLS = True # TLS 보안 방법


MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.common.CommonMiddleware",
    #"django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
    "corsheaders.middleware.CorsMiddleware",

]

ROOT_URLCONF = "itbook_service.urls"

TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [],
        "APP_DIRS": True,
        "OPTIONS": {
            "context_processors": [
                "django.template.context_processors.debug",
                "django.template.context_processors.request",
                "django.contrib.auth.context_processors.auth",
                "django.contrib.messages.context_processors.messages",
            ],
        },
    },
]

WSGI_APPLICATION = "itbook_service.wsgi.application"
ASGI_APPLICATION = 'itbook_service.asgi.application'

CHANNEL_LAYERS = {
    "default": {
        "BACKEND": "channels.layers.InMemoryChannelLayer"
    }
}

# Database
# https://docs.djangoproject.com/en/4.1/ref/settings/#databases

DATABASES = my_settings.DATABASES


# Password validation
# https://docs.djangoproject.com/en/4.1/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        "NAME": "django.contrib.auth.password_validation.UserAttributeSimilarityValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.MinimumLengthValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.CommonPasswordValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.NumericPasswordValidator",
    },
]




LANGUAGE_CODE = "ko-kr"

TIME_ZONE = "Asia/Seoul"

USE_I18N = True

USE_TZ = False


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.1/howto/static-files/

STATIC_URL = "static/"

MEDIA_URL='/media/'
MEDIA_ROOT=os.path.join(BASE_DIR,'media')

TAGGIT_CASE_INSENTIVE=True
TAGGIT_LIMIT=50

# Default primary key field type
# https://docs.djangoproject.com/en/4.1/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"


##CORS
CORS_ORIGIN_ALLOW_ALL=True
CORS_ALLOW_CREDENTIALS = True
CORS_ALLOW_METHODS = (
    'DELETE',
    'GET',
    'OPTIONS',
    'PATCH',
    'POST',
    'PUT',
)
CORS_ALLOW_HEADERS = (
    'accept',
    'accept-encoding',
    'authorization',
    'content-type',
    'dnt',
    'origin',
    'user-agent',
    'x-csrftoken',
    'x-requested-with',

)

REST_FRAMEWORK = {
    'DEFAULT_AUTHENTICATION_CLASSES': [
        'rest_framework.authentication.TokenAuthentication',
    ],
}
