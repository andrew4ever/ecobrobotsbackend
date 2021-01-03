from datetime import datetime, timedelta
from os import environ

from flask_restful import Resource
from models import AreaModel, SensorModel, SensorDataModel
from sqlalchemy import desc


class Map(Resource):
    def get(self):
        latest_records = self._get_latest_records()
        aqi_records = []

        for record in latest_records:
            aqi_record = AreaModel.query \
                .order_by(
                    AreaModel.created.desc()
                ).filter_by(
                    latitude=record.latitude
                ).filter_by(
                    longitude=record.longitude
                ).first()

            if aqi_record:
                aqi_records.append(aqi_record.as_dict())

        return aqi_records

    def _get_latest_records(self):
        sensors = SensorModel.query.all()

        latest_records = []
        for sensor in sensors:
            record = SensorDataModel.query.order_by(SensorDataModel.recorded.desc()).filter_by(
                internal_id=sensor.external_id).first()

            if not record:
                continue

            timedelta = datetime.now() - record.recorded
            if (timedelta.seconds // 3600) <= int(environ.get('MAX_RECORD_HOURS')):
                latest_records.append(record)

        return latest_records
