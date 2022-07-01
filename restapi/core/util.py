import os
import json
import logging
from typing import Iterable

from django.core import serializers


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


def get_logger(name: str = 'xxx'):
    log = logging.getLogger(name)
    # log_format = '[%(asctime)s] %(levelname)s: %(message)s'
    # date_format = '%Y-%m-%d %H:%M:%S'
    # logging.basicConfig(format=log_format, datefmt=date_format)
    log.setLevel(get_logging_level())
    return log


def convert_django_model(django_model) -> list:
    print(isinstance(django_model, Iterable))
    if isinstance(django_model, Iterable):
        serial_json = serializers.serialize('json', django_model)
    else:
        serial_json = serializers.serialize('json', [django_model])
    objects = []
    for object in json.loads(serial_json):
        print(f'convert - object: {object}')
        data = object['fields']
        data['pk'] = object['pk']
        objects.append(data)
    return objects
