import config
from services import mondodb_manager
from flask import Blueprint, request, redirect, render_template

user_login = Blueprint(name='user_login', import_name=__name__, template_folder='templates')
user_disconnect = Blueprint(name='user_disconnect', import_name=__name__, template_folder='templates')


@user_login.route('/', methods=['GET'])
def index():
    title = "Login"
    # body request data
    data = request.json

    # TODO: get user_name from html form
    # get password from mongodb
    login_res = mondodb_manager.get_data("login", {"user_name": "beni"})
    print(login_res)
    if login_res:
        # TODO: get password from html form
        if login_res.get("password") == "A12345":
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
