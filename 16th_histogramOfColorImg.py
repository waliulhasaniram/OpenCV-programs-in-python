import cv2 as cv, numpy as np
import matplotlib.pyplot as plt

img = cv.imread('E:\OpenCV Image detections\images\cars.jpg')
cv.imshow('image', img)

plt.title('Histograms for color image')
plt.xlabel('bin')
plt.ylabel('# of pixel')

Colors = ['b', 'g', 'r']
for i,col in enumerate(Colors):
    hist = cv.calcHist([img], [i], None, [256], [0,256])
    plt.plot(hist, color=col)
    #plt.xlim(0,256)

plt.show()
cv.waitKey(0)