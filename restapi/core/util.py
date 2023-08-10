import os
import json
import logging
from logging.handlers import RotatingFileHandler
from typing import Iterable

from django.core import serializers
from restapi.core import conf


def get_logging_level():
    """ Return logging level by the value of environment variable"""
    log_dict = {
        "info": logging.INFO,
        "debug": logging.DEBUG,
        "warning": logging.WARNING,
        "critical": logging.CRITICAL,
        "error": logging.ERROR,
    }

    lvl = os.getenv("XXX_LOG_LEVEL", "debug").strip().lower()
    return log_dict[lvl]


def init_logger(name: str = 'xxx'):
    logger = logging.getLogger(name)
    logger.setLevel(get_logging_level())
    sh = logging.StreamHandler()
    fh = RotatingFileHandler('main.log', mode='a', maxBytes=conf.LOG_MAX_BYTES, backupCount=conf.LOG_BACKUP_COUNT)
    fmt = logging.Formatter(conf.LOG_FORMAT)

    sh.setFormatter(fmt)
    fh.setFormatter(fmt)
    logger.addHandler(sh)
    logger.addHandler(fh)
    return logger

LOG = init_logger(__name__)

def convert_django_model(django_model) -> list:
    LOG.debug(f"django_model iterable: {isinstance(django_model, Iterable)}")
    if isinstance(django_model, Iterable):
        serial_json = serializers.serialize('json', django_model)
    else:
        # If "django_model" is not iterable, convert it to list
        serial_json = serializers.serialize('json', [django_model])
    objects = []
    LOG.debug(f"serial_json: {serial_json}")
    for object in json.loads(serial_json):
        data = object['fields']
        data['pk'] = object['pk']
        objects.append(data)
    return objects
