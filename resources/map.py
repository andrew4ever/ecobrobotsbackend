from flask_restful import Resource

from models import AreaModel


class Map(Resource):
    def get(self):
        areas = AreaModel.query.filter().all()

        return areas
