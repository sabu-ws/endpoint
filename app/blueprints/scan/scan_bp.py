from flask import Blueprint, render_template

from app.utils.api.function import login_required

scan_bp = Blueprint("scan", __name__, template_folder="templates")

@scan_bp.route("/")
@login_required
def index():
	return render_template("browser_scan.html")