from flask import Blueprint, jsonify, request
from registers.service_register import service_register

pathRegister = Blueprint('register', __name__)


@pathRegister.route("/register", methods=["POST"])
def store():
    try:
        email = request.json.get('email')
        name = request.json.get('name')
        service = service_register()
        return jsonify(service.store(email, name)), 202, {'Access-Control-Allow-Origin': '*'}
    except Exception as Argument:
        return jsonify({"message": str(Argument.args[0]), 'error': str(Argument.args[1])
                           , 'code': Argument.args[2]}), Argument.args[2], {'Access-Control-Allow-Origin': '*'}


@pathRegister.route("/register", methods=["GET"])
def all():
    try:
        service = service_register()
        return jsonify(service.getAll()), 200, {'Access-Control-Allow-Origin': '*'}
    except Exception as Argument:
        return jsonify({"message": str(Argument.args[0]), 'error': str(Argument.args[1])
                           , 'code': Argument.args[2]}), Argument.args[2], {'Access-Control-Allow-Origin': '*'}


@pathRegister.route("/register/<id>", methods=["GET"])
def show(id):
    try:
        service = service_register()
        return jsonify(service.show(id)), 200, {'Access-Control-Allow-Origin': '*'}
    except Exception as Argument:
        return jsonify({"message": str(Argument.args[0]), 'error': str(Argument.args[1])
                           , 'code': Argument.args[2]}), Argument.args[2], {'Access-Control-Allow-Origin': '*'}
