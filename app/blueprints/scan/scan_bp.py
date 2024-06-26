from config import *
from app.utils.api.function import login_required
from app.utils.usb import usb_detect_wrap, usb_get_name

from flask import Blueprint, render_template, request, redirect, url_for, flash, session
import os
from io import BytesIO
import zipfile
import tempfile

from app import logger as log, api

scan_bp = Blueprint("scan", __name__, template_folder="templates")

@scan_bp.route("/")
@usb_detect_wrap
def index():
	return redirect(url_for("scan.path"))

@scan_bp.route("/path/<path:MasterListDir>")
@scan_bp.route("/path/")
@login_required
@usb_detect_wrap
def path(MasterListDir=""):
	name_usb = usb_get_name()
	joining = os.path.join(DATA_PATH, MasterListDir)
	cur_dir = MasterListDir
	if not os.path.exists(joining):
		abort(404)
	if os.path.isdir(joining):
		new_path = os.listdir(joining)
		list_items = [i for i in os.walk(joining)][0]
		items_dir = list_items[1]
		items_file = list_items[2]
	
	scan_info = api.last_scan_info()
	if "message" in scan_info and scan_info["message"] == "result_scan":
		if scan_info["result"] != "":
			session["scan_result"] = api.last_scan_info()["result"]
	return render_template("browser_scan.html", items_file=items_file, items_dir=items_dir, cur_dir=cur_dir,usb_name=name_usb)

@scan_bp.route("/scan",methods=["POST","GET"])
@login_required
@usb_detect_wrap
def scan():
	scan_state = api.status_scan()
	if request.method == "POST" and scan_state["state"] == True:
		get_file_name = request.form.getlist("file_info")
		memory_file = BytesIO()
		os.chdir(DATA_PATH)
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
			flash("Error to scan","error")
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
@usb_detect_wrap
def scan_state():
	scan_state = api.status_scan()
	if scan_state["state"]:
		flash("Scan completed","good")
		return {"state":True}
	else:
		return {"state":False}