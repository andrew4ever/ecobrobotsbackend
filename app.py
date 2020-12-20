import logging
from os import environ

from flask import Flask
from flask_cors import CORS
from flask_restful import Api
from flask_sqlalchemy import SQLAlchemy

from config import DevConfig, ProdConfig

db = SQLAlchemy()


def create_app():
    from resources import Area, Map, Ping, SensorData

    env = environ.get('ENVIRONMENT')
    if env == 'DEVELOPMENT':
        Config = DevConfig
    else:
        Config = ProdConfig

    app = Flask(__name__)
    app.config.from_object(Config())
    CORS(app)
    logging.basicConfig(
        filename='app.log',
        level=logging.INFO
    )

    api = Api(app)
    api.add_resource(Area, '/area')
    api.add_resource(Map, '/map')
    api.add_resource(SensorData, '/api/v1/saveSensorData')
    api.add_resource(Ping, '/ping')

    db.init_app(app)

    with app.app_context():
        from models import AreaModel, SensorDataModel
        db.create_all()

    return app
