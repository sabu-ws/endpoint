from flask import Blueprint, render_template, redirect

browser_bp = Blueprint("browser", __name__, template_folder="templates")

@browser_bp.route("/")
def index():
	return redirect("/browser/usb")

@browser_bp.route("/usb")
def browserUsb():
	return render_template("browser_usb.html")

@browser_bp.route("/server")
def browserServer():
	return render_template("browser_server.html")
