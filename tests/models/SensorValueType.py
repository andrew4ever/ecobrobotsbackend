import unittest

from models import SensorValueTypeModel


class SensorValueTypeModelTest(unittest.TestCase):
    def test_as_dict(self):
        data = {
            'name': 'co2',
            'type': 'co2',
            'round_digits': 3,
            'max_possible_value': 32,
            'is_in_aqi': 1,
            'calculate_period': 5
        }

        result = SensorValueTypeModel(
            **data).as_dict()
        del result['id']

        self.assertEqual(result, data)

    def test_repr(self):
        data = {
            'name': 'co2',
            'type': 'co2',
            'round_digits': 3,
            'max_possible_value': 32,
            'is_in_aqi': 1,
            'calculate_period': 5
        }

        result = str(SensorValueTypeModel(**data))

        self.assertEqual(
            result, '<SensorValueTypeModel {}>'.format(data['name']))
