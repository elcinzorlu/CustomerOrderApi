from flask import jsonify, Blueprint, request
from flask_jwt_extended import jwt_required

from api.controllers import token_authentication_controller
from api.controllers.add_customer_order_controller import add_customer_order_controller
from api.controllers.get_customer_order_controller import get_customer_order_controller
from api.controllers.update_customer_order_controller import update_customer_order_controller
from api.controllers.delete_customer_order_controller import delete_customer_order_controller
from api.controllers.token_authentication_controller import token_authentication

bp = Blueprint("customer_order", __name__)


@bp.route('/add_customer_order', methods=['POST'])
@jwt_required()
def add_customer_order():
    data = request.get_json()
    new_customer_order_data = add_customer_order_controller(data)
    return jsonify({'result': new_customer_order_data})


@bp.route('/get_customer_order/<customer_id>', methods=['GET'])
@jwt_required()
def get_customer_order(customer_id):
    response_data = get_customer_order_controller(customer_id)
    return jsonify({'result': response_data})


@bp.route("/update_customer_order/<customer_id>", methods=["PATCH"])
@jwt_required()
def update_customer_order(customer_id):
    data = request.get_json()
    response_data = update_customer_order_controller(customer_id, data)
    return jsonify({'result': response_data})


@bp.route("/delete_customer_order/<customer_id>", methods=["DELETE"])
@jwt_required()
def delete_customer_order(customer_id):
    response_data = delete_customer_order_controller(customer_id)
    return jsonify({'result': response_data})


@bp.route('/token_authentication', methods=["POST"])
def token_authentication():
    data = request.get_json()
    response, http_code = token_authentication_controller.token_authentication(data)
    return jsonify({"Response": response}), http_code

