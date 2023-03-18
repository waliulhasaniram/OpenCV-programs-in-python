import cv2 as cv
import numpy as np

img = cv.imread('E:\OpenCV Image detections\images\cars.jpg')

cv.imshow('image', img)

#from gray, blur, edge count contours
gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
cv.imshow('gray', gray)

blur = cv.GaussianBlur(gray, (3,3), cv.BORDER_DEFAULT)
cv.imshow('blur', blur)

canny = cv.Canny(blur, 125, 255)
cv.imshow('edge', canny)

contours, hierarchies = cv.findContours(gray, cv.RETR_TREE, cv.CHAIN_APPROX_NONE)
print(f'{len(contours)} contours found')

#thresh hold count contours
ret, thresh = cv.threshold(gray, 125, 175, cv.THRESH_BINARY)
cv.imshow('thresh', thresh)

contours1, hierarchies1 = cv.findContours(thresh, cv.RETR_LIST, cv.CHAIN_APPROX_NONE)
print(f'{len(contours1)} contours found again')


#draw contours
blank = np.zeros(img.shape, dtype='uint8')
cv.drawContours(blank, contours1, -1, (0,255,0), 1)
cv.imshow('Draw contours', blank)

cv.waitKey(0)