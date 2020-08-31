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
