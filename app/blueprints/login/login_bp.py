from flask import Blueprint, render_template, request, redirect, render_template, session, url_for

from app.forms import LoginForm
from app import api, logger as log
from app.utils.api.function import login_required, already_login


login_bp = Blueprint("login", __name__, template_folder="templates")

@login_bp.route("/",methods=["GET","POST"])
@already_login
def index():
	if request.method == "POST":
		data = dict(request.form)
		form = LoginForm(data=data)
		if form.code.validate(form):
			to_login = api.login(data["username"],data["code"])
			log.info(str(to_login))
			if to_login != None:
				if "message" in to_login:
					if to_login["message"] == "user connected":
						return render_template("login.html", con="ok")
					return render_template("login.html", con="ko")
				else:
					return render_template("login.html", con="ko")
		return render_template("login.html", con="ko")
	return render_template("login.html")

@login_bp.route("/logout",methods=["GET","POST"])
@login_required
def logout():
	out = api.logout()
	log.info(str(out))
	session.pop("username")
	session.pop("name")
	session.pop("firstname")
	session.pop("job")
	return redirect(url_for("login.index"))