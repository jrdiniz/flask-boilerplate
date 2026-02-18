from flask import Blueprint

# Import routes
from .webui import index

# Register blueprints
bp = Blueprint("webui", __name__, template_folder="templates", static_folder="static", url_prefix="/")

# Index route
index.methods = ["GET"]
bp.add_url_rule("/", view_func=index)



