import unittest

from models import AreaModel


class AreaModelTest(unittest.TestCase):
    def test_as_dict(self):
        data = {
            'aqi': 42,
            'sensor_id': '123456789',
            'co': None,
            'co2': None,
            'humi': None,
            'latitude': '50.442',
            'longitude': '30.91',
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

        result = AreaModel(**data).as_dict()
        del result['created']
        del result['id']

        self.assertEqual(result, data)

    def test_string_coords(self):
        data = {
            'aqi': 42,
            'latitude': '50.442',
            'longitude': '30.91'
        }

        result = AreaModel(**data).string_coords()

        self.assertEqual(result, self.string_coords(data))

    def test_repr(self):
        data = {
            'aqi': 42,
            'latitude': '50.442',
            'longitude': '30.91'
        }

        result = str(AreaModel(**data))

        self.assertEqual(result, '<Area {}>'.format(self.string_coords(data)))

    def string_coords(self, data):
        return data['latitude'] + '-' + data['longitude']
