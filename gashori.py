#playing video 
import cv2
import numpy as np 

def video_info(video_data):
    movie = cv2.VideoCapture(video_data) 
    fps    = movie.get(cv2.CAP_PROP_FPS)
    height = movie.get(cv2.CAP_PROP_FRAME_HEIGHT)
    width  = movie.get(cv2.CAP_PROP_FRAME_WIDTH)
    print("fpsは{}".format(fps))
    print("heightは{}".format(height))
    print("widthは{}".format(width))
    return fps,height,width

def white_area_ratio(mov):
	out = mov.copy()
	image_size = out.size
	whitepx = cv2.countNonZero(out)
	blackpx = image_size - whitepx

	ratio = (whitepx/image_size)*100

	return ratio

def movie_edit(frame):
	# bgr -> gray
	gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

	# Perspective Transformation
	h, w = gray.shape

	pts1 = np.float32([[235,288],[361,290],[234,161],[363,164]])
	pts2 = np.float32([[0,0],[300,0],[0,300],[300,300]])

	M = cv2.getPerspectiveTransform(pts1,pts2)

	dst = cv2.warpPerspective(gray,M,(300,300))

	# normalize
	blur = cv2.GaussianBlur(dst,(5,5),0)
	ret,th = cv2.threshold(blur, 0, 255, cv2.THRESH_BINARY+cv2.THRESH_OTSU)	

	return gray, th 

def capture_file(video_data):
	cap = cv2.VideoCapture(video_data)

	fmt = cv2.VideoWriter_fourcc("m","p","4","v")

	fps,height,width = video_info(video_data)
	writer = cv2.VideoWriter("output.mp4", fmt, fps, (int(width), int(height)), False)

	whitelist = []

	while(True):
	
		ret, frame = cap.read()

		if ret == True:
			# bgr -> gray
			# gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

			# Perspective Transformation
			# h, w = gray.shape

			# pts1 = np.float32([[235,288],[361,290],[234,161],[363,164]])
			# pts2 = np.float32([[0,0],[300,0],[0,300],[300,300]])

			# M = cv2.getPerspectiveTransform(pts1,pts2)

			# dst = cv2.warpPerspective(gray,M,(300,300))

			# normalize
			# blur = cv2.GaussianBlur(dst,(5,5),0)
			# ret2,th = cv2.threshold(blur, 0, 255, cv2.THRESH_BINARY+cv2.THRESH_OTSU)
			gray, out = movie_edit(frame)
			# White area : Black area
			# out = th.copy()
			# image_size = out.size
			# whitepx = cv2.countNonZero(out)
			# blackpx = image_size - whitepx

			# ratio = (whitepx/image_size)*100
			white_ratio = white_area_ratio(out)

			# black_area_ratio = (blackpx/image_size)*100
			# white_area_ratio = (whitepx/image_size)*100
			# print("White Area [%] :", white_area_ratio)
			# print("Black Area [%] :", black_area_ratio)

			whitelist.append(white_ratio)
			# whitelist.append(white_area_ratio)
			# blacklist.append(black_area_ratio)
			np.savetxt("whitepx.csv", whitelist, delimiter=",")
			# np.savetxt("blackpx.csv", blacklist, delimiter=",")

			cv2.imshow('frame',out)

			writer.write(out)
			if cv2.waitKey(1) & 0xFF == ord('q'):
			    break

		else:
			break

	cap.release()
	writer.release()
	cv2.destroyAllWindows()

video_data = "cylinder1.wmv"
capture_file(video_data)