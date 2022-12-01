import os
import json

from flask import Flask, render_template, jsonify, request
from .db import get_ponds, get_pond, insert_pond, update_pond
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
        return "Hello World"

    @app.get('/pond')
    def pond():
      data = get_ponds({})
      data = dumps(data)
      return json.loads(data)

    @app.get('/pond/<id>')
    def pond_id(id):
      filter = {'_id' : id}
      data = get_pond(filter)   
      data = dumps(data)
      return json.loads(data)

    @app.post('/pond')
    def add_pond():
        name = request.json['name']
        shape = request.json['shape']
        material = request.json['material']
        location = request.json['location']
        # id = request.form['id']
        # length = request.form['length']
        # width = request.form['width']
        # height = request.form['height']
        # diameter = request.form['diameter']
        data = {
            "name" : name,
            "shape_id" : shape,
            "material_id" : material,
            "location" : location,
            # "id" : id,
            # "length" : length,
            # "width" : width,
            # "height" : height,
            # "diameter" : diameter,
        }
        print(data)
        row = insert_pond(data)
        if (row > 0):
            data = {
                "message" : "success",
            }
            response = app.response_class(
                response=json.dumps(data),
                status=201,
                mimetype='application/json'
            )
            return response
        data = {
            "message" : "Failed",
        }
        response = app.response_class(
            response=json.dumps(data),
            status=200,
            mimetype='application/json'
        )
        return response
    
    @app.put('/pond/<id>')
    def edit_pond():
        filter = {'_id' : id}
        
        name = request.json['name']
        shape = request.json['shape']
        material = request.json['material']
        location = request.json['location']
        id = request.form['id']
        length = request.form['length']
        width = request.form['width']
        height = request.form['height']
        diameter = request.form['diameter']
        data = {
            "name" : name,
            "shape_id" : shape,
            "material_id" : material,
            "location" : location,
            "id" : id,
            "length" : length,
            "width" : width,
            "height" : height,
            "diameter" : diameter,
        }
        print(data)
        row = update_pond(filter, data)
        if (row > 0):
            data = {
                "message" : "success",
            }
            response = app.response_class(
                response=json.dumps(data),
                status=201,
                mimetype='application/json'
            )
            return response
        data = {
            "message" : "Failed",
        }
        response = app.response_class(
            response=json.dumps(data),
            status=200,
            mimetype='application/json'
        )
        return response

    @app.errorhandler(404)
    def page_not_found(e):
        return "kosong"

    return app
