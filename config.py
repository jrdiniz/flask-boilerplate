import os

BASE_DIR = os.path.abspath(os.path.dirname(__file__))

class Config(object):
    # Default
    SECRET_KEY = "C3}Z%~H:qvjdhm}e)=Cjen4[t.7fNEP*3dd9--RB&jgVAm?hYz95809580958091435DD"
    TIMEZONE = "America/Sao_Paulo"

class ProductionConfig(Config):
    # Debug
    DEBUG = False

class DevelopmentConfig(Config):
    # Debug
    DEBUG = True

class TestingConfig(Config):
    # Debug
    DEBUG = True