from flask import Blueprint, jsonify, request
from registers.service_register import service_register
from validators.validate import validate

pathRegister = Blueprint('register', __name__)


#
# Clase que maneja las rutas de registro para newsletter
#

@pathRegister.route("/register", methods=["POST"])
def store():
    try:
        check = validate()
        email = check.is_valid_email(request.json.get('email'))
        name = check.sanitize_string(request.json.get('name'))
        service = service_register()
        return jsonify(service.store(email, name)), 202, {'Access-Control-Allow-Origin': 'https://teguio.cl'}
    except Exception as Argument:
        return jsonify({"message": str(Argument.args[0]), 'error': str(Argument.args[1])
                           , 'code': Argument.args[2]}), Argument.args[2], {'Access-Control-Allow-Origin': 'https://teguio.cl'}


@pathRegister.route("/register", methods=["GET"])
def all():
    try:
        service = service_register()
        return jsonify(service.all()), 200, {'Access-Control-Allow-Origin': 'https://teguio.cl'}
    except Exception as Argument:
        return jsonify({"message": str(Argument.args[0]), 'error': str(Argument.args[1])
                           , 'code': Argument.args[2]}), Argument.args[2], {'Access-Control-Allow-Origin': 'https://teguio.cl'}


@pathRegister.route("/register/<id>", methods=["GET"])
def show(id):
    try:
        service = service_register()
        check = validate()
        return jsonify(service.show(check.sanitize_string(id))), 200, {'Access-Control-Allow-Origin': 'https://teguio.cl'}
    except Exception as Argument:
        return jsonify({"message": str(Argument.args[0]), 'error': str(Argument.args[1])
                           , 'code': Argument.args[2]}), Argument.args[2], {'Access-Control-Allow-Origin': 'https://teguio.cl'}
