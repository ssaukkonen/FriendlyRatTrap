from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import io
import time
import picamera

from PIL import Image


class CameraCapture:
    def __init__(self, classifyImageObject):
        self.classifyImageObject = classifyImageObject

    def captureContinuously(self):
        with picamera.PiCamera(resolution=(640, 480), framerate=30) as camera:
            camera.start_preview()
            timer_for_capture = time.time()
            try:
                stream = io.BytesIO()
                for _ in camera.capture_continuous(stream, format='jpeg', use_video_port=True):
                    stream.seek(0)
                    image = Image.open(stream).convert('RGB').resize((self.classifyImageObject.width, self.classifyImageObject.height),
                                                                    Image.ANTIALIAS)
                    image2 = Image.open(stream).convert('RGB')
                    results = self.classifyImageObject.classify_image(image)
                    label_id, prob = results[0]
                    stream.seek(0)
                    stream.truncate()
                    if label_id == 0 and prob > 0.6:
                        print('Rat detected and picture taken')
                        return self.get_image_ready_for_sending(image2)
                    if time.time() - timer_for_capture > 10:
                        return 0
            finally:
                camera.stop_preview()
                
    def get_image_ready_for_sending(self, image):
        output = io.BytesIO()
        image.save(output, format='JPEG')
        return output.getvalue()
