"""
Here was will create a simple application which shows the color you spedcify. You have a window which shows the
color and three trackbars to specify each of B,G,R colors. You slide the trackbar and correspondingly widow color
changes. By default, initial color woll be set to Black.

This is the code from the lesson "Trackbar as the color palette" on opencv.org

DISCLAIMER: I am not the owner of any of the code

Written by: Matthew Gleich
Date of Creation: 02/13/19
"""

import cv2
import numpy as np

# Will be used later:
def nothing(x):
    pass

# Creates a black image, a window:
img = np.zeros((300, 512, 3), np.uint8)  # Just for refrence, the three numbers are in BGR, not RGB
cv2.namedWindow("image")

# Create trackbars for color change:
# Aruguments: Trackbar's name, name of window that its attached too, default value, maximum value, callback function
# General Format: cv2.createTrackbar("Trackbar's name","Attached windows name",defaul value, maximum value,callback function)
cv2.createTrackbar("R", "image", 0, 255, nothing)
cv2.createTrackbar("G", "image", 0, 255, nothing)
cv2.createTrackbar("B", "image", 0, 255, nothing)

# Create switch for ON/OFF functionality:
switch = "0 : OFF \n1 : ON"
cv2.createTrackbar(switch, "image" ,0, 1, nothing)

while(1):
    cv2.imshow("image", img)
    k = cv2.waitKey(1) & 0xFF
    if k == 27:
        break

    # Get current position of four trackbars:
    r = cv2.getTrackbarPos("R","image")
    g = cv2.getTrackbarPos("G","image")
    b = cv2.getTrackbarPos("B","image")
    s = cv2.getTrackbarPos(switch,"image")

    if s == 0:
        img[:] = 0
    else:
        img[:] = [b,g,r]

cv2.destroyAllWindows()
