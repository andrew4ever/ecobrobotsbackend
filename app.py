from flask import Flask
from flask_restful import Api
from flask_sqlalchemy import SQLAlchemy

from config import DevConfig
from resources.area import AreaResource
from resources.map import Map

db = SQLAlchemy()


def create_app():
    app = Flask(__name__)
    app.config.from_object(DevConfig())

    api = Api(app)
    api.add_resource(AreaResource, '/area' '/area/<string:square_coords>')
    api.add_resource(Map, '/map')

    db.init_app(app)

    with app.app_context():
        from models import AreaModel
        db.create_all()

    return app
