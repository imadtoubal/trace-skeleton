# The `trace_skeleton` Python package

A python package for tracing the skeleton of a 2D image. This work uses the
[Skeleton Tracing algorithm](https://github.com/LingDong-/skeleton-tracing)
developed by [LingDong](https://github.com/LingDong-).
This repo provides an easy to install python package for tracing the skeleton.
This is done to ease the use of the algorithm in other Python projects. We've
taken the SWIG C implementation for optimal performance.

## Usage
Quick and easy installation:
```bash
pip install trace-skeleton
```

## Example
The examples shown are a copy-paste from the
[original repo](https://github.com/LingDong-/skeleton-tracing).

```python
import trace_skeleton
import cv2
import random

im = cv2.imread("../test_images/opencv-thinning-src-img.png",0)

_,im = cv2.threshold(im,128,255,cv2.THRESH_BINARY);

polys = trace_skeleton.from_numpy(im);

for l in polys:
	c = (200*random.random(),200*random.random(),200*random.random())
	for i in range(0,len(l)-1):
		cv2.line(im,(l[i][0],l[i][1]),(l[i+1][0],l[i+1][1]),c)

cv2.imshow('',im);cv2.waitKey(0)
```

## Advanced

The aforementioned API's have a tiny linear time overhead for transforming input
and output between internal datastructures and python objects. Alternatively,
you can use the following: 

```python
from trace_skeleton import *

im = "\0\1\0\0\1\0\0\1\0 ..... " #image stored as a (char*)
w = 128 #dimensions
h = 64

trace(im,w,h)

# iterate over each point in each polyline
# by popping them off the internal datastructure
# len_polyline() gets the length of current polyline
# -1 means no more polylines
while (len_polyline() != -1):
	n = len_polyline();
	for i in range(0,n):
		# pop_point() retrieve and remove the next point
		# on the polyline. It returns the flat index in image
		# mod/div it with width to get (x,y) coordinate
		idx = pop_point()
		x = idx % w;
		y = idx //w;
		print(x,y)
	print("\n")
```