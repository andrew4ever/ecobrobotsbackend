from flask import Flask
from flask_restful import Api
from flask_sqlalchemy import SQLAlchemy

from config import DevConfig
from resources.area import Area
from resources.map import Map

db = SQLAlchemy()


def create_app():
    app = Flask(__name__)
    app.config.from_object(DevConfig())

    api = Api(app)
    api.add_resource(Area, '/area' '/area/<string:square_coords>')
    api.add_resource(Map, '/map')

    db.init_app(app)
    db.create_all()

    return app
