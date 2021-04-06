#!/usr/bin/env python

import numpy as np
import  cv2

def gamma_area(frame, x, y, w, h, g=0.1):
    dst = frame.copy()
    dst[y:y+h, x:x+w] = gamma(dst[y:y+h, x:x+w], g)
    return dst

def gamma(img, g=0.5):
    gamma_cvt = np.zeros((256, 1), dtype=np.uint8)
    for i in range(256):
        gamma_cvt[i][0] = 255 * (float(i)/255) ** (1.0/g)
    img_gamma = cv2.LUT(img, gamma_cvt)
    return img_gamma

def movie_edit(frame):
    frame = gamma(frame)
    frame = gamma_area(frame, 200, 100, 200, 90, g=0.3) 
    # bgr -> gray
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    # Perspective Transformation
    h, w = gray.shape
    pts1 = np.float32([[265,288],[388,288],[266,165],[389,165]]) 
    pts2 = np.float32([[0,0],[300,0],[0,300],[300,300]])
    M = cv2.getPerspectiveTransform(pts1,pts2)
    dst = cv2.warpPerspective(gray,M,(300,300))
    # normalize
    blur = cv2.GaussianBlur(dst,(5,5),0)
    ret,th = cv2.threshold(blur, 30, 255, cv2.THRESH_BINARY)
    kernel = np.ones((3,3), np.uint8)
    closing = cv2.morphologyEx(th, cv2.MORPH_CLOSE, kernel, iterations=1)
    # opening = cv2.morphologyEx(closing, cv2.MORPH_OPEN, kernel, iterations=3) 
    # erosion = cv2.erode(th, kernel, iterations=1)
    return gray, closing

cap = cv2.VideoCapture("../movie/cylinder46.wmv")

fgbg = cv2.createBackgroundSubtractorMOG2()

while(True):
    ret, frame = cap.read()
    if ret == True:
            gary, out = movie_edit(frame)
            fgmask = fgbg.apply(out)

            cv2.imshow("frame", fgmask)
            k = cv2.waitKey(30) & 0xff
            if k == 27:
                break

cap.release()
cv2.destroyAllWindows()
