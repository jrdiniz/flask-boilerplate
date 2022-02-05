import os

BASE_DIR = os.path.abspath(os.path.dirname(__file__))

class Config(object):
    # Default
    SECRET_KEY = "flask-bolierplate"

class ProductionConfig(Config):
    # Debug
    DEBUG = False

class DevelopmentConfig(Config):
    # Debug
    DEBUG = True

class TestingConfig(Config):
    # Debug
    DEBUG = True