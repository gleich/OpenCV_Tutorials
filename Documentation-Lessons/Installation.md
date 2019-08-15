# OpenCV Installation

Notes from **1.1** in the documentation

## Python Prerequisites

Install the following dependencies for python. Use any python version that is supported by OpenCV. Check the documentation for supported python versions.

`pip install numpy matplotlib`

* Numpy
* MatPlotLib

## Downloading OpenCV

Once you have installed the python prerequisites, you need to download OpenCV. Follow the instructions on the website listed below:

[SourceForge](http://sourceforge.net/projects/opencvlibrary/files/opencv-win/2.4.6/OpenCV-2.4.6.0.exe/download)

## Testing OpenCV

Test OpenCV by making the python script shown below and running it.

```python
import cv2
print(cv2.__version__)
```

If that runs without any errors, then it works!
