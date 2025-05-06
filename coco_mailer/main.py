import requests
import os
from errors import CocoError


# * ENV [COCO_SECRET]

class Client:
    url:str = 'http://127.0.0.1:8000'
    client_secret:str

    def __init__(self,client_secret = None, url = None,):
        if url:
            self.url = url

        if not client_secret:
            # check environmental variablesincase it was set there
            if os.getenv("COCO_SECRET",None):
                self.client_secret = os.getenv("COCO_SECRET")
            else:
                raise CocoError('Client Secret was not set \nYou can set it via the Environmetal variables as [COCO_SECRET] or in the Coco client class during initialization.')
        else:
            self.client_secret = client_secret

    def send_mail()->tuple[bool ,str]:...