from flask import Blueprint, render_template, jsonify, session, request

from app import api,logger as log
from app.utils.api.function import login_required

index_bp = Blueprint("index", __name__, template_folder="templates")

@index_bp.route("/")
@login_required
def index():
	return render_template("index.html")

@index_bp.route("/user")
@login_required
def user():
	info = api.status_user()
	return jsonify(info)

@index_bp.route("/test")
def test():
	return api.test()