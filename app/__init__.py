import importlib
# Flask
from flask import Flask

# Extensions
from app.extensions import configurations


def create_app():
    app = Flask(__name__)

    # Initialize Configurations (Bootstrap)
    configurations.init_app(app)

    # Dynamic Extensions Loading
    for extension in app.config.get("EXTENSIONS", []):
        # extension_name = extension.split(".")[-1] # Optional: use for logging
        mod = importlib.import_module(extension)
        mod.init_app(app)

    # Dynamic Blueprints Loading
    for blueprint in app.config.get("BLUEPRINTS", []):
        mod = importlib.import_module(blueprint)
        app.register_blueprint(mod.bp)

    return app
