import config
from flask import Blueprint, request, redirect, render_template

user_login = Blueprint(name='user_login', import_name=__name__, template_folder='templates')
user_disconnect = Blueprint(name='user_disconnect', import_name=__name__, template_folder='templates')


@user_login.route('/', methods=['GET'])
def index():
    title = "Login"
    # body request data
    data = request.json

    # TODO: check the user_name & password from DB
    if data:
        if data.get("user_name") == "beni" and data.get("password") == "A12345":
            # redirect to home page
            return redirect(f"{config.base_url}/home_page/", code=307)
        else:
            return render_template("login/templates.login_page", data={"msg": "Login Error"}, title=title)
    else:
        return render_template("login/login_page.html", data={"msg": "Login Error"}, title=title)


@user_disconnect.route('/user_disconnect', methods=['GET'])
def index():
    # TODO: remove connect session and redirect to login page
    # body request data
    data = request.json

    print("user disconnect")

    return {"operation": "disconnect"}

