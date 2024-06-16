from flask import Blueprint, render_template, jsonify, session, request
from flask_socketio import emit

from app import api,logger as log, socketio
from app.utils.api.function import login_required
from app.utils.usb import usb_detect

index_bp = Blueprint("index", __name__, template_folder="templates")

@socketio.on("state_usb",namespace="/usb")
def socket_state_usb():
	while True:
		socketio.sleep(1)
		emit("ret_state_usb",usb_detect())

@index_bp.route("/")
@login_required
def index():
	return render_template("index.html",state_usb=usb_detect())

@index_bp.route("/user")
@login_required
def user():
	info = api.status_user()
	return jsonify(info)