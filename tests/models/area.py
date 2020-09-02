import unittest

from models import AreaModel


class AreaModelTest(unittest.TestCase):
    def test_as_dict(self):
        data = {
            'aqi': 42,
            'latitude': '50.442',
            'longitude': '30.91'
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
