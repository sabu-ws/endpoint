import requests
import socketio
from socketio.exceptions import TimeoutError
import logging

log_format = "%(levelname)s [%(asctime)s] %(name)s  %(message)s"
logging.basicConfig(format=log_format,level=logging.INFO,filename="/sabu/logs/endpoint/sabu.log",filemode="a")
log = logging.getLogger("sabu.endpoint.apî")

class Api:
    def __init__(self,server_url,token,hostname):
        self.server_url = server_url
        self.token = token
        self.hostname = hostname
        self.namespace = "/api/v2"
        
        http_session = requests.Session()
        http_session.verify = False
        self.sio = socketio.SimpleClient(http_session=http_session)
    
    def connect(self):
        headers={"X-SABUAPITOKEN":self.token,
                "X-SABUHOSTNAME":self.hostname}
        self.sio.connect(self.server_url,namespace=self.namespace,headers=headers,transports="websocket")
        self.sio.emit("join")

    def get_instance(self):
        return self.sio
    
    def receive(self):
        try:
            event = self.sio.receive(timeout=3)
            callback_event = event[1]
        except TimeoutError:
            return None
        # except Error:
            # return None
        else:
            return callback_event
    
    def login(self,username,password):
        self.sio.emit("set_connection",{"username":username,"password":password})
        return self.receive()