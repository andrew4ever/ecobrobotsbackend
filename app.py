from flask import Flask
from flask_restful import Api

from config import DevConfig
from resources.area import Area
from resources.map import Map

app = Flask(__name__)
app.config.from_object(DevConfig())

api = Api(app)
api.add_resource(Area, '/area' '/area/<string:square_coords>')
api.add_resource(Map, '/map')
