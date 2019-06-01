# Introduction and Loading Images in OpenCV


## Setup for OpenCV

Inorder just use OpenCV by just installing the content with pip, fun the following commands: `pip install numpy matplotlib opencv-python`

## Setup in Python file
Not all of the modules below are needed to setup an OpenCV file

Here is a sample file that will setup opencv for you:
```python
import numpy
import matplotlib
import cv2
```


#### Your all setup for basic opencv usage!


## Loading and Image
The code shown below is how to load an image in OpenCV.
```python
import cv2

img = cv2.imread("/sample_images/IMG_2958.jpg", cv2.IMREAD_GRAYSCALE)  # Loads image in from the local directory and converts it to grayscale.
# If nothing is put in for the second parameter, then it will load it in color but remove the alpha channel.
# The alpha channel is a degree of opaqueness. The line cv2.IMREAD_GRAYSCALE also removes this channel.
# The reason that we remove the alpha channel is because it is easier to work with and faster.
# Below are a few examples of other ways you can read in the image:
img = cv2.imread("/sample_images/IMG_2958.jpg", cv2.IMREAD_COLOR)  # Will load the image in color
img = cv2.imread("/sample_images/IMG_2958.jpg", cv2.IMREAD_UNCHANGED)  # Will load the raw image
```

## Showing an image using OpenCV
The code shown below is how to show (display) an image using OpenCV.
```python
import cv2

# You first need to load the image
img = cv2.imread("/sample_images/IMG_2958.jpg", cv2.IMREAD_GRAYSCALE)
# The lines below will display the image:
cv2.imshow('title for window', img)
cv2.waitKey(0)  # Waits for any key to be presses.
cv2.destroyAllWindows()  # Will close the window.
```

## Showing an image using matplotlib:
The reason that you would want to use this to display an image rather than OpenCV is becuase of the plot feature. This will be able to show you the coordinates of any point on the image when your mouse hovers over it.

The code shown below is how to show (display) an image using matplotlib.
```python
import cv2
import matplotlib.pyplot as plt

# You first need to load the image
img = cv2.imread("/sample_images/IMG_2958.jpg", cv2.IMREAD_GRAYSCALE)
# The lines below will display the image:
plt.imshow(img, cmap='gray', interpolation='bicubic')  # Opens the image in black and white.
plt.show()  # Will display the image
```

## Saving an Image
the code shown below demonstrates how to save an image.

```python
import cv2

# You first need to load the image
img = cv2.imread("/sample_images/IMG_2958.jpg", cv2.IMREAD_GRAYSCALE)
# The line below will save the image
cv2.imwrite("new-file-name.extension", img)
```