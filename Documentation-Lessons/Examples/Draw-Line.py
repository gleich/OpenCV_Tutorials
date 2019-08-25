import numpy as np
import cv2

# Create a black image
# Tuple passed in is: (Image Width, Image Height, Number of Color Channels)
img = np.zeros((512, 512, 3), np.uint8)

# Draw a diagonal blue line with thickness of 5 px
# Arguments: image, start coordinate, end coordinate, color value (BGRd, thickness)
img = cv2.line(img, (0, 0), (511, 511), (255, 0, 0), 5)

# Showing example:
cv2.imshow("line example", img)
k = cv2.waitKey(0)
if k == 27:  # Waiting for ESC key to quit
    cv2.destroyAllWindows()
