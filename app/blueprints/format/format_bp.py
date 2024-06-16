from flask import Blueprint, render_template
from app.utils.usb import usb_detect_wrap

format_bp = Blueprint("format", __name__, template_folder="templates")

@format_bp.route("/")
@usb_detect_wrap
def index():
    return render_template("format.html")