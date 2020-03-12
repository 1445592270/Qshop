"""
Django settings for Qshop project.

Generated by 'django-admin startproject' using Django 2.2.1.

For more information on this file, see
https://docs.djangoproject.com/en/2.2/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/2.2/ref/settings/
"""

import os

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/2.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '^jgme0enjtuxwspg&z7$366&b)shzvvy)358y%#5pg=(%&uf1q'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ['*']


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'Buyer',
    'Saller',
    'djcelery',
]

MIDDLEWARE = [
    # 'django.middleware.cache.UpdateCacheMiddleware'
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'Qshop.middlewaretest.MiddleWareTest',
    # 'django.middleware.cache.FetchFromCacheMiddleware'
]

ROOT_URLCONF = 'Qshop.urls'

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

WSGI_APPLICATION = 'Qshop.wsgi.application'


# Database
# https://docs.djangoproject.com/en/2.2/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    },
    'slave': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db2.sqlite3'),
}
}

####logging日志的配置
# LOGGING = {
#     'version': 1,
#     'disable_existing_loggers': False,
#     'handlers': {
#         'file': {
#             'level': 'DEBUG',
#             'class': 'logging.FileHandler',
#             'filename': os.path.join(BASE_DIR,'debug.log'),
#         },
#     },
#     'loggers': {
#         'django': {
#             'handlers': ['file'],
#             'level': 'DEBUG',
#             'propagate': True,
#         },
#     },
# }






# Password validation
# https://docs.djangoproject.com/en/2.2/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/2.2/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'Asia/Shanghai'

USE_I18N = True

USE_L10N = True

USE_TZ = False


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/2.2/howto/static-files/

STATIC_URL = '/static/'
STATICFILES_DIRS=(
    os.path.join(BASE_DIR,'static'),
)

# STATIC_ROOT=os.path.join(BASE_DIR,'static')

MEDIA_URL='/media/'
MEDIA_ROOT=os.path.join(BASE_DIR,'static')

## 公钥
alipay_public_key_string = """-----BEGIN PUBLIC KEY-----
MIIBIjANBgkqhkiG9w0BAQEFAAOCAQ8AMIIBCgKCAQEA2kS6XyMGm59Bse/Ry7IuKBSpb4+fPvWMM0086a2zCiVgFzV44Yln/oGV/MUztd5JlH3Oqhv2ldMfCxLuppU9fgS/KqbCdaDMnlLLm9b5P5KYLzc58FU/LILfXpisncI9iIuQBfoDFF/AQrS1KZw0FWCr/y0V5xl2ky4bshVKGkgY8qKlJK2O0FR0tySvHNM/uyfvPcMSwlnm5EncRaHL0IE75pgFM5az1zKoVQ+6X6sZPOxKlZLlbhNyMHJaBnsIGKW7SAkdhyOljBemR/FF3YvAIIQacrBVKB0l/5oHMIvJJIG0Hc7q2SKgxlpoxrRAB8gyJo+mVRu/NnyVoX+TVwIDAQAB
-----END PUBLIC KEY-----"""
## 私钥
alipay_private_key_string = """-----BEGIN RSA PRIVATE KEY-----
MIIEpAIBAAKCAQEA2kS6XyMGm59Bse/Ry7IuKBSpb4+fPvWMM0086a2zCiVgFzV44Yln/oGV/MUztd5JlH3Oqhv2ldMfCxLuppU9fgS/KqbCdaDMnlLLm9b5P5KYLzc58FU/LILfXpisncI9iIuQBfoDFF/AQrS1KZw0FWCr/y0V5xl2ky4bshVKGkgY8qKlJK2O0FR0tySvHNM/uyfvPcMSwlnm5EncRaHL0IE75pgFM5az1zKoVQ+6X6sZPOxKlZLlbhNyMHJaBnsIGKW7SAkdhyOljBemR/FF3YvAIIQacrBVKB0l/5oHMIvJJIG0Hc7q2SKgxlpoxrRAB8gyJo+mVRu/NnyVoX+TVwIDAQABAoIBAC7L23V4Sftlmq0usLlOe2zmeSlNDqRt+uAo6C1lq2Q6fS6crU0Vq7E6UVD/asXMYdQvYPbBxg17VUWHipk2mBeDpwTa+ghEMHqlX7gK0CecI3rECW0IqeG+MWvTqfas5Yp3+an+X1in6s2idtD0B4qpzlaIcRC6Odz2XsPAosGdXC036pmSox/j4R6zFpcjPuqQS9AMYMsOVuWssvl4muMrMWBimAW7/2RO4C1v3DVZtoY+kRoHip/x9h8KLxXZlngUjsWi5VxhMhvg1BzKFFASi9rp/sKw8cqomNxlWuXwKmsW6b+JpQAwV28qIT7GlzHtyvwX68i4s96yKo7+9QECgYEA8xowCN7ki6yGTT5He2fi8PW84mBQb0qvcgIyF+7Q8PY8+zU/QohTCnHEQDcp2Y6H0ZkBPeA7FzD1XBDiAzvlmWG2b3Hw34fMzTbVS0CG5zDsMCf/lqwSzmUc4a2QQHUoq5afsatjZ7nZ0nS5jY+gyjZAst0szIHQxpDAQBUnCoECgYEA5dk/ZjBM3wT/DgJX7BUad14JqTeX+Q3Tx2X4yEDQhTnOsQp57jBkhvAYBRtwCrxeg2HfEr8PdoD0p4gnz/ezZcG4WXFPs7B5zI/fOWvWR/hhw4FBrIUfRpm1fDewZ7HNeTYKlkU/P2K+kH3Myz0OEV2i4ej4mQ/mVccFkkCLQdcCgYEAjbPRFgqem4/oBPRthFBs51nGTQopOIYHOGRxQKQTJLHTn/ZMtoJyLR9dbrT47vh20MToBWJD72O5UX4B0DLExaBAUDvRVOp6hZAVyjSFrhNFSVi3UeNhXu9vY1jhQcFJAKPe2Bh37AlYH6WsVwjGh7gSBHCJ4Xc189iCR5hM1oECgYEAvyWqietFIntfOWFNiTILrpVv52AqbJ7JLpxpBvCP+RuX/re9qw5nq6hj8WteBC+fUhfEkix+SYj47ZJXuaY/dTJjg06uf7sVr78+XtyFeZjghNwrp7OVzPrraQBPHg1J2bHNoCa6cJZH8JYOCD8gQeTjHojGpVQJs/Ate/FdXkUCgYAq13wVODoGBurIAnuzkO5A1tPHASMsh2OtK2Wv3hU9Rkz4QuNmP80ZnnDNgQHkWgI6Pm0AioKiZge2QE6Jjvao9KF6RxHTtU7u+1zytG97Z3DCWwaVWTeW7WDIVVrXwNgV2Yzrm+Ucdgm/YbRva1FusF276K3790AuPTsr2nW0yw==
-----END RSA PRIVATE KEY-----"""

import djcelery
djcelery.setup_loader()
BROKER_URL='redis://127.0.0.1:6379/1'
CELERY_IMPORTS=('CeleryTask.tasks')
CELERY_TIMEZONE='Asia/Shanghai'
CELERYBEAT_SCHEDULER='djcelery.schedulers.DatabaseScheduler'


from celery.schedules import timedelta

CELERYBEAT_SCHEDULE={
    u'测试任务':{
        'task':'CeleryTask.tasks.test',
        'schedule':timedelta(seconds=1)
    }
}

CACHES = {
    'default': {
        'BACKEND': 'django.core.cache.backends.memcached.MemcachedCache',
        'LOCATION':[
            '127.0.0.1:11211'    #本地memcache地址端口
        ]
    }
}
CACHE_MIDDLEWARE_KEY_PREFIX = ''
CACHE_MIDDLEWARE_SECONDS = 600
CACHE_MIDDLEWARE_ALIAS = 'default'
