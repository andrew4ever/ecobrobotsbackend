import math
from datetime import datetime
from os import environ

from sqlalchemy import desc

from app import create_app
from common import load_config
from models import db
from models import AreaModel, SensorDataModel, SensorValueTypeModel
from models import SensorValueBreakpointsModel as Breakpoints


class AQICalculator:
    def __init__(self, db):
        self.db = db

        self._map_precision = 0.004
        self._map_round_digits = 6
        self._min_index_value = 0
        self._max_index_value = 500
        self._value_types = ['pm25', 'pm100', 'o31', 'o38', 'co', 'so2',
                             'no2', 'temp', 'humi', 'press', 'pm1', 'nh3', 'co2', 'rad', 'sound']
        self._aqi_value_types = ['pm25', 'pm100',
                                 'o31', 'o38', 'co', 'so2', 'no2']

    def calculate_aqi(self):
        sensor_records = SensorDataModel.query.order_by(
            desc(SensorDataModel.recorded)).all()

        records = []
        for record in sensor_records:
            timedelta = datetime.now() - record.recorded

            if timedelta.days <= int(environ.get('MAX_RECORD_DAYS')):
                records.append(record)

        squares = {}
        for record in records:
            center = self.get_dot_center(
                float(record.latitude), float(record.longitude))

            if not squares.get(center):
                squares[center] = []

            squares[center].append(record)

        for center, records in squares.items():
            values = {}

            for record in records:
                for t in self._value_types:
                    val = getattr(record, t)

                    if not values.get(t):
                        values[t] = {
                            'value': 0,
                            'count': 0
                        }

                    values[t]['value'] += float(val)
                    values[t]['count'] += 1

            aqi_global = 0
            values_global = {}

            for t, value in values.items():
                t_data = SensorValueTypeModel.query.filter(
                    SensorValueTypeModel.name == t).first()

                sensor_value = round(
                    value['value'] / value['count'], t_data.round_digits)
                sensor_value = min(sensor_value, float(
                    t_data.max_possible_value))
                values_global[t] = sensor_value

                if t not in self._aqi_value_types:
                    continue

                value_breakpoint = self.get_breakpoints(
                    t_data.id, sensor_value)

                if not value_breakpoint:
                    continue

                a = value_breakpoint.aqi_max - value_breakpoint.aqi_min
                b = sensor_value - value_breakpoint.value_min
                c = value_breakpoint.value_max - value_breakpoint.value_min

                current_value = a * b / c + value_breakpoint.value_min
                aqi_global = max(current_value, aqi_global)

            aqi_global = min(self._max_index_value, aqi_global)
            aqi_global = max(self._min_index_value, aqi_global)

            area = AreaModel(
                latitude=center[0], longitude=center[1], aqi=aqi_global, **values_global)
            self.db.session.add(area)
            self.db.session.commit()

    def get_dot_center(self, lat, lon):
        start_lat = self._map_precision * math.floor(lat / self._map_precision)
        start_lon = self._map_precision * math.floor(lon / self._map_precision)

        return (
            round(start_lat + self._map_precision / 2, self._map_round_digits),
            round(start_lon + self._map_precision / 2, self._map_round_digits)
        )

    def get_breakpoints(self, value_type, sensor_value):
        return Breakpoints.query.filter(Breakpoints.value_min <= sensor_value, Breakpoints.value_max >=
                                        sensor_value, Breakpoints.sensor_value_type_id == value_type).first()


if __name__ == '__main__':
    load_config()
    app = create_app()
    app.app_context().push()

    calc = AQICalculator(db)
    result = calc.calculate_aqi()
