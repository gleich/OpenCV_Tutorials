"""
Created on Fri Feb 15 8:19:21PM 2019

@author: Matt-Gleich

How to convert BRG to other colorspaces such as HSV or Grayscale
"""
import numpy as np
import cv2

photo_path = '/Users/matthewgleich/Desktop/First/CV2_Test_Images/Solid_Red_Sized__25214.1507754519.jpg'
img = cv2.imread(photo_path)

# Color conversion:
# Arguments: file path and what BGR is being converted too
# General format: cv2.cvtColor(input_image, product colorspace)
HSV_Values = cv2.cvtColor(photo_path, cv2.COLOR_BGR2HSV)
Gray_Scale_Values = cv2.cvtColor(photo_path, cv2.COLOR_BGR2GRAY)
print(HSV_Values)
print(Gray_Scale_Valuess)

"""
Note!
For HSV, Hue range is [0,179], Saturation range is [0,255] and Value range is [0,255]. Different softwares use different scales.
So if you are comparing OpenCV values with them, you need to normalize these ranges.
"""
