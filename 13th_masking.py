import cv2 as cv, numpy as np

img = cv.imread('E:\OpenCV Image detections\images\cars.jpg')
cv.imshow('image', img)

blank = np.zeros(img.shape[:2], dtype='uint8')
cv.imshow('blank', blank)

circle = cv.circle(blank.copy(), (img.shape[1]//2 -60, img.shape[0]//2 +100), 100, (255,255,255), -1)
cv.imshow('circle', circle)

masked = cv.bitwise_and(img, img, mask=circle)
cv.imshow('mask', masked)

cv.waitKey(0)