"""
    handle all application register
        * add here new application project
"""
from project_app import auth


def register_app(app):
    """
        register applocation
    """
    auth.register(app)
