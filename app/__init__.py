import os
import json

from flask import Flask, render_template, jsonify, request
from .db import get_ponds, get_pond
from bson.json_util import dumps
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

    @app.route('/index')
    @app.route('/')
    def index():
        return "Hello Statics"

    @app.get('/pond')
    def pond():
      data = get_ponds({})
      data = dumps(data)
      return json.loads(data)

    @app.get('/pond/<id>')
    def pond_id(id):
      filter = {'id' : id}
      data = get_pond(filter)   
      data = dumps(data)
      return json.loads(data)

    @app.post('/pond')
    def insert_pond():
        name = request.form['name']
        shape = request.form['shape']
        material = request.form['material']
        length = request.form['length']
        width = request.form['width']
        id = request.form['id']
        location = request.form['location']
        diameter = request.form['diameter']
        data = {
            "name" : name,
            "shape" : shape,
            "material" : material,
            "length" : length,
            "width" : width,
            "id" : id,
            "location" : location,
            "diameter" : diameter,
        }
        row = insert_pond(data)
        if (row > 0):
            return True
        return False

    @app.errorhandler(404)
    def page_not_found(e):
        return "kosong"

    return app
