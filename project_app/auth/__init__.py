"""
    local application register
"""
from project_app.auth.user_login import user_login


def register(app):
    # test_request blueprint
    app.register_blueprint(user_login, url_prefix='/user_login')
