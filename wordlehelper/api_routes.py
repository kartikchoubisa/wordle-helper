from wordlehelper import app, api, logger
from wordlehelper.utils.solve_wordle import solve_wordle

from flask import request
from flask_restful import Resource
import json


class Wordle(Resource):

    #must receive a form data with the following keys:
    #gray, green, yellow
    def post(self):
        data = request.form.to_dict()
        logger.info(f"Received post request with data: {data}")
        #TODO: create a central validator for this data, availalabe to both flask-from and flask-restful
        try:
            gray = data["gray"]
            green = data["green"]
            yellow = data["yellow"]
            solutions = solve_wordle(gray, green, yellow) #list of top words
            solutions_dict = {"solutions": solutions}
            logger.info(f"Solutions found successfully: {solutions_dict}")
            return solutions_dict, 200


        except KeyError as e:
            logger.error(f"missing a required field: {e}")
            return {"error": f"missing a required field: {e}"}, 400

        except Exception as e:
            logger.error(f"error while solving wordle: {e}")
            return {"error": str(e)}, 400

api.add_resource(Wordle, '/api/wordle-state-to-words')
logger.info("Initialized api")