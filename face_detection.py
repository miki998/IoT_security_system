import cv2
import numpy as numpy
import time
import os


##############################################################################

def detect_faces(img,train=0):
    face_clf = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    faces = face_clf.detectMultiScale(gray, 1.3, 5)

    array_face = []
    rect = []
    for (x, y, w, h) in faces:
        fc = gray[y:y+h, x:x+w]
        rect.append((x,y,w,h))
        array_face.append(fc)

    if train: 
        if len(array_face) != 0: return array_face[0],rect[0]
        return [],[]
    return array_face,rect
