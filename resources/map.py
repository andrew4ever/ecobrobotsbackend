from flask_restful import Resource

from models import AreaModel


class Map(Resource):
    def get(self):
        areas = AreaModel.query.order_by(AreaModel.created).all()

        areas_list = []
        for area in reversed(areas):
            areas_list.append(area.as_dict())

        return areas_list
