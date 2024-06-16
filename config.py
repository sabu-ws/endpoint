from dotenv import dotenv_values

DOT_ENV = dotenv_values(".env")

HOSTNAME_ENDPOINT = DOT_ENV["HOSTNAME_ENDPOINT"] 
SERVER_IP = DOT_ENV["SERVER_IP"] 
TOKEN_API = DOT_ENV["TOKEN_API"]

MAX_CONTENT_LENGTH = 5 * 1024 * 1024 * 1024

DATA_PATH = "/mnt/usb"