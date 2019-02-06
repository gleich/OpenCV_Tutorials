# img : The image where you want to draw the shapes
# color : Color of the shape. for BGR, pass it as a tuple, eg: (255,0,0) for blue. For grayscale, just pass the scalar value.
# thickness : Thickness of the line or circle etc. If -1 is passed for closed figures like circles, it will fill the shape. default thickness = 1
# lineType : Type of line, whether 8-connected, anti-aliased line etc. By default, it is 8-connected. cv2.LINE_AA gives anti-aliased line which looks great for curves.
import numpy as np
import cv2

# Set a backround color:
# Aruguments: HSL colors
# General Format: np.zeros((Colors), np.uint8)
img = np.zeros((512, 512, 3), np.uint8)  # Creates a black image (Should have nothing in it)

# Draw a line:
# Aruguments: Starting and ending coordinates for the line.
# General Formant: cv2.line(image name, (starting coordinates), (stopping coordinates), (color), thickness)
diagonal_img = cv2.line(img, (0, 0), (511, 511), (255, 0, 0), 5)  # Creates a diagonal blue line with thickness of 5 px

# Draw a rectangle:
# Aruguments: Top left corner position and bottom right corner position of the rectangle
# General format: cv2.rectangle(image name, (top left corner position), (bottom right corner position), (color), thickness)
rectangle_img = cv2.rectangle(img, (384, 0), (510, 128), (0, 255, 0), 3)

# Draw a circle:
# Aruguments: Center coordinates and radius
# General format: cv2.circle(image name, (center corrdinates), radius, (colors), thickness)
circle_img = cv2.circle(img, (447, 63), 63, (0, 0, 255), -1)