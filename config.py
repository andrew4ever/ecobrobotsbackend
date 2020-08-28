import os


class Config:
    SECRET_KEY = os.urandom(24)

    SESSION_COOKIE_NAME = 'ecobrobotsbackend-websession'
    SESSION_COOKIE_SECURE = True


class ProdConfig(Config):
    FLASK_ENV = 'production'
    DEBUG = False
    TESTING = False


class DevConfig(Config):
    FLASK_ENV = 'development'
    DEBUG = True
    TESTING = True
