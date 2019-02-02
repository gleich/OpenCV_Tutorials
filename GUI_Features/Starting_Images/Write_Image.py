# Disclaimer: You need to change the path of where you are trying to load your photo

# When ever your using CV you need to import two things:
import numpy as np
import cv2
photo_path = '/Users/matthewgleich/Desktop/First/CV2_Test_Images/applecv2testphoto.jpg'
# Code from the file "Read_Image.py"
image_in_color = cv2.imread(photo_path, 1)  # Put a one to load picture in color
image_in_BW = cv2.imread(photo_path, 0)  # Put a zero to load picture in black and white
image_unchanged = cv2.imread(photo_path, -1)  # Put a negative one to load a picture unchanged

# cv.imwrite(photo_path, image_in_color)  # This would save the changes make to the photo

# Below is a program that loads an image in grayscale, displays it, saves the image is you press
cv2.imshow("image", image_in_color)
k = cv2.waitKey(0)
if k == 27:  # Wait for ESC key to exit
    cv2.destroyAllWindows()
elif k == ord("s"):  # Wait for 's' key to save and exit
    cv2.imwrite(photo_path, image_in_color)
    cv2.destroyAllWindows()
