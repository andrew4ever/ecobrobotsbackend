from flask import Flask
from flask_restful import Api
from flask_sqlalchemy import SQLAlchemy

from config import DevConfig as Config


db = SQLAlchemy()


def create_app():
    from resources.area import AreaResource
    from resources.map import Map

    app = Flask(__name__)
    app.config.from_object(Config())

    api = Api(app)
    api.add_resource(AreaResource, '/area')
    api.add_resource(Map, '/map')

    db.init_app(app)

    with app.app_context():
        from models import AreaModel
        db.create_all()

    return app
