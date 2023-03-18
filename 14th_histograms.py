import cv2 as cv, numpy as np
import matplotlib.pyplot as plt

img = cv.imread('E:\OpenCV Image detections\images\cars.jpg')
cv.imshow('image', img)

gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
cv.imshow('gray', gray)

gray_hist = cv.calcHist([gray], [0], None,[256], [0,255] )

plt.title('Grayscale histograms')
plt.xlabel('bin')
plt.ylabel('# of pixel')
plt.grid()
plt.plot(gray_hist)
plt.show()

#mask and histogram
blank = np.zeros((500,500), dtype='uint8')
circle = cv.circle(blank, (img.shape[1]//2, img.shape[0]//2), 100, (255,255,255), -1)
cv.imshow('circle', circle)

cv.waitKey(0)