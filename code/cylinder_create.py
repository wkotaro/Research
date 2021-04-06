#!/usr/bin/env python

import cv2
import numpy as np
from matplotlib import pyplot as plt

img = cv2.imread("../image/sample.jpg",0)


c1 = img[0:48, 184:235]

cv2.imwrite("../image/circle.jpg", c1)
out = c1.copy()
image_size = out.size
whitepx = cv2.countNonZero(out)
blackpx = image_size - whitepx
ratio = (whitepx/image_size)*100
print(whitepx)

