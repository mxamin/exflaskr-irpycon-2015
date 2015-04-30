import os
import logging

from flask import Flask, current_app
from flask.ext.sqlalchemy import SQLAlchemy
from flask.ext.bootstrap import Bootstrap

from config import config

db = SQLAlchemy()
bootstrap = Bootstrap()


def create_app(config_name):
    app = Flask(__name__)
    app.config.from_object(config[config_name])
    config[config_name].init_app(app)

    db.init_app(app)
    bootstrap.init_app(app)

    if app.debug:
        logging.basicConfig(level=logging.DEBUG,
                            format='%(name)s[%(funcName)s] %(message)s')
    elif app.testing:
        logging.basicConfig(level=logging.INFO,
                            format='%(message)s')
    else:
        logging.basicConfig(level=logging.ERROR,
                            format='%(name)s: %(message)s')

    from .main import main as main_blueprint
    app.register_blueprint(main_blueprint)

    return app
