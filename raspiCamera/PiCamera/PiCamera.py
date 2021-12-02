from classifyImage import ClassifyImage
from cameraCapture import CameraCapture
from apiAccess import APIAccess
#from ultraSensor import UltraSensor

class RunUltraAndCamera:
    def __init__(self):
        #UltraSensorObject = UltraSensor()
        self.classifyImageObject = ClassifyImage()
        self.cameraCaptureObject = CameraCapture(self.classifyImageObject)
        self.APIAccessObject = APIAccess()  
      
    def runEverything(self):
        while True:
            #ultraSensorResult = UltraSensorObject.distance()
            ultraSensorResult = True
            if ultraSensorResult is True:
                result = self.cameraCaptureObject.captureContinuously()
                if result != 0:
                    self.APIAccessObject.send_data_to_server(result)
                    return False

def main():
    #open cred
    RunUltraAndCameraObject = RunUltraAndCamera()
    trapActive = True
    while True:
        if trapActive is True:
            trapActive = RunUltraAndCameraObject.runEverything()
        else:
            print('trapActive is false')
            break        


if __name__ == '__main__':
    main()