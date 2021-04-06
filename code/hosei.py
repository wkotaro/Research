#!/usr/bin/env python

import cv2
import numpy as np
from matplotlib import pyplot as plt

img = cv2.imread("origin.JPG",0)
h, w = img.shape
pts1 = np.float32([[1106,212],[2849,167],[1117,1970],[2886,1940]])
pts2 = np.float32([[0,0],[300,0],[0,300],[300,300]])
M = cv2.getPerspectiveTransform(pts1,pts2)
dst = cv2.warpPerspective(img,M,(300,300)) 
blur = cv2.GaussianBlur(dst,(5,5),0)
ret,th = cv2.threshold(blur, 70, 255, cv2.THRESH_BINARY)
kernel = np.ones((3,3), np.uint8)
erosion = cv2.erode(th, kernel, iterations=1)
closing = cv2.morphologyEx(th, cv2.MORPH_CLOSE, kernel, iterations=2)
opening = cv2.morphologyEx(closing, cv2.MORPH_OPEN, kernel, iterations=3)
edge = cv2.Canny(dst, 70, 200)
out = opening.copy()
image_size = out.size
whitepx = cv2.countNonZero(out)
blackpx = image_size - whitepx
ratio = (whitepx/image_size)*100
print(ratio)
add = cv2.addWeighted(edge,0.3,out,0.7,0)
plt.subplot(131)
plt.imshow(edge, cmap="gray")
plt.subplot(132)
plt.imshow(out, cmap="gray")
plt.subplot(133)
plt.imshow(add, cmap="gray")
plt.show()
