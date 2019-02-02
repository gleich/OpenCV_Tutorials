# Disclaimer: You need to change the path of where you are trying to load your photo

# When ever your using CV you need to import two things:
import numpy as np
import cv2
photo_path = '/Users/matthewgleich/Desktop/First/CV2_Test_Images/applecv2testphoto.jpg'
# Code from the file "Read_Image.py"
image_in_color = cv2.imread(photo_path, 1)  # Put a one to load picture in color
image_in_BW = cv2.imread(photo_path, 0)  # Put a zero to load picture in black and white
image_unchanged = cv2.imread(photo_path, -1)  # Put a negative one to load a picture unchanged
