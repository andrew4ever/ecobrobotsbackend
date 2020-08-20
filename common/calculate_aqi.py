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

        # get latest records
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

        # arrange records to squares
        squares = {}
        for record in records:
            square_center = self.get_dot_center(record[3], record[4])

            if not squares.get(square_center, None):
                squares[square_center] = []

            squares[square_center].append(record)

        # get aqi for each square
        for center, records in squares.items():
            # prepare dataset
            sensor_values = {}
            for record in records:
                self.cursor.execute(
                    "SELECT * FROM `sensor_value` WHERE `record_id` = {}".format(record[0]))
                values = self.cursor.fetchall()

                self.cursor.execute("SELECT * FROM `sensor_value_type`")
                types = self.cursor.fetchall()
                used_ids = [value_type[0]
                            for value_type in types if value_type[-2] == 1]
                types = {value_type[0]: value_type for value_type in types}

                for value in values:
                    if value[2] not in used_ids:
                        continue

                    if not sensor_values.get(value[2], None):
                        sensor_values[value[2]] = {
                            'type': value[2],
                            'value': 0,
                            'count': 0
                        }

                    sensor_values[value[2]]['value'] += value[3]
                    sensor_values[value[2]]['count'] += 1

            for value_type, value in sensor_values.items():
                sensor_value = round(
                    value['value'] / value['count'], types[value_type][3])
                sensor_value = min(sensor_value, types[value_type][4])

    def get_dot_center(self, lat, lon):
        start_lat = self._map_precision * math.floor(lat / self._map_precision)
        start_lon = self._map_precision * math.floor(lon / self._map_precision)

        return (
            round(start_lat + self._map_precision / 2, self._map_round_digits),
            round(start_lon + self._map_precision / 2, self._map_round_digits)
        )
