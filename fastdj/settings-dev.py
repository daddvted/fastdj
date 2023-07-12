from .settings import *

DEBUG = True

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'fastdj',
        'USER': 'root',
        'PASSWORD': 'root',
        'HOST': '10.0.0.111',
        'PORT': '3306',
    }
}