from config import *

from flask import Flask, session
from flask_socketio import SocketIO
from flask_wtf.csrf import CSRFProtect, CSRFError
from flask_session import Session
from flask_login import (
	UserMixin,
	login_user,
	LoginManager,
	login_required,
	logout_user,
	current_user,
)
from werkzeug.middleware.proxy_fix import ProxyFix

from app.utils.api import Api

import logging
import string
import random
import datetime

log_format = "%(levelname)s [%(asctime)s] %(name)s  %(message)s"
logging.basicConfig(format=log_format,level=logging.INFO,filename="/sabu/logs/endpoint/sabu.log",filemode="a")
logger = logging.getLogger("sabu.endpoint")
logger_no = logging.getLogger("werkzeug")
logger_no.setLevel(logging.CRITICAL)


# Flask app
app = Flask(__name__)
app.config["SECRET_KEY"] = "".join(
	random.choices(string.ascii_letters + string.digits, k=30)
)

app.config["SESSION_TYPE"] = 'filesystem'
app.config["SESSION_KEY_PREFIX"] = "SABU_session_"
app.config["SESSION_COOKIE_SECURE"] = True
app.config["PERMANENT_SESSION_LIFETIME"] = datetime.timedelta(minutes=5)

# socketio
socketio = SocketIO(app)

# Proxy fix
app.wsgi_app = ProxyFix(app.wsgi_app, x_for=1, x_proto=1)

# Api conf
api = Api(app,SERVER_IP,TOKEN_API,HOSTNAME_ENDPOINT)
api.connect()

# # init login
# login_manager = LoginManager()
# login_manager.init_app(app)
# login_manager.login_view = "login.index"

# Import all views
from app import views
