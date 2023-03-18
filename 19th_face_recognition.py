import numpy as np
import cv2 as cv
import os

haar_cascard = cv.CascadeClassifier(r'E:\\OpenCV Image detections\\haar_faces.xml')

people = []
for i in os.listdir(r'E:\OpenCV Image detections\Faces\train'):
    people.append(i)

feature = np.load('feature.npy', allow_pickle=True)
labels = np.load('labels.npy')    

face_recognizer = cv.face.LBPHFaceRecognizer_create()
face_recognizer.read('face_recognizer.yml')


img = cv.imread(r'E:\OpenCV Image detections\Faces\val\ben_afflek\1.jpg')

gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
cv.imshow('gray', gray)

#detect faces

face_rect = haar_cascard.detectMultiScale(gray, 1.1)

for (x,y,w,h) in face_rect:
    face_roi = gray[y:y+h, x:x+w]

    label, confidence = face_recognizer.predict(face_roi)
    print(f'Label = {people[label]} with a confidence of {confidence}')

    cv.putText(img, str(people[label]), (20,20), cv.FONT_HERSHEY_COMPLEX, 1, (0,255,0), thickness=1) 
    cv.rectangle(img, (x,y), (x+w,y+h), (0,255,0), thickness=1)

cv.imshow('detect face', img)
cv.waitKey(0)   