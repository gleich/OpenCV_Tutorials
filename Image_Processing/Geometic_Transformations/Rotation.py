"""
Created on Fri Feb 15 8:19:21PM 2019

@author: Matt-Gleich

How to convert BRG to other color-spaces such as HSV or Gray-scale
"""
import numpy as np
import cv2
photo_path = '/Users/matthewgleich/Desktop/First/CV2_Test_Images/Solid_Red_Sized__25214.1507754519.jpg'
img = cv2.imread(photo_path, 0)
rows, cols = img.shape

M = cv2.getRotationMatrix2d((cols/2, rows/2), 90, 1)
dst = cv2.warpAffine(img, M (cols, rows))

cv2.show(img)
