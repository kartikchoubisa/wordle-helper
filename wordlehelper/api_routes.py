from wordlehelper import app, api, logger
from wordlehelper.utils import solve_wordle

from flask_restful import Resource


class Wordle(Resource):
    def get(self):
        return {'hello': 'world'}


api.add_resource(Wordle, '/api')
logger.info("Initialized api")