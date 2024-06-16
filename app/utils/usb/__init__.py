from functools import wraps
import re
import os
from pyudev import Context, Devices

from flask import redirect, url_for

from app import app

def usb_detect_wrap(f):
	@wraps(f)
	def decorated_function(*args, **kwargs):
		context = Context()
		try:
		  sda = Devices.from_name(context, 'block', 'sda')
		except:
		  sda = None
		if sda == None:
			return redirect(url_for("index.index"))
		else:
			return f(*args, **kwargs)
	return decorated_function

def usb_detect():
	context = Context()
	try:
		sda = Devices.from_name(context, 'block', 'sda')
	except:
		sda = None
	if sda == None:
		return False
	else:
		return True

def usb_get_name():
	context = Context()
	if usb_detect():
		sda = Devices.from_name(context, 'block', 'sda')
		return str(sda.get("ID_MODEL"))
	else:
		return None