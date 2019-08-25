import numpy as np
import cv2

# Create a black image
# Tuple passed in is: (Image Width, Image Height, Number of Color Channels)
img = np.zeros((512, 512, 3), np.uint8)

img = cv2.rectangle(img, (384, 0), (510, 128), (0, 255, 0), 3)

cv2.imshow("rectangle", img)
k = cv2.waitKey(0)
if k == 27:
    cv2.destroyAllWindows()
