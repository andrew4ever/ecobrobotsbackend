from datetime import datetime, timedelta
from os import environ

from flask_restful import Resource
from sqlalchemy import desc

from models import AreaModel


class Map(Resource):
    def get(self):
        maxdate = datetime.now() - timedelta(days=int(environ.get('MAX_RECORD_DAYS')))

        areas = AreaModel.query.order_by(desc(AreaModel.created)).filter(
            AreaModel.created >= maxdate).all()

        areas_coords = []
        areas_list = []

        for area in areas:
            a = area.as_dict()

            if (a['latitude'], a['longitude']) in areas_coords:
                continue

            areas_coords.append((a['latitude'], a['longitude']))
            areas_list.append(area.as_dict())

        return areas_list
