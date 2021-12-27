import config
from flask import Blueprint, request, redirect

user_login = Blueprint(name='user_login', import_name=__name__)


@user_login.route('/', methods=['GET'])
def index():
    # body request data
    data = request.json

    # TODO: check the user_name & password from DB
    if data:
        if data.get("user_name") == "beni" and data.get("password") == "A12345":
            # redirect to home page
            return redirect(f"{config.base_url}/home_page/", code=307)
        else:
            # TODO: print the message in the html file
            return "<h1>login failed</h1>"
    else:
        # TODO: print the message in the html file
        return "<h1>login failed</h1>"
