from classifyImage import ClassifyImage
from cameraCapture import CameraCapture
from apiAccess import APIAccess
from ultraSensor import UltraSensor

def main():
  #open cred
  UltraSensorObject = UltraSensor()
  classifyImageObject = ClassifyImage()
  cameraCaptureObject = CameraCapture(classifyImageObject)
  APIAccessObject = APIAccess()
  while True:
    ultraSensorResult = UltraSensorObject.distance()
    if ultraSensorResult is True:
        result = cameraCaptureObject.captureContinuously()
        if result != 0:
          APIAccessObject.send_data_to_server(result)


if __name__ == '__main__':
  main()