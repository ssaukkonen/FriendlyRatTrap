import requests


class APIAccess:
    def __init__(self, credentials):
        self.credentials = credentials
        self.url = 'http://' + self.credentials[0] + ':' + self.credentials[1] + '@172.20.241.184/'

    def send_data_to_server(self, result):
        print('sending')
        try:
            requests.post(self.url + 'img/', files={'image': result}, timeout=1)
            #requests.post(self.url + 'db/', files={'1'})
            return True
        except Exception as e:
            print(e)
            return False
        
    def get_trapActive_status(self):
        result = request.get(self.url + 'db/')
        if result == 1:
            return True
        elif result == 0:
            return False
