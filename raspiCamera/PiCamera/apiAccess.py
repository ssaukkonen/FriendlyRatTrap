import requests
import json
import time


class APIAccess:
    def __init__(self, credentials):
        self.credentials = credentials
        self.url = 'http://' + self.credentials[0] + ':' + self.credentials[1] + '@172.20.241.184/'

    def send_data_to_server(self, result):
        print('Sending picture to server')
        try:
            requests.post(self.url + 'img/', files={'image': result}, timeout=1)
            return True
        except Exception as e:
            print(e)
            time.sleep(10)
            return False
        
    def get_trapActive_status(self):
        try:
            result = requests.get(self.url + 'wait/')
            result = json.loads(result.content)
            result = result['state'][0][0]
            if result == 1:
                print('Reseting trap')
                return True
            else:
                time.sleep(10)
                return False
        except Exception as e:
            print(e)
            time.sleep(10)
            return False
