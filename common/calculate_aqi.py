from connect_remote_db import connect_remote_db


def calculate_aqi(db_data):
    db = connect_remote_db(db_data)

    cursor = db.cursor(buffered=True)
    cursor.execute("SELECT * FROM `sensor`")
    sensors = cursor.fetchall()

    records = []
    for sensor in sensors:
        if sensor[2] == 0:
            continue

        cursor.execute(
            "SELECT * FROM `sensor_record` WHERE `sensor_id` = {}".format(
                sensor[0])
        )
        record = cursor.fetchone()

        if record:
            records.append(record)
