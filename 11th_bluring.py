import cv2 as cv

img = cv.imread('E:\OpenCV Image detections\images\cars.jpg')
cv.imshow('image', img)

#Averaging
Averaging = cv.blur(img, (3,3))
cv.imshow('averaging', Averaging)

#GaussianBlur
gaussianBlur = cv.GaussianBlur(img, (3,3), 0)
cv.imshow('GaussianBlur', gaussianBlur)

#medianBlur
me = cv.medianBlur(img, 3)
cv.imshow('medianBlur', me)

#bilateralFilter
BI = cv.bilateralFilter(img, 5, 15, 15)
cv.imshow('bilateralFilter', BI)

cv.waitKey(0)
