# Disclaimer: You need to change the path of where you are trying to load your photo

# When ever your using CV you need to import two things:
import numpy as np
import cv2
photo_path = '/Users/matthewgleich/Desktop/First/CV2_Test_Images/applecv2testphoto.jpg'
# How to read an image:
image_in_color = cv2.imread(photo_path, 1)  # Put a one to load picture in color
image_in_BW = cv2.imread(photo_path, 0)  # Put a zero to load picture in black and white
image_unchanged = cv2.imread(photo_path, -1)  # Put a negative one to load a picture unchanged

# How to display an image:
# cv2.imshow('image', image_in_color)  # The first argument is the window name and the second one is the variable that is attached to the cv2.imread
# cv2.waitKey(0)  # Will wait until any key on the keyboard is pressed until continuing with the rest of the program
# cv2.destroyAllWindows()  # Will close all open windows

# How to write an image:
cv2.imwrite(photo_path, image_unchanged)  # Will save PNG format in the working directory (AKA will save the changes)

