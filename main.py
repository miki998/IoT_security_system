import numpy as np
import cv2
import os

from face_detection import *
from face_recognition import *

####################################################################################

def main():
	model = Face_recog()
	model.train()
	video_capture = cv2.VideoCapture(0)
	while True :
		ret, frame = video_capture.read()
		if not ret : break
		frame = model.recognition(frame)
		#print(frame.shape)
		cv2.imshow('ok', frame)

		if cv2.waitKey(1) & 0xFF == ord('q') :
			break

	#video_capture.release()
	cv2.destroyAllWindows()


if __name__ == '__main__':
	main()
