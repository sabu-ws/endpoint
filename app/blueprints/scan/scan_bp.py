from app.utils.api.function import login_required

from flask import Blueprint, render_template, request, redirect, url_for
import os
from io import BytesIO
import zipfile
import tempfile

from app import logger as log, api

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

@scan_bp.route("/scan",methods=["POST","GET"])
@login_required
def scan():
	scan_state = api.status_scan()
	if request.method == "POST" and scan_state["state"] == True:
		get_file_name = request.form.getlist("file_info")
		memory_file = BytesIO()
		os.chdir(path_temp_usb)
		with zipfile.ZipFile(memory_file, "w", zipfile.ZIP_DEFLATED) as zipf:
			for items in get_file_name:
				if os.path.exists(items):
					if os.path.isdir(items):
							for root, dirs, files in os.walk(items):
								for file in files:
									zipf.write(os.path.join(root, file))
					elif os.path.isfile(items):
						zipf.write(items)
		memory_file.seek(0)
		result = api.upload_zip(memory_file)
		if "error" in result:
			flash("error to scan")
			return redirect(url_for("scan.path"))
		if "message" in result:
			if result["message"] == "scanning":
				if "state" in result:
					return render_template("scan.html")
	if request.method == "GET" and scan_state["state"] == False:
		info_user = api.status_user()["info"]
		if info_user["scan_state"]:
			return render_template("scan.html")
	return redirect(url_for("scan.path"))

@scan_bp.route("/scan/state")
@login_required
def scan_state():
	scan_state = api.status_scan()
	if scan_state["state"]:
		return {"state":True}
	else:
		return {"state":False}