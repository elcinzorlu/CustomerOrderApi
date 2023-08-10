import datetime

from flask import Flask
from flask_jwt_extended import create_access_token
from flask_jwt_extended import JWTManager



app = Flask(__name__)
app.config["JWT_SECRET_KEY"] = "super-secret"
jwt = JWTManager(app)


def token_authentication(data):
    data_keys_list = ["_id", "date_time"]
    for message_tag in data_keys_list:
        if message_tag not in data:
            print(f"'{message_tag}' tag not in received data")
            return {"Response": KeyError}, 400
    check_password = datetime.datetime.now().strftime('%d.%m.%Y %H')
    if data["date_time"] == check_password:
        access_token = create_access_token(identity=data)
        return access_token, 200
    return "Bad username or password", 400
