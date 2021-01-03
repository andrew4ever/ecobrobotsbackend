from datetime import datetime, timedelta
from os import environ

from flask_restful import Resource
from models import AreaModel, SensorModel, SensorDataModel
from common.convert_types_to_names import convert_types_to_names
from sqlalchemy import desc


class Map(Resource):
    def get(self):
        aqi_records = []
        latest_records = self._get_latest_records()
        maxdate = datetime.now() - timedelta(
            hours=int(environ.get('MAX_RECORD_HOURS'))
        )

        for record in latest_records:
            aqi_record = AreaModel.query \
                .order_by(
                    AreaModel.created.desc()
                ).filter(
                    AreaModel.created >= maxdate
                ).filter_by(
                    latitude=record.latitude
                ).filter_by(
                    longitude=record.longitude
                ).first()

            if aqi_record:
                aqi_records.append(convert_types_to_names(aqi_record))

        return aqi_records

    def _get_latest_records(self):
        sensors = SensorModel.query.all()

        latest_records = []
        for sensor in sensors:
            record = SensorDataModel.query.order_by(SensorDataModel.recorded.desc()).filter_by(
                internal_id=sensor.external_id).first()

            if record:
                latest_records.append(record)

        return latest_records
