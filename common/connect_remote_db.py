import mysql.connector


def connect_remote_db(url, user_creds, db_name):
    database = mysql.connector.connect(
        host=url,
        user=user_creds['username'],
        password=user_creds['password'],
        database=db_name
    )

    return database
