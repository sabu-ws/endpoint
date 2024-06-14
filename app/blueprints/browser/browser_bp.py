from config import *
from flask import Blueprint, render_template, redirect, url_for, abort, flash
import os

from app import api, logger as log
from app.utils.api.function import login_required

browser_bp = Blueprint("browser", __name__, template_folder="templates")

@browser_bp.route("/")
@login_required
def index():
	return redirect(url_for('browser.usb_path'))

@browser_bp.route("/usb/path/<path:MasterListDir>")
@browser_bp.route("/usb/path/")
@login_required
def usb_path(MasterListDir=""):
	joining = os.path.join(DATA_PATH, MasterListDir)
	cur_dir = MasterListDir
	if not os.path.exists(joining):
		abort(404)
	if os.path.isdir(joining):
		new_path = os.listdir(joining)
		list_items = [i for i in os.walk(joining)][0]
		items_dir = list_items[1]
		items_file = list_items[2]
	return render_template("browser_usb.html", items_file=items_file, items_dir=items_dir, cur_dir=cur_dir)

@browser_bp.route("/usb/delete/<path:MasterListDir>")
@browser_bp.route("/usb/delete/")
@login_required
def usb_delete(MasterListDir=""):
	path = os.path.join(DATA_PATH ,MasterListDir)
	master_path = "/".join(path.split("/")[:-1])
	last = MasterListDir.split("/")[-1]
	os.chdir(master_path)
	if os.path.exists(path):
		if os.path.isdir(path):
			for root, dirs, files in os.walk(last, topdown=False):
				for name in files:
					os.remove(os.path.join(root, name))
				for name in dirs:
					os.rmdir(os.path.join(root, name))
			os.rmdir(last)
			return "ok"
		elif os.path.isfile(path):
			os.remove(last) 
			return "ok"
	return redirect(url_for('browser.usb_path'))

@browser_bp.route("/server/path/<path:MasterListDir>")
@browser_bp.route("/server/path/")
@login_required
def server_path(MasterListDir=""):
	ret = api.get_path(MasterListDir)
	if "error" in ret:
		return abort(404)
	info = ret["info"]
	return render_template("browser_server.html",items_file=info["items_file"], items_dir=info["items_dir"], cur_dir=info["cur_dir"])

@browser_bp.route("/server/delete/<path:MasterListDir>")
@browser_bp.route("/server/delete/")
@login_required
def server_delete(MasterListDir=""):
	ret = api.delete_path(MasterListDir)
	if "error" in ret:
		return abort(404)
	else:
		return "ok"

@browser_bp.route("/server/download/<path:MasterListDir>")
@browser_bp.route("/server/download/")
@login_required
def server_download(MasterListDir=""):
	ret = api.download_path(MasterListDir)
	if "error" in ret:
		return abort(404)
	log.info(str(ret))
	flash("Successful download to USB key","good")
	return redirect(url_for("browser.server_path"))