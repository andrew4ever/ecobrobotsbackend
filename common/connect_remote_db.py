import mysql.connector


def connect_remote_db(db_data):
    database = mysql.connector.connect(**db_data)

    return database
