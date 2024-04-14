from flask import Blueprint, render_template

format_bp = Blueprint("format", __name__, template_folder="templates")

@format_bp.route("/")
def index():
    return render_template("format.html")