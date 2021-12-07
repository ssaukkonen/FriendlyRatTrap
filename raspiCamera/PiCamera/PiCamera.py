from classifyImage import ClassifyImage
from cameraCapture import CameraCapture
from apiAccess import APIAccess
#from ultraSensor import UltraSensor
from openCredentials import OpenCredentials
import time


class RunUltraAndCamera:
    def __init__(self, credentials):
        self.credentials = credentials
        #UltraSensorObject = UltraSensor()
        self.classifyImageObject = ClassifyImage()
        self.cameraCaptureObject = CameraCapture(self.classifyImageObject)
        self.APIAccessObject = APIAccess(self.credentials)
      
    def startEverything(self):
        trapActive = True
        while True:
            if trapActive is True:
                trapActive = self.runSensors()
            else:
                print('trapActive is false')
                #trapActive = self.APIAccessObject.get_trapActive_status()
                time.sleep(1)
                break
    
    def runSensors(self):
        while True:
            #ultraSensorResult = UltraSensorObject.distance()
            ultraSensorResult = True
            if ultraSensorResult is True:
                result = self.cameraCaptureObject.captureContinuously()
                if result != 0:
                    sendData = False
                    while sendData is False:
                        sendData = self.APIAccessObject.send_data_to_server(result)
                    return False

def main():
    openCredentialsObject = OpenCredentials('credentials.json')
    credentials = openCredentialsObject.get_credentials()
    RunUltraAndCameraObject = RunUltraAndCamera(credentials)
    RunUltraAndCameraObject.startEverything()     


if __name__ == '__main__':
    main()