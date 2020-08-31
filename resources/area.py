from flask_restful import Resource, request

from models import AreaModel


class AreaResource(Resource):
    def get(self):
        area_coords = request.args.get('area_coords')

        latitude, longitude = area_coords.split('-')

        area = AreaModel.query.filter_by(
            latitude=latitude, longitude=longitude).first()

        if not area:
            return {'code': 404, 'message': 'Area not found'}, 404

        return area
