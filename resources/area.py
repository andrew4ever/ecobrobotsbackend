from flask_restful import Resource

from models import AreaModel


class AreaResource(Resource):
    def get(self, area_coords):
        latitude, longitude = area_coords.split('-')

        area = AreaModel.query.filter_by(
            latitude=latitude, longitude=longitude).first()

        return area
