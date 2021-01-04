import math
from datetime import datetime
from os import environ

from app import create_app, db
from common import load_config
from models import AreaModel, SensorDataModel, SensorModel
from models import SensorValueBreakpointsModel as Breakpoints
from models import SensorValueTypeModel


class AQICalculator:
    def __init__(self, db):
        self.db = db

        self._min_index_value = 0
        self._max_index_value = 500
        self._value_types = ['pm25', 'pm100', 'o31', 'o38', 'co', 'so2',
                             'no2', 'temp', 'humi', 'press', 'pm1', 'nh3', 'co2', 'rad', 'sound']
        self._aqi_value_types = ['pm25', 'pm100',
                                 'o31', 'o38', 'co', 'so2', 'no2']

    def execute(self):
        latest_records = self.get_latest_records()

        for record in latest_records:
            if not record:
                continue

            record_aqi = 0
            values = self.check_record_limits(record)

            for value_type, value in values.items():
                current_aqi = self.calculate_aqi(value_type, value)

                if current_aqi is False:
                    continue

                if isinstance(value_type, SensorValueTypeModel) \
                        and value_type.type in self._aqi_value_types:
                    record_aqi = round(max(current_aqi, record_aqi), 3)
                    values[value_type] = round(current_aqi, 3)
                    # save AQI value for values used in AQI

            record_aqi = min(self._max_index_value, record_aqi)
            record_aqi = max(self._min_index_value, record_aqi)

            self.save_area_data(record_aqi, values, record.internal_id)

    def get_latest_records(self):
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

    def check_record_limits(self, record):
        values = record.as_dict()
        result = {}

        for value_type in self._value_types:
            type_data = SensorValueTypeModel.query.filter(
                SensorValueTypeModel.type == value_type).first()

            if values.get(value_type, None):
                value_float = float(values[value_type])
                result[type_data] = min(
                    value_float,
                    float(type_data.max_possible_value)
                ) if not math.isnan(value_float) else None

        result['latitude'] = values['latitude']
        result['longitude'] = values['longitude']
        return result

    def calculate_aqi(self, value_type, value):
        if not isinstance(value_type, SensorValueTypeModel)\
                or not value_type.type in self._value_types:
            return False

        if value is None \
                or math.isnan(value):
            return False

        value_breakpoint = self.get_breakpoints(
            value_type.id, value)

        if not value_breakpoint:
            return False

        a = value_breakpoint.aqi_max - value_breakpoint.aqi_min
        b = float(value) - value_breakpoint.value_min
        c = value_breakpoint.value_max - value_breakpoint.value_min

        current_value = a * b / c + value_breakpoint.value_min
        return current_value

    def get_breakpoints(self, value_type, sensor_value):
        return Breakpoints.query.filter(
            Breakpoints.value_min <= sensor_value,
            Breakpoints.value_max >= sensor_value,
            Breakpoints.sensor_value_type_id == value_type
        ).first()

    def save_area_data(self, record_aqi, values, sensor_id):
        v = {}
        for key in values:
            if not isinstance(key, str):
                v[key.type] = values[key]
            else:
                v[key] = values[key]

        area = AreaModel(
            aqi=record_aqi,
            sensor_id=sensor_id,
            **v
        )
        self.db.session.add(area)
        self.db.session.commit()


if __name__ == '__main__':
    load_config()
    app = create_app()
    app.app_context().push()

    calc = AQICalculator(db)
    result = calc.execute()
