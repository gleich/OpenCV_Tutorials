"""
Created on Fri Feb 15 8:19:21PM 2019

@author: Matt-Gleich

How to convert BRG to other colorspaces such as HSV or Grayscale
"""
import numpy as np
import cv2

cap = cv2.VideoCapture(0)

while(1):

    # Take each frame
    frame = cap.read()

    # Convert BGR to HSV
    HSV_Values = cv2.cvtColor(cv2.UMat(frame), cv2.COLOR_BGR2HSV)

    # Define range of blue color in HSV
    lower_blue = np.array([110, 50, 50])
    upper_blue = np.array([130, 255, 255])

    # Threshold the HSV image ot get only blue color-space
    mask = cv2.inRange(HSV_Values, lower_blue, upper_blue)

    # Bitwise_AND mask and frame
    res = cv2.bitwise_and(frame, frame, mask = mask)

    cv2.imshow("frame", frame)
    cv2.imshow("mask", mask)
    k = cv2.waitKey(5) & 0xFF
    if k == 27:
        break

cv2.destroyAllWindows()
