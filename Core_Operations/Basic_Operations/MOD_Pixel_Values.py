"""
Created on Thur Feb 14 4:43:33PM 2019

@author: Matt-Gleich

This file demonstrates how to Access and Modify Pixel Values
Lesson on actual website:
"""
import numpy as np
import cv2

photo_path = '/Users/matthewgleich/Desktop/First/CV2_Test_Images/Solid_Red_Sized__25214.1507754519.jpg'

img = cv2.imread(photo_path)
pd = img[100, 100]  # Both numbers are the coordinates for the pixel in the image
# print(pd)

blue_value = img[100, 100, 0]  # The zero at the end tells the array to only grab the blue color
# print(blue_value)

img[100, 100] = [255, 255, 255]  # This will now change the pixel to be white
# print(img)

red_value = img.item(10, 10, 2)  # Accessing the RED value

# Changing the RED value
img.itemset((10, 10, 2), 90)
red_changed = img.item(10, 10, 2)
print(red_changed)

# Find

