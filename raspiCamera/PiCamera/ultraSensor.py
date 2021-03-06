import RPi.GPIO as GPIO
import time

class UltraSensor: 
    def __init__(self):
        pass
    
    def set_GPIO(self):
        #GPIO Mode (BOARD / BCM)
        GPIO.setmode(GPIO.BCM)
        GPIO.setwarnings(False)
        
        #set GPIO Pins
        self.GPIO_TRIGGER = 18
        self.GPIO_ECHO = 24
        
        #set GPIO direction (IN / OUT)
        GPIO.setup(self.GPIO_TRIGGER, GPIO.OUT)
        GPIO.setup(self.GPIO_ECHO, GPIO.IN)
        
    def distance(self):
        self.set_GPIO()
        try:
            while True:
                # set Trigger to HIGH
                GPIO.output(self.GPIO_TRIGGER, True)
            
                # set Trigger after 0.01ms to LOW
                time.sleep(0.00001)
                GPIO.output(self.GPIO_TRIGGER, False)
            
                StartTime = time.time()
                StopTime = time.time()
            
                # save StartTime
                while GPIO.input(self.GPIO_ECHO) == 0:
                    StartTime = time.time()
            
                # save time of arrival
                while GPIO.input(self.GPIO_ECHO) == 1:
                    StopTime = time.time()
            
                # time difference between start and arrival
                TimeElapsed = StopTime - StartTime
                # multiply with the sonic speed (34300 cm/s)
                # and divide by 2, because there and back
                distance = (TimeElapsed * 34300) / 2

                if distance < 30:
                    print('Object detected by ultrasonic sensor')
                    return True
        finally:
            GPIO.cleanup()
 