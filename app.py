from flask import Flask
from flask_cors import CORS
from flask_restful import Api
from flask_sqlalchemy import SQLAlchemy

from config import DevConfig as Config

db = SQLAlchemy()


def create_app():
    from resources import Area
    from resources import Map
    from resources import SensorData

    app = Flask(__name__)
    app.config.from_object(Config())
    CORS(app)

    api = Api(app)
    api.add_resource(Area, '/area')
    api.add_resource(Map, '/map')
    api.add_resource(SensorData, '/saveSensorData')

    db.init_app(app)

    with app.app_context():
        from models import AreaModel, SensorDataModel
        db.create_all()

    return app


if __name__ == '__main__':
    app = create_app()
    app.run(host='0.0.0.0', port=8080)
