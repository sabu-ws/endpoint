from flask import Blueprint, render_template, redirect, url_for
import os

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
	path_temp_usb = "/mnt"
	joining = os.path.join(path_temp_usb, MasterListDir)
	cur_dir = MasterListDir
	if not os.path.exists(joining):
		abort(404)
	if os.path.isdir(joining):
		new_path = os.listdir(joining)
		list_items = [i for i in os.walk(joining)][0]
		items_dir = list_items[1]
		items_file = list_items[2]
	return render_template("browser_usb.html", items_file=items_file, items_dir=items_dir, cur_dir=cur_dir)

@browser_bp.route("/usb/delete")
@login_required
def usb_delete():
	return redirect(url_for('browser.usb_path'))

@browser_bp.route("/server")
@login_required
def server_path():
	return render_template("browser_server.html")
