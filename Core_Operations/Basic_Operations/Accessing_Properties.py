"""
Created on Thur Feb 14 8:25:43PM 2019

@author: Matt-Gleich

This file demonstrates how to Access and Modify Pixel Values
Lesson on actual website:
"""
import numpy as np
import cv2

photo_path = '/Users/matthewgleich/Desktop/First/CV2_Test_Images/Solid_Red_Sized__25214.1507754519.jpg'
img = cv2.imread(photo_path)

img_shape = img.shape  # Number of rows, columns, and channels (channels if image is in color)
print(img_shape)

"""
img.dtype is very important while debugging because a large number of errors in Open-CV
Python code is cause by invalid data type.
"""
image_data = img.dtype
print(image_data)
