import cv2 as cv
import numpy as np
import matplotlib.pyplot as plt

img = cv.imread('E:\OpenCV Image detections\images\cars.jpg')
cv.imshow('image', img)

#grayscale
gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
cv.imshow('gray', gray)

#HSV
HSV = cv.cvtColor(img, cv.COLOR_BGR2HSV)
cv.imshow('huv', HSV)

#LAB

LAB = cv.cvtColor(img, cv.COLOR_BGR2LAB)
cv.imshow('lab', LAB)

#BGR to RGB
RGB = cv.cvtColor(img, cv.COLOR_BGR2RGB)
cv.imshow('RGB', RGB)

plt.imshow(RGB)
plt.show()

cv.waitKey(0)