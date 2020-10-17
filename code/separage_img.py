#!/usr/bin/env python

import cv2
import numpy as np
from PIL import Image
import glob

def ImgSplit1(img):
    i = 0
    while(i < 632):
        img1 = img[i]
        img2 = img1[30 : 90, 30 : 90]
        cv2.imwrite("../separate_img/1/{}.jpg".format(i), img2)
        i += 1

def ImgSplit2(img):
    i = 0
    while(i < 633):
        img1 = img[i]
        img2 = img1[30 : 90, 90 : 150]
        cv2.imwrite("../separate_img/2/{}.jpg".format(i), img2)
        i += 1

def ImgSplit3(img):
    i = 0
    while(i < 633):
        img1 = img[i]
        img2 = img1[30 : 90, 150 : 210]
        cv2.imwrite("../separate_img/3/{}.jpg".format(i), img2)
        i += 1

def ImgSplit4(img):
    i = 0
    while(i < 633):
        img1 = img[i]
        img2 = img1[30 : 90, 210 : 270]
        cv2.imwrite("../separate_img/4/{}.jpg".format(i), img2)
        i += 1 

def ImgSplit5(img):
    i = 0
    while(i < 633):
        img1 = img[i]
        img2 = img1[90 : 150, 30 : 90]
        cv2.imwrite("../separate_img/5/{}.jpg".format(i), img2)
        i += 1

def ImgSplit6(img):
    i = 0
    while(i < 633):
        img1 = img[i]
        img2 = img1[90 : 150, 90 : 150]
        cv2.imwrite("../separate_img/6/{}.jpg".format(i), img2)
        i += 1 

def ImgSplit7(img):
    i = 0
    while(i < 633):
        img1 = img[i]
        img2 = img1[90 : 150, 150 : 210]
        cv2.imwrite("../separate_img/7/{}.jpg".format(i), img2)
        i += 1

def ImgSplit8(img):
    i = 0
    while(i < 633):
        img1 = img[i]
        img2 = img1[90 : 150, 210 : 270]
        cv2.imwrite("../separate_img/8/{}.jpg".format(i), img2)
        i += 1  

def ImgSplit9(img):
    i = 0
    while(i < 633):
        img1 = img[i]
        img2 = img1[150 : 210, 30 : 90]
        cv2.imwrite("../separate_img/9/{}.jpg".format(i), img2)
        i += 1

def ImgSplit10(img):
    i = 0
    while(i < 633):
        img1 = img[i]
        img2 = img1[150 : 210, 90 : 150]
        cv2.imwrite("../separate_img/10/{}.jpg".format(i), img2)
        i += 1

def ImgSplit11(img):
    i = 0
    while(i < 633):
        img1 = img[i]
        img2 = img1[150 : 210, 150 : 210]
        cv2.imwrite("../separate_img/11/{}.jpg".format(i), img2)
        i += 1

def ImgSplit12(img):
    i = 0
    while(i < 633):
        img1 = img[i]
        img2 = img1[150 : 210, 210 : 270]
        cv2.imwrite("../separate_img/12/{}.jpg".format(i), img2)
        i += 1 

def ImgSplit13(img):
    i = 0
    while(i < 633):
        img1 = img[i]
        img2 = img1[210 : 270, 30 : 90]
        cv2.imwrite("../separate_img/13/{}.jpg".format(i), img2)
        i += 1

def ImgSplit14(img):
    i = 0
    while(i < 633):
        img1 = img[i]
        img2 = img1[210 : 270, 90 : 150]
        cv2.imwrite("../separate_img/14/{}.jpg".format(i), img2)
        i += 1

def ImgSplit15(img):
    i = 0
    while(i < 633):
        img1 = img[i]
        img2 = img1[210 : 270, 150 : 210]
        cv2.imwrite("../separate_img/15/{}.jpg".format(i), img2)
        i += 1

def ImgSplit16(img):
    i = 0
    while(i < 633):
        img1 = img[i]
        img2 = img1[210 : 270, 210 : 270]
        cv2.imwrite("../separate_img/16/{}.jpg".format(i), img2)
        i += 1

frames = []
images = glob.glob("../out/cylinder_46/*.jpg")

for image in images:
    new_frame = np.array(Image.open(image))
    frames.append(new_frame)

ImgSplit1(frames)

