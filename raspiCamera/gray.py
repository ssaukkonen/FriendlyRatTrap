import cv2
import numpy as np


img = cv2.imread('image.jpg',cv2.IMREAD_COLOR)
grayscale = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)

result=cv2.imwrite('gray_image.jpg', grayscale)