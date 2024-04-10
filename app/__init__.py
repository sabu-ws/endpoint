from config import *

from flask import Flask
from flask_socketio import SocketIO
from flask_wtf.csrf import CSRFProtect, CSRFError

from app.utils.api import Api

import logging
import string
import random

log_format = "%(levelname)s [%(asctime)s] %(name)s  %(message)s"
logging.basicConfig(format=log_format,level=logging.INFO,filename="/sabu/logs/endpoint/sabu.log",filemode="a")
logger = logging.getLogger("sabu.endpoint")

# Flask app
app = Flask(__name__)
app.config["SECRET_KEY"] = "".join(
	random.choices(string.ascii_letters + string.digits, k=30)
)

# socketio
socketio = SocketIO(app)

api = Api(SERVER_URL,TOKEN_API,HOSTNAME_ENDPOINT)
api.connect()

# Import all views
from app import views
