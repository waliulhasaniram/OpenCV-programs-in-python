import cv2
import numpy as np

blank = np.zeros((500,500,3), dtype='uint8')

# cv2.imshow('blank_image', blank)

#drowing shape
blank[100:300, 300:400]= 245,255,0

#drowing rectangle around the shape
cv2.rectangle(blank, (400,300), (300,100), (0,0,255), thickness=2, lineType=None)

#drowing circle
cv2.circle(blank, (100,200), 50, (0,255,0), thickness=1, lineType=None)

#draw a line
cv2.line(blank, (100,200), (200, 300), (0,255,255), thickness=1)

#putting text in image
cv2.putText(blank, 'Hello guys!!!', (150, 50), cv2.FONT_HERSHEY_DUPLEX, 1.0, (0,255,0), 2)
cv2.putText(blank, 'how are you doing!', (90, 90), cv2.FONT_HERSHEY_DUPLEX, 1.0, (0,255,0), 2)

cv2.imshow('circle',blank)


cv2.waitKey(0)

