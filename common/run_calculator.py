from datetime import datetime
from os import environ

from AQICalculator import AQICalculator, connect_remote_db
from load_config import load_config

load_config()

DATABASE_HOST = environ.get('DATABASE_HOST')
DATABASE = environ.get('DATABASE')
USERNAME = environ.get('USERNAME')
PASSWORD = environ.get('PASSWORD')

db_data = {
    'host': DATABASE_HOST,
    'database': DATABASE,
    'user': USERNAME,
    'password': PASSWORD
}

db = connect_remote_db(db_data)
calc = AQICalculator(db)
results = calc.calculate_aqi()

DATABASE_HOST = environ.get('DATABASE_HOST_NEW')
DATABASE = environ.get('DATABASE_NEW')
USERNAME = environ.get('USERNAME_NEW')
PASSWORD = environ.get('PASSWORD_NEW')

db_data = {
    'host': DATABASE_HOST,
    'database': DATABASE,
    'user': USERNAME,
    'password': PASSWORD
}

db = connect_remote_db(db_data)
cursor = db.cursor(buffered=True)

for center, aqi in results.items():
    add_records = ("INSERT INTO `aqi_records` "
                   "(aqi, latitude, longitude, created) "
                   "VALUES (%s, %s, %s, %s)")

    data = (aqi, str(center[0]), str(center[1]), datetime.now())

    cursor.execute(add_records, data)

db.commit()

cursor.close()
db.close()
