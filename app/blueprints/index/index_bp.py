from flask import Blueprint, render_template

index_bp = Blueprint("index", __name__, template_folder="templates")

@index_bp.route("/")
def index():
	return render_template("index.html")