import os
from os import environ

from common import load_config

load_config()


class Config:
    SECRET_KEY = os.urandom(24)

    SESSION_COOKIE_NAME = environ.get('SESSION_COOKIE_NAME')
    SESSION_COOKIE_SECURE = True

    SQLALCHEMY_DATABASE_URI = environ.get('SQLALCHEMY_DATABASE_URI')
    SQLALCHEMY_ECHO = False
    SQLALCHEMY_TRACK_MODIFICATIONS = False


class ProdConfig(Config):
    FLASK_ENV = 'production'
    DEBUG = False
    TESTING = False


class DevConfig(Config):
    FLASK_ENV = 'development'
    DEBUG = True
    TESTING = True
