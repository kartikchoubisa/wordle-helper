from flask import Flask
import logging
from flask_sqlalchemy import SQLAlchemy
from flask_restful import Api


def create_app():
    # initialize flask app
    app = Flask(__name__)

    # initialize logger and store in app context
    logging.basicConfig(level=logging.INFO)
    logger = logging.getLogger(__name__)
    logger.info("Initialized logger")

    # FUTURE: move this to config file
    app.config['SECRET_KEY'] = 'mysecretcode'
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'

    # we're not using db currently
    # db = SQLAlchemy(app)
    # app.db.init_app(app)

    # initialize flask restful api
    api = Api(app)

    return app, api, logger


app, api, logger = create_app()

from wordlehelper import routes, api_routes
