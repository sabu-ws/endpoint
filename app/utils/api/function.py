from flask import redirect, url_for, session
from app import api
from functools import wraps

def login_required(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        get_status = api.status_user()
        if get_status != None:
            if "message" in get_status:
                if get_status["message"] == "connected":
                    for i in api.status_user()["info"]:
                        session[i] = api.status_user()["info"][i]
                    return f(*args, **kwargs)
                else:
                    return redirect(url_for("login.index"))
            else:
                return redirect(url_for("login.index"))
        else:
            return redirect(url_for("login.index"))
    return decorated_function

def already_login(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        get_status = api.status_user()
        if get_status != None:
            if "message" in get_status:
                if get_status["message"] == "connected":
                    return redirect(url_for("index.index"))
                else:
                    for i in api.status_user()["info"]:
                        session[i] = api.status_user()["info"][i]
                    return f(*args, **kwargs)
            else:
                return redirect(url_for("index.index"))
        else:
            return redirect(url_for("index.index"))
    return decorated_function
