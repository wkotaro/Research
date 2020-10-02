#!/usr/bin/env python

import cv2
import numpy as np 
import imgviz

def video_info(video_data):
    movie = cv2.VideoCapture(video_data) 
    fps    = movie.get(cv2.CAP_PROP_FPS)
    height = movie.get(cv2.CAP_PROP_FRAME_HEIGHT)
    width  = movie.get(cv2.CAP_PROP_FRAME_WIDTH)
    print("fps:{}".format(fps))
    print("height:{}".format(height))
    print("width:{}".format(width))
    return fps,height,width

def movie_edit(frame):
    # Perspective Transformation
    h, w = frame.shape[:2]
    pts1 = np.float32([[265,288],[389,289],[267,167],[390,164]])
    pts2 = np.float32([[0,0],[300,0],[0,300],[300,300]])
    M = cv2.getPerspectiveTransform(pts1,pts2)
    dst = cv2.warpPerspective(frame,M,(300,300))
    return dst

def capture_file(video_data):
    cap = cv2.VideoCapture(video_data)
    fmt = cv2.VideoWriter_fourcc("m","p","4","v")
    fps,height,width = video_info(video_data)
    frame_id = 0
    while(True):
            ret, frame = cap.read()
            if ret == True:
                    out = movie_edit(frame)
                    cv2.imshow('frame',out)
                    imgviz.io.imsave(f"../original/cylinder_36/{frame_id:08d}.jpg", out)
                    if cv2.waitKey(1) & 0xFF == ord('q'):
                        break
            else:
                    break
            frame_id += 1
    cap.release()
    cv2.destroyAllWindows()

video_data = "../movie/cylinder36.wmv"
capture_file(video_data)  
