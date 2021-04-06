#playing video 
import cv2
import numpy as np 
import imgviz

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

def video_info(video_data):
    movie = cv2.VideoCapture(video_data) 
    fps    = movie.get(cv2.CAP_PROP_FPS)
    height = movie.get(cv2.CAP_PROP_FRAME_HEIGHT)
    width  = movie.get(cv2.CAP_PROP_FRAME_WIDTH)
    print("fps:{}".format(fps))
    print("height:{}".format(height))
    print("width:{}".format(width))
    return fps,height,width

def white_area_ratio(mov):
    out = mov.copy()
    image_size = out.size
    whitepx = cv2.countNonZero(out)
    blackpx = image_size - whitepx
    ratio = (whitepx/image_size)*100
    return ratio

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
    dst = cv2.fastNIMeansDenosisingColored(dst,None,0)
    ret,th = cv2.threshold(blur, 30, 255, cv2.THRESH_BINARY)
    kernel = np.ones((3,3), np.uint8)
    closing = cv2.morphologyEx(th, cv2.MORPH_CLOSE, kernel, iterations=1)
    # opening = cv2.morphologyEx(closing, cv2.MORPH_OPEN, kernel, iterations=3) 
    # erosion = cv2.erode(th, kernel, iterations=1)
    return gray, closing

def capture_file(video_data):
    cap = cv2.VideoCapture(video_data)
    fmt = cv2.VideoWriter_fourcc("m","p","4","v")
    fps,height,width = video_info(video_data)
    whitelist = []
    frame_id = 0
    while(True):
            ret, frame = cap.read()
            if ret == True:
                    gray, out = movie_edit(frame)
                    white_ratio = white_area_ratio(out)
                    whitelist.append(white_ratio)
                    np.savetxt("../data/cylinder26.csv", whitelist, delimiter=",")
                    cv2.imshow('frame',out)
                    imgviz.io.imsave(f"../out/cylinder_26/{frame_id:08d}.jpg", out)
                    if cv2.waitKey(1) & 0xFF == ord('q'):
                        break
            else:
                    break
            frame_id += 1
    cap.release()
    cv2.destroyAllWindows()

video_data = "../movie/cylinder26.wmv"
capture_file(video_data)