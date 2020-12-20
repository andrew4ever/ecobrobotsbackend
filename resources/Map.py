from datetime import datetime, timedelta
from os import environ

from common.convert_types_to_names import convert_types_to_names
from flask_restful import Resource
from models import AreaModel
from sqlalchemy import desc


class Map(Resource):
    def get(self):
        maxdate = datetime.now() - timedelta(hours=int(environ.get('MAX_RECORD_HOURS')))

        areas = AreaModel.query.order_by(desc(AreaModel.created)).filter(
            AreaModel.created >= maxdate).all()

        areas_coords = []
        areas_list = []

        for area in areas:
            if (area.latitude, area.longitude) in areas_coords:
                continue

            areas_coords.append((area.latitude, area.longitude))
            areas_list.append(convert_types_to_names(area))

        return areas_list
