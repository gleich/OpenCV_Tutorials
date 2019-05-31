"""
Created on Fri Feb 15 9:30:37PM 2019

@author: Matt-Gleich

Resizing the image using OpenCV
"""
import numpy as np
import cv2
photo_path = '/Users/matthewgleich/Desktop/First/CV2_Test_Images/Solid_Red_Sized__25214.1507754519.jpg'
img = cv2.imread(photo_path)

# Scale to half resolution
# Arguments: image path, none, x resolution multiplied by, y resolution multiplied by, interpolation method
# General format: cv2.resize(img, None, int1, int2, interpolation method)
res = cv2.resize(img,None,fx=2, fy=2, interpolation = cv2.INTER_CUBIC)
