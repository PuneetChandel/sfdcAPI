from flask import request, Response, Flask,Blueprint,jsonify
from models.sfobject.sfobject import sfobject

# flask app
app = Flask(__name__)
sfobject_blueprint = Blueprint('sfobject', __name__)

@sfobject_blueprint.route('/v1/sfobject', methods=['POST'])
def createObject():
    if not request.json:
        resp = Response(status=400)
        return resp

    if request.headers.get('x-object-name') == None:
        resp = jsonify(
            {"success": False,
             "message": "Object Header is missing please add x-object-name"
             })
        resp.status_code = 400
        return resp

    return sfobject.createsfobj(request.json,request.headers.get('x-object-name'))

@sfobject_blueprint.route('/v1/sfobject/<id>', methods=['GET'])
def getObject(id):
    if request.headers.get('x-object-name') == None:
        resp = jsonify(
            {"success": False,
             "message": "Object Header is missing please add x-object-name"
             })
        resp.status_code = 400
        return resp

    return sfobject.getobj(id,request.headers.get('x-object-name'))

@sfobject_blueprint.route('/v1/sfobject/<id>', methods=['PATCH'])
def updateObject(id):

    if request.headers.get('x-object-name') == None:
        resp = jsonify(
            {"success": False,
             "message": "Object Header is missing please add x-object-name"
             })
        resp.status_code = 400
        return resp
    return sfobject.updateobj(request.json,id,request.headers.get('x-object-name'))

