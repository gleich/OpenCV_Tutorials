# GUI Features

Notes from **1.2** in the documentation

GUI stands for _**Graphical User Interface**_

## Reading an Image

You can load an image into your program multiple ways. Below is a table of all the options.

| `cv2.imread(file_name, 1)`     | Loads a color image. The default option         |
|------------------------|-------------------------------------------------|
| `cv2.imread(file_name, 0)` | Loads a black and white image                   |
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

## Getting started with Images
