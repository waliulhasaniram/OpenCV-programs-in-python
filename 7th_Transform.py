import cv2
import numpy as np 

img = cv2.imread('E:\OpenCV Image detections\images\cars.jpg')

cv2.imshow('image', img)

#transform
def transform(img, x,y):
    transform_Mat = np.float32([[1,0,x],[0,1,y]])
    dimention = (img.shape[1], img.shape[0])
    return cv2.warpAffine(img, transform_Mat, dimention)

transformed = transform(img, 50, -100)

cv2.imshow("transformed", transformed)

#resize
resized = cv2.resize(img, (700,500), interpolation=cv2.INTER_CUBIC)
cv2.imshow('resize', resized)

#flip
fliped = cv2.flip(img, 1)
cv2.imshow('flip', fliped)

#Rotate
def rotatingImage(img, angle, rotPoint):
    width = img.shape[1]
    height = img.shape[0]

    rotPoint = (width//2, height//2)
    rotMat = cv2.getRotationMatrix2D(rotPoint, angle, 1.0)
    dimention = (width, height)

    return cv2.warpAffine(img, rotMat, dimention)

rotating = rotatingImage(img, 45, None)
cv2.imshow('rotated',rotating)

cv2.waitKey(0)