from picamera import PiCamera
from time import sleep
import numpy as np
import matplotlib.pyplot as plt


def numpyCamera():
    while True:
        camera.resolution = (320,240)
        camera.framerate = 3
        output = np.empty((240,320, 3), dtype=np.uint8)
        camera.capture(output, 'rgb')
        print(output)
        plt.imshow(output)
        plt.show()
    

def captureImage():
    camera.resolution = (320,240)
    camera.framerate = 3
    camera.start_preview()
    sleep(2)
    camera.capture('image2.jpg')
    camera.stop_preview()
    
camera = PiCamera()
captureImage()
#numpyCamera()
