import os
import logging
from helpers import _open_yaml

_basedir = os.path.abspath(os.path.dirname(__file__))
class Config(object):

    # Default Values

    def __init__(self):
        self.configObject = {}
        # Open config
        self.configObject=_open_yaml("config.yml")
        # COnfig Logger
        self.LOG_LVL = self.configObject['logger']['level']
        self.LOG_PATH = "{}/{}".format(
            _basedir,
            self.configObject['logger']['path'])
        self.LOG_FORMAT = self.configObject['logger']['format']
        # Config dataset
        self.CSV_FILE = "{}{}".format(
            self.configObject['service']['filepath'],
            self.configObject['service']['dataset'])
        self.SCHEME = self.configObject['service']['scheme']
        # Config ElasticSearch backend
        self.ES_HOST = self.configObject['elastic']['hostname']
        self.ES_PORT = self.configObject['elastic']['port']
        self.ES_USER = self.configObject['elastic']['user']
        self.ES_PASS = self.configObject['elastic']['pass']
        # Config scheme
