import os

from flask import Flask
from flask_restful import Api

app = Flask(__name__)
app.config.update(
    SECRET_KEY=os.urandom(24),
    SESSION_COOKIE_SECURE=True,
    SESSION_COOKIE_NAME='ecobrobotsbackend-websession'
)

api = Api(app)
