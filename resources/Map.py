from datetime import datetime, timedelta
from os import environ

from flask_restful import Resource
from models import AreaModel, SensorModel, SensorDataModel
from common.convert_types_to_names import convert_types_to_names
from sqlalchemy import desc


class Map(Resource):
    def get(self):
        aqi_records = []
        sensor_ids = set([sensor.external_id
                          for sensor in SensorModel.query.all()
                          ])
        maxdate = datetime.now() - timedelta(
            hours=int(environ.get('MAX_RECORD_HOURS'))
        )

        for sensor in sensor_ids:
            aqi_record = AreaModel.query \
                .order_by(
                    AreaModel.created.desc()
                ).filter(
                    AreaModel.created >= maxdate
                ).filter_by(
                    sensor_id=sensor
                ).first()

            if aqi_record:
                aqi_records.append(convert_types_to_names(aqi_record))

        return aqi_records
