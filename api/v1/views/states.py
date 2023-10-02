#!/usr/bin/python3
"""holds State module"""
from models import storage
from models.state import State
from api.v1.views import app_views
from flasgger.utils import swag_from
from flask import jsonify, abort, request, make_response


@app_views.route('/states', methods=['GET'], strict_slashes=False)

@swag_from('documentation/state/get.yml', methods=['GET'])

def get_all():
    """read all by identifier"""
    all_list = [obj.to_dict() for obj in storage.all(State).values()]
    return jsonify(all_list)


@app_views.route('/states/<string:state_id>', methods=['GET'],
                 strict_slashes=False)

@swag_from('documentation/state/get_id.yml', methods=['GET'])

def get_method_state(state_id):
    """reads state by identifier"""
    state = storage.get(State, state_id)
    if state is None:
        abort(404)
    return jsonify(state.to_dict())


@app_views.route('/states/<string:state_id>', methods=['DELETE'],
                 strict_slashes=False)

@swag_from('documentation/state/delete.yml', methods=['DELETE'])

def del_method(state_id):
    """to remove state by identifier"""
    state = storage.get(State, state_id)
    if state is None:
        abort(404)
    state.delete()
    storage.save()
    return jsonify({})


@app_views.route('/states/', methods=['POST'],
                 strict_slashes=False)
@swag_from('documentation/state/post.yml', methods=['POST'])
def create_obj():
    """does creating of new instance"""
    if not request.get_json():
        return make_response(jsonify({"error": "Not a JSON"}), 400)
    if 'name' not in request.get_json():
        return make_response(jsonify({"error": "Missing name"}), 400)
    js = request.get_json()
    obj = State(**js)
    obj.save()
    return jsonify(obj.to_dict()), 201


@app_views.route('/states/<string:state_id>', methods=['PUT'],
                 strict_slashes=False)

@swag_from('documentation/state/put.yml', methods=['PUT'])

def post_method(state_id):
    """update"""
    if not request.get_json():
        return make_response(jsonify({"error": "Not a JSON"}), 400)
    obj = storage.get(State, state_id)
    if obj is None:
        abort(404)
    for key, value in request.get_json().items():
        if key not in ['id', 'created_at', 'updated']:
            setattr(obj, key, value)
    storage.save()
    return jsonify(obj.to_dict())
