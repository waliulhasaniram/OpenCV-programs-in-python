import cv2 as cv, numpy as np
import matplotlib.pyplot as plt

img = cv.imread('E:\OpenCV Image detections\images\cars.jpg')
cv.imshow('image', img)

gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
cv.imshow('gray', gray)

#grayscale, mask and histogram
blank = np.zeros(img.shape[:2], dtype='uint8')
circle = cv.circle(blank, (img.shape[1]//2 -60, img.shape[0]//2 +100), 100, (255,255,255), -1)

mask = cv.bitwise_and(gray, gray, mask=circle)
cv.imshow('mask', mask)

mask_hist = cv.calcHist([mask], [0],mask, [256], [0,255] )

plt.title('Grayscale masked histograms')
plt.xlabel('bin')
plt.ylabel('# of pixel')
plt.grid()
plt.plot(mask_hist)
plt.show()

cv.waitKey(0)