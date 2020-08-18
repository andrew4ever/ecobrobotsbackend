import math


class AQICalculator:
    def __init__(self, db):
        self.db = db
        self.cursor = db.cursor(buffered=True)

        self._map_precision = 0.004
        self._map_round_digits = 6

    def calculate_aqi(self):
        self.cursor.execute("SELECT * FROM `sensor`")
        sensors = self.cursor.fetchall()

        records = []
        for sensor in sensors:
            if sensor[2] == 0:
                continue

            self.cursor.execute(
                "SELECT * FROM `sensor_record` WHERE `sensor_id` = {}".format(
                    sensor[0])
            )
            record = self.cursor.fetchone()

            if record:
                records.append(record)

        squares = {}
        for record in records:
            square_center = self.get_dot_center(record[3], record[4])

            if not squares[square_center]:
                squares[square_center]['records'] = []

            squares[square_center]['records'].append(record)

    def get_dot_center(self, lat, lon):
        start_lat = self._map_precision * math.floor(lat / self._map_precision)
        start_lon = self._map_precision * math.floor(lon / self._map_precision)

        return (
            round(start_lat + self._map_precision / 2, self._map_round_digits),
            round(start_lon + self._map_precision / 2, self._map_round_digits)
        )
