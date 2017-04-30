"""
Entry point for app
"""

import os

from flask import Flask

from .directory import directory

from .frontend import frontend

from database import mongo


def create_app(configfile=None):
    """
    Application Factory - see http://flask.pocoo.org/docs/patterns/appfactories/
    """

    app = Flask(__name__)

    # init database
    mongo.init_app(app)

    # Load blueprints
    # http://flask.pocoo.org/docs/0.12/blueprints/

    app.register_blueprint(directory, url_prefix='/directory')
    app.register_blueprint(frontend)

    return app
