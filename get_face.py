import cv2
import numpy as np 
import os
import random
from face_detection import *
####################################################################################

def main():

    label = input('What is your name?')
    label = label.strip().lower()
    print('We will be taking 5 pictures! Smile when you are ready!')
    cap = cv2.VideoCapture(0) # video capture source camera (Here webcam of laptop) 
    count = 0
    print('Press on y to select the current photo')
    while(True):
        ret,frame = cap.read() # return a single frame in variable `frame`
        rannumb = random.randint(1,100000000)
        while os.path.exists('images/{}.jpg'.format(label+str(rannumb))): rannumb = random.randint(1,100000000)
        cropped,rect = detect_faces(frame,train=1)
        if len(rect) != 0:
            (x, y, w, h) = rect
            cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 255, 0))
        cv2.imshow('it\'s you',frame) #display the captured image
        if cv2.waitKey(1) & 0xFF == ord('y'): #save on pressing 'y' 
            if len(frame) != 0: 
                cv2.imwrite('images/{}.jpg'.format(label+str(rannumb)),cropped)
                count += 1
                print('Picture number {}'.format(count))
                if count == 5:
                    cv2.destroyAllWindows()
                    break

    cap.release()

if __name__ == '__main__':
    main()