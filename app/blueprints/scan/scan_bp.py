from flask import Blueprint, render_template
import os

from app.utils.api.function import login_required

scan_bp = Blueprint("scan", __name__, template_folder="templates")

path_temp_usb = "/mnt"
@scan_bp.route("/path/<path:MasterListDir>")
@scan_bp.route("/path/")
@login_required
def path(MasterListDir=""):
	joining = os.path.join(path_temp_usb, MasterListDir)
	cur_dir = MasterListDir
	if not os.path.exists(joining):
		abort(404)
	if os.path.isdir(joining):
		new_path = os.listdir(joining)
		list_items = [i for i in os.walk(joining)][0]
		items_dir = list_items[1]
		items_file = list_items[2]
	return render_template("browser_scan.html", items_file=items_file, items_dir=items_dir, cur_dir=cur_dir)