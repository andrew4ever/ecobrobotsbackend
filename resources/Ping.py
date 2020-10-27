from flask_restful import Resource


class Ping(Resource):
    def get(self):
        return {'code': 200, 'message': 'pong'}, 200
