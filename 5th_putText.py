import cv2, numpy as np

blank = np.zeros([500, 500, 3], dtype='uint8')

cv2.putText(blank, 'Hello guys!!!', (150, 50), cv2.FONT_HERSHEY_DUPLEX, 1.0, (0,255,0), 2)
cv2.putText(blank, 'how are you doing!', (90, 90), cv2.FONT_HERSHEY_DUPLEX, 1.0, (0,255,0), 1)
cv2.imshow('text', blank)

cv2.waitKey(0)