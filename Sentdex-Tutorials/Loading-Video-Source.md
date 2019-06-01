# Loading Video Source
This file will go how to interact with a webcam or a video file within OpenCV.

## Get a live feed from a webcam
The code shown below will get the video feed from your webcam live.
```python
import cv2
import numpy as np

cap = cv2.VideoCapture(0)  # Will capture the video feed from the first webcam in your system.

while True:
    ret, frame = cap.read()  # ret will return a True or False statement based of if there is a feed from the webcam. frame is the acual current frame from the video.
    
    cv2.imshow('frame', frame)
    
    if cv2.waitKey(1) and 0xFF == ord('q'):  # Checks to see if the 'q' key is pressed
        break
        
        
cap.release()  # Stop the connection to the webcam.
cv2.destroyAllWindows()
```


## Changing the current frame to B&W
The code shown below will get the video feed from you webcam live and turn it to black and white.
```python

```