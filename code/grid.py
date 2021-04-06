#!/usr/bin/env python

import cv2
import numpy as np
from matplotlib import pyplot as plt

img = cv2.imread("grid.JPG",0)
h, w = img.shape
pts1 = np.float32([[1013,213],[2653,212],[998,1886],[2671,1862]])
pts2 = np.float32([[0,0],[300,0],[0,300],[300,300]])
M = cv2.getPerspectiveTransform(pts1,pts2)
dst = cv2.warpPerspective(img,M,(300,300)) 
blur = cv2.GaussianBlur(dst,(5,5),0)
ret,th = cv2.threshold(blur, 70, 255, cv2.THRESH_BINARY)
kernel = np.ones((3,3), np.uint8)
erosion = cv2.erode(th, kernel, iterations=1)
out = erosion.copy()
image_size = out.size
whitepx = cv2.countNonZero(out)
blackpx = image_size - whitepx
ratio = (whitepx/image_size)*100
print(ratio)
plt.imshow(out, cmap="gray")
plt.show()
