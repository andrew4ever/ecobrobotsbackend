from flask_restful import Resource, request
from sqlalchemy import desc

from models import AreaModel


class AreaResource(Resource):
    def get(self):
        latitude = request.args.get('latitude')
        longitude = request.args.get('longitude')

        areas = AreaModel.query \
            .filter_by(latitude=latitude) \
            .filter_by(longitude=longitude) \
            .order_by(desc(AreaModel.created)).all()

        if not areas:
            return {'code': 404, 'message': 'Area not found'}, 404

        areas_list = []
        for area in areas:
            areas_list.append(area.as_dict())

        return areas_list
