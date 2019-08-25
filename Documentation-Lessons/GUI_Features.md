# GUI Features

Notes from **1.2** in the documentation

GUI stands for _**Graphical User Interface**_

## Reading an Image

You can load an image into your program multiple ways. Below is a table of all the options.

| `cv2.imread(file_name, 1)`  | Loads a color image. The default option         |
| --------------------------- | ----------------------------------------------- |
| `cv2.imread(file_name, 0)`  | Loads a black and white image                   |
| `cv2.imread(file_name, -1)` | Loads the image as such including alpha channel |

Below is an example of loading an image and saving it as a variable called img.

```python
import numpy as np
import cv2

# Load an color image in gray scale
img = cv2.imread("messi5.jpg", 0)
```

_Keep in mind that if the image path is wrong, it won't through a error but img will be None._

## Displaying an Image

You can use `cv2.imshow()` to show an image. Below is an example.

```python
import numpy as np
import cv2

img = cv2.imread("messi5.jpg", 0)
cv2.imshow("image", img)
cv2.waitKey(0)  # Waits for any key to be pressed, value represents how long it will be until it will taken in a key press in milliseconds.
cv2.destroyAllWindows()  # Closes all open windows
```

## Writing an Image

You can use `cv2.imwrite()` to write to an image. Below is an example.

```python
import numpy as np
import cv2

img = cv2.imread("messi5.jpg", 0)
cv2.imwrite("messigray.png", img)  # Saves the file in the current working directory in PNG format.
```

## Getting started with Videos

To capture live video feed from a camera, we can do the following shown below. In the example below, we are using our computer's webcam.

```python
import numpy as np
import cv2

cap = cv2.VideoCapture(0)  # 0 is the webcam location, it can also be the path to a video file

while True:
    ret, frame = cap.read()
    gray_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    cv2.imshow("frame", gray)
    if cv2.waitkey(1) and 0xFF == ord("q"):
        break

cap.release()
cv2.destroyAllWindows()
```

If you would like to this this program in action run Examples/Video-Capture.py

You can also use `cap.read()` to make sure that the frame is read correctly. It returns a bool accordingly. You can also make sure that camera is open by doing `cap.isOpened()`. Again it returns a bool accordingly. If it is not open, you can open it using `cap.open()`.

## Dealing with video files

Due to the fact that I am not using video files, I am not going to be taking notes on it. If you would like to get some information on it, reference the documentation located at the root of this repo.

## Drawing Functions in OpenCV

Drawing geometric figures on an image using OpenCV. One thing to take note of it that we are using BGR values (blue, green, and red). This is important when setting the color of lines/shapes being drawn. Below is a table of important things when dealing with drawing images.

| color     | Color of the drawn object. Passed in as a tuple in the BGR format       |
| --------- | ----------------------------------------------------------------------- |
| thickness | Thiccness of the lines in the drawn image. 1 is default and -1 is close |
| image     | Image that you wanna draw on                                            |

Below is a list of all the functions that we will be using.

1. `cv2.line()`
2. `cv2.circle()`
3. `cv2.rectangle()`
4. `cv2.ellipse()`
5. `cv2.putText()`

### Drawing a Line

In order to draw a line using OpenCV, you need to pass in the start coordinate and the end coordinate. Below is an example of drawing a line in OpenCV, the file can also be found in the _Examples_ folder as _Draw-Line.py_.

```python
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
```

### Drawing a Rectangle

In order to draw a rectangle using OpenCV, you need to do the same type of thing with the line but instead of putting in the start and end coordinates, but in the top-left corner and bottom-right coordinates. Below is an example of drawing a rectangle in OpenCV, the file can also be found in the _Examples_ folder as _Draw-Rectangle.py_.

```python
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
```

### Drawing other objects

If you would like to draw other objects using OpenCV, check the documentation.
