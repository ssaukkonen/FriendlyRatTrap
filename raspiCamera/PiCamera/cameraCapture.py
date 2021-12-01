
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
                    start_time = time.time()
                    results = self.classifyImageObject.classify_image(image)
                    elapsed_ms = (time.time() - start_time) * 1000
                    label_id, prob = results[0]
                    stream.seek(0)
                    stream.truncate()
                    camera.annotate_text = '%s %.2f\n%.1fms' % (label_id, prob,
                                                                elapsed_ms)
                    if label_id == 0 and prob > 0.6:
                        return self.get_image_ready_for_sending(image)
                    if time.time() - timer_for_capture > 10:
                        return 0
            finally:
                camera.stop_preview()
    def get_image_ready_for_sending(self, image):
        byte_io = io.BytesIO
        image.save(byte_io, 'jpg')
        return byte_io.seek(0)
