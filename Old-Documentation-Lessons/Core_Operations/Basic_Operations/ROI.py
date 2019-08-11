"""
Created on Fri Feb 15 7:42:30PM 2019

@author: Matt-Gleich

ROI is again obtained using Numpy indexing. Here I am selecting the ball
and copyign it to another region in the image
"""
import numpy as np
import cv2

photo_path = '/Users/matthewgleich/Desktop/First/ROI.jpg'
img = cv2.imread(photo_path)

ball = img[280:340, 330:390]
img[273:333, 100:160] = ball
