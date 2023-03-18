import cv2 as cv, numpy as np


#simple video thresholding
capture = cv.VideoCapture('videos\Greenscreen.mp4')
while True:
    isTrue, frame = capture.read()

    if isTrue:
        grayV = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)
        ThresholdV, ThreshV = cv.threshold(grayV, 155, 255, cv.THRESH_BINARY)
        cv.imshow('Thresholded video', ThreshV)
        
        if cv.waitKey(20) & 0xFF==ord('q'):
            break

    else:
        break

cv.waitKey(0)