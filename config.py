from dotenv import dotenv_values

DOT_ENV = dotenv_values(".env")

HOSTNAME_ENDPOINT = DOT_ENV["HOSTNAME_ENDPOINT"] 
SERVER_URL = DOT_ENV["SERVER_URL"] 
TOKEN_API = DOT_ENV["TOKEN_API"] 