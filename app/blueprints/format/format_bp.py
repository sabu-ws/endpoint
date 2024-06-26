from config import *
from flask import Blueprint, render_template, flash, redirect, url_for
import subprocess
import os

from app import logger as log, socketio
from flask_socketio import emit
from app.utils.usb import usb_detect_wrap

format_bp = Blueprint("format", __name__, template_folder="templates")

@socketio.on("simple",namespace="/format")
def fomat_simple():
    script = os.path.join(SCRIPT_PATH,"format_standard.sh")  
    log.info("start format standard")
    command = f"sudo /usr/bin/bash {script}"
    process = subprocess.run(command.split())
    log.info("end format standard")
    emit("recv_format")

@socketio.on("advanced",namespace="/format")
def format_advanced():
    script = os.path.join(SCRIPT_PATH,"format_advanced.sh")  
    log.info("start format advanced")
    command = f"sudo /usr/bin/bash {script}"
    process = subprocess.run(command.split())
    log.info("end format advanced")
    emit("recv_format")

@format_bp.route("/simple")
@usb_detect_wrap
def simple():
    return render_template("format.html",type="simple")

@format_bp.route("/advanced")
@usb_detect_wrap
def advanced():
    return render_template("format.html",type="advanced")

@format_bp.route("/end")
@usb_detect_wrap
def end():
    flash("Format completed","good")
    return redirect(url_for("index.index"))