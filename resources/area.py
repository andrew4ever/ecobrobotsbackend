from flask_restful import Resource, request

from models import AreaModel


class AreaResource(Resource):
    def get(self):
        area_coords = request.args.get('area_coords')

        if not '-' in area_coords:
            return {'code': 400, 'message': 'Invalid coordinate format'}, 400

        latitude, longitude = area_coords.split('-')

        areas = AreaModel.query.filter_by(
            latitude=latitude).filter_by(longitude=longitude).limit(10).all()

        if not areas:
            return {'code': 404, 'message': 'Area not found'}, 404

        areas_list = []
        for area in areas:
            areas_list.append(area.as_dict())

        return areas_list
