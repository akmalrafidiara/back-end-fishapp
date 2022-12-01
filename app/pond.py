import json
from flask import(
    Blueprint, request
)
from .db import get_ponds, get_pond, insert_pond, update_pond
from bson.json_util import dumps
from bson.objectid import ObjectId

bp = Blueprint('pond', __name__, url_prefix='/')

@bp.route('/index')
@bp.route('/')
def index():
    return "Hello World"

@bp.get('/pond')
def pond():
  data = get_ponds({})
  data = dumps(data)
  return json.loads(data)

@bp.get('/pond/<id>')
def pond_id(id):
  ObjInstance = ObjectId(id)
  filter = {'_id':ObjInstance}
  data = get_pond(filter)   
  data = dumps(data)
  return json.loads(data)
#   data = json.loads(data)
#   return data['_id']['$oid']

@bp.post('/pond')
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

@bp.put('/pond/<id>')
def edit_pond():
    ObjInstance = ObjectId(id)
    filter = {'_id':ObjInstance}
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