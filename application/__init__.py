# Flask
from flask import Flask

# Extensions
from application.extensions import configurations

# Blueprints
from application.blueprints import default

def create_app():
    app = Flask(__name__)

    # Initialize Extensions
    configurations.init_app(app)

    # Initialize Blueprints
    default.init_app(app)

    return app