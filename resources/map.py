from flask_restful import Resource
from sqlalchemy import desc

from models import AreaModel


class Map(Resource):
    def get(self):
        areas = AreaModel.query.order_by(desc(AreaModel.created)).all()

        areas_coords = []
        areas_list = []

        for area in areas:
            a = area.as_dict()

            if (a['latitude'], a['longitude']) in areas_coords:
                continue

            areas_coords.append((a['latitude'], a['longitude']))
            areas_list.append(area.as_dict())

        return areas_list
