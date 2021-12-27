"""
    handle all application register
        * add here new application project
"""
from project_app import auth, home_page


def register_app(app):
    """
        register applocation
    """
    auth.register(app)
    home_page.register(app)
