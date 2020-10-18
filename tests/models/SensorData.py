import unittest

from models import SensorDataModel


class SensorDataModelTest(unittest.TestCase):
    def test_as_dict(self):
        data = {
            'latitude': '50.442',
            'longitude': '30.91',
            'altitude': None,
            'co': None,
            'co2': None,
            'humi': None,
            'nh3': None,
            'no2': None,
            'o31': None,
            'o38': None,
            'pm1': None,
            'pm100': None,
            'pm25': None,
            'press': None,
            'rad': None,
            'so2': None,
            'sound': None,
            'temp': None
        }

        result = SensorDataModel(**data).as_dict()
        del result['id']
        del result['internal_id']
        del result['recorded']

        self.assertEqual(result, data)

    def test_string_coords(self):
        data = {
            'latitude': '50.442',
            'longitude': '30.91'
        }

        result = SensorDataModel(**data).string_coords()

        self.assertEqual(result, self.string_coords(data))

    def test_repr(self):
        data = {
            'latitude': '50.442',
            'longitude': '30.91'
        }

        result = str(SensorDataModel(**data))

        self.assertEqual(result, '<SensorData {}>'.format(
            self.string_coords(data)))

    def string_coords(self, data):
        return data['latitude'] + '-' + data['longitude']
