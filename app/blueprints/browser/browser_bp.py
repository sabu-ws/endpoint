from flask import Blueprint, render_template, redirect, url_for

from app.utils.api.function import login_required

browser_bp = Blueprint("browser", __name__, template_folder="templates")

@browser_bp.route("/")
@login_required
def index():
	return redirect(url_for('browser.browserUsb'))

@browser_bp.route("/usb")
@login_required
def browserUsb():
	return render_template("browser_usb.html")

@browser_bp.route("/server")
@login_required
def browserServer():
	return render_template("browser_server.html")
