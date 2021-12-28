import config
from services import mondodb_manager
from flask import Blueprint, request, redirect, render_template

user_login = Blueprint(name='user_login', import_name=__name__, template_folder='templates')
user_disconnect = Blueprint(name='user_disconnect', import_name=__name__, template_folder='templates')


@user_login.route('/', methods=['GET', 'POST'])
def index():
    title = "Login"
    message = ''

    # if the data came from the "form_login"
    if request.method == 'POST':
        # read user and pass from mongodb
        user_name = request.form.get('user_name')
        password = request.form.get('password')

        # get password from mongodb
        login_res = mondodb_manager.get_data("login", {"user_name": user_name, "password": password})

        if login_res:
            if login_res.get("password") == password:
                # redirect to home page
                return redirect(f"{config.base_url}/home_page/", code=307)
            else:
                message = {"msg": "Login Error"}
        else:
            message = {"msg": "Login Error"}

    return render_template("login/login_page.html", message=message, title=title)


@user_disconnect.route('/user_disconnect', methods=['GET'])
def index():
    # TODO: remove connect session and redirect to login page
    # body request data
    data = request.json

    print("user disconnect")

    return {"operation": "disconnect"}
