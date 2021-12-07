import json

class OpenCredentials:
    def __init__(self, filename):
        self.file = open(filename)
        self.data = json.load(self.file)
     
    def __del__(self):
        self.file.close()

    def get_credentials(self):
        return (self.data['username'], self.data['password'])
