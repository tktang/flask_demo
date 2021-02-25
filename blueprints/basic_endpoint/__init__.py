from flask import Blueprint, request

blueprint = Blueprint('api', __name__, url_prefix='/basic_api')


@blueprint.route('/hello_world')
def hello_world():
    return {'message': 'Hello World!'}


@blueprint.route('/entities', methods=['GET', 'POST'])
def get_users():
    if request.method == "GET":
        return {'message': 'This endpoint should return a list of entities', 'method': request.method}
    if request.method == "POST":
        return {'message': 'This endpoint should create an entity', 'method': request.method}


@blueprint.route('/entities/<int:user_id>', methods=['GET', 'PUT', 'DELETE'])
def get_user(user_id):
    if request.method == "GET":
        return {'message': 'This endpoint should return the entity {} details'.format(user_id), 'method': request.method}
    if request.method == "PUT":
        return {'message': 'This endpoint should update the entity {}'.format(user_id), 'method': request.method}
    if request.method == "DELETE":
        return {'message': 'This endpoint should delete the entity {}'.format(user_id), 'method': request.method}
