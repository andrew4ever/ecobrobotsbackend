import unittest

from models import SensorValueBreakpointsModel


class SensorValueBreakpointsModelTest(unittest.TestCase):
    def test_as_dict(self):
        data = {
            'sensor_value_type_id': 1,
            'value_min': 0,
            'value_max': 10,
            'aqi_min': 0,
            'aqi_max': 50
        }

        result = SensorValueBreakpointsModel(**data).as_dict()
        del result['id']

        self.assertEqual(result, data)

    def test_repr(self):
        data = {
            'sensor_value_type_id': 1,
            'value_min': 0,
            'value_max': 10,
            'aqi_min': 0,
            'aqi_max': 50
        }

        result = str(SensorValueBreakpointsModel(**data))

        self.assertEqual(result, '<SensorValueBreakpointsModel {}>'.format(
            data['sensor_value_type_id']))
