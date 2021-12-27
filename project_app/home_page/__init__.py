"""
    local application register
"""
from project_app.home_page.home_page import home_page


def register(app):
    # test_request blueprint
    app.register_blueprint(home_page, url_prefix='/home_page')
