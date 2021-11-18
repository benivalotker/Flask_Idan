#!/usr/bin/env python
import project_app
from flask import Flask

app = Flask(__name__)

"""
    to register new app:
        * go to project_app --> __init__.py
        * import the app project and call is register function (from local __init__.py application file).
"""
project_app.register_app(app)

app.run(debug=True)
