from api.views import customer_order
from flask import Flask

import datetime
from flask_jwt_extended import JWTManager


def create_app():
    app = Flask(__name__)
    app.register_blueprint(customer_order.bp)
    app.config['JWT_ACCESS_TOKEN_EXPIRES'] = datetime.timedelta(hours=24)
    app.config['JWT_SECRET_KEY'] = "super_Secret_key"
    jwt = JWTManager(app)

    return app


app = create_app()
