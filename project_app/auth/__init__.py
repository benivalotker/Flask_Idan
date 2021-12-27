"""
    local application register
"""
from project_app.auth.user_login import user_login, user_disconnect


def register(app):
    # test_request blueprint
    app.register_blueprint(user_login, url_prefix='/user_login')
    app.register_blueprint(user_disconnect, url_prefix='/user_login')
