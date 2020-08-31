from flask_restful import Resource, request

from models import AreaModel


class AreaResource(Resource):
    def get(self):
        area_coords = request.args.get('area_coords')

        latitude, longitude = area_coords.split('-')

        areas = AreaModel.query.filter_by(
            latitude=latitude, longitude=longitude).limit(10).all()

        if not areas:
            return {'code': 404, 'message': 'Area not found'}, 404

        return areas
