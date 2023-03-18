import cv2 as cv, numpy as np

img = cv.imread('E:\OpenCV Image detections\images\cars.jpg')
cv.imshow('image', img)

gry = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
cv.imshow('gray', gry)

# #simple image thresholding
Threshold, Thresh = cv.threshold(gry, 155, 255, cv.THRESH_BINARY)
cv.imshow('simple threshold', Thresh)

#Adaptive thresholding
adaptive_thresholding = cv.adaptiveThreshold(gry, 255, cv.ADAPTIVE_THRESH_MEAN_C, cv.THRESH_BINARY, 13,3)
cv.imshow('Adaptive thresholding', adaptive_thresholding)
cv.waitKey(0)