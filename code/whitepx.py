#!/usr/bin/env python

import cv2
import numpy as np
from PIL import Image
import glob

def white_area_ratio(mov):
    out = mov.copy()
    image_size = out.size
    whitepx = cv2.countNonZero(out)
    blackpx = image_size - whitepx
    ratio = (whitepx/image_size)*100
    return ratio

def whitepx_save(img):
    whitelist = []
    i = 0
    while(i < 632):
        out = img[i]
        white_ratio = white_area_ratio(out)
        whitelist.append(white_ratio)
        np.savetxt("../data/16.csv", whitelist, delimiter=",")
        i += 1

frames = []
images = glob.glob("../separate_img/16/*.jpg")

for image in images:
    new_frame = np.array(Image.open(image))
    frames.append(new_frame)

whitepx_save(frames)
