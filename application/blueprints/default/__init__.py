from flask import Blueprint

# Import routes
from .default import index

# Register blueprints
bp = Blueprint("default", __name__, template_folder="templates", static_folder="static")

# Index route
index.methods = ["GET"]
bp.add_url_rule("/", view_func=index)

def init_app(app):
    with app.app_context():
        app.register_blueprint(bp, url_prefix="/")