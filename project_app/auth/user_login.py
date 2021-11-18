from flask import Blueprint, request

user_login = Blueprint(name='user_login', import_name=__name__)


@user_login.route('/', methods=['GET'])
def index():
    response = {
        "Request_Methods": "test response",
    }

    return response
