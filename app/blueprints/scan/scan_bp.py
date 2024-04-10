from flask import Blueprint

scan_bp = Blueprint("scan", __name__, template_folder="templates")

@scan_bp.route("/")
def index():
	return "scan page"