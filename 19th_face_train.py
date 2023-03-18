import os
import cv2 as cv
import numpy as np

people = []
for i in os.listdir(r'E:\OpenCV Image detections\Faces\train'):
    people.append(i)

DIR = r'E:\OpenCV Image detections\Faces\train'

haar_cascard = cv.CascadeClassifier(r'E:\\OpenCV Image detections\\haar_faces.xml')

feature = []
labels = []

def creat_train():
    for person in people:
        path = os.path.join(DIR, person)
        label = people.index(person)

        for img in os.listdir(path):
            img_path = os.path.join(path, img)
                                    
            img_array = cv.imread(img_path)
            gray = cv.cvtColor(img_array, cv.COLOR_BGR2GRAY)

            faces_rect = haar_cascard.detectMultiScale(gray, scaleFactor=1.1)

            for (x,y,w,h) in faces_rect:
                faces_roi = gray[y:y+h, x:x+w]
                feature.append(faces_roi)
                labels.append(label)

creat_train()
print('train done ---------------')

feature = np.array(feature, dtype='object')
labels = np.array(labels)

face_recognizer = cv.face.LBPHFaceRecognizer_create()

# train the recognizer on the features list and labels list
face_recognizer.train(feature, labels)

face_recognizer.save('face_recognizer.yml')
np.save('feature.npy', feature)
np.save('labels.npy', labels)