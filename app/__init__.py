import os

from flask import Flask
from . import db
from . import pond
from flask_cors import CORS


def create_app(test_config=None):
    #create and configure the app
    app = Flask(__name__, instance_relative_config=True)
    app.config.from_pyfile('settings.cfg', silent=True)
    
    #ensure the instance folder exists
    try:
        os.makedirs(app.instance_path)
    except OSError:
        pass

    db.init_app(app)
    CORS(app)
    app.register_blueprint(pond.bp)

    @app.errorhandler(404)
    def page_not_found(e):
        return "Not Found 404"

    return app
