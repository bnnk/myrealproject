import logging

from flask import Flask, request as req
from .extensions import db, lm, mbox

from app.controllers import pages


def create_app(config_filename):
    app = Flask(__name__)
    db.init_app(app)
    lm.init_app(app)
    mbox.init_app(app)
    app.config["MONGODB_SETTINGS"] = {
        'db': 'pyfoxardb'
    }
    app.config.from_object(config_filename)

    app.register_blueprint(pages.blueprint)

    app.logger.setLevel(logging.NOTSET)

    @app.after_request
    def log_response(resp):
        app.logger.info("{} {} {}\n{}".format(
            req.method, req.url, req.data, resp)
        )
        return resp

    return app
