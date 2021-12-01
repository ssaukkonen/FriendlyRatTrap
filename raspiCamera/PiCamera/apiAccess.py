import requests


class APIAccess:
    def __init__(self):
        self.url = 'http://172.20.241.184/'

    def send_data_to_server(self, file):
        requests.post(self.url + 'img/', files=file)
        requests.post(self.url + 'db/', files='1')