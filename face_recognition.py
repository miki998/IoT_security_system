import cv2
import numpy as np
import time
import os
from face_detection import *
from buzzer import alertor, stopAlertor

global thres
thres = 0

##############################################################################

def label_reading(filename):
    s = filename.split('.jpg')[0]
    return ''.join([i for i in s if not i.isdigit()])

names = [label_reading(name) for name in os.listdir('images')]

class Face_recog:

    def __init__(self):
        self.face_recognizer = cv2.face.LBPHFaceRecognizer_create()
        self.path = 'images/'

    def train(self):
        images = os.listdir(self.path)
        faces = []
        labels = []
        
        for image in images:
            img = cv2.imread(self.path+image)

            labels.append(names.index(label_reading(image)))
            img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
            faces.append(img)
            #print(img.shape)
        faces = np.array(faces)
        
        self.face_recognizer.train(faces, np.array(labels))

    def recognition(self,img):
        face, rect = detect_faces(img)
        global thres
        for i in range(0, len(face)) :
            label,confidence = self.face_recognizer.predict(face[i])
            #print(confidence)
            
            label_text = names[label]
            if confidence > 65:
                thres += 1
                label_text = 'Unknown'
                print(thres)
            (x, y, w, h) = rect[i]
            cv2.rectangle(img, (x, y), (x+w, y+h), (0, 255, 0))
            cv2.putText(img, label_text, (x, y), cv2.FONT_HERSHEY_PLAIN, 1.5, (0, 255, 0), 2)
            if label_text == 'Unknown':
                if thres > 10:
                    alertor()
            else:
                thres = 0
                stopAlertor()
        return img


