#!/usr/bin/env python

import cv2
import numpy as np
from matplotlib import pyplot as plt
from PIL import Image, ImageDraw, ImageFilter

img1 = Image.open("../image/black.jpg")
s = Image.open("../image/circle.jpg")

img1.paste(s)
# img1.save("../image/black_circle_paste.jpg", quality=95)



