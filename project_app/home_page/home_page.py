from flask import Blueprint, request, render_template

home_page = Blueprint(name='home_page', import_name=__name__)


@home_page.route('/', methods=['GET'])
def index():
    # body request data
    data = request.json

    # TODO: return html file home_page.html
    return "<h1>Home Page</h1>"
