import cv2 as cv, numpy as np


blank = np.zeros((450, 450), dtype='uint8')

rectangle = cv.rectangle(blank.copy(), (50,50), (410,410), 255, -1)
cv.imshow('rectangle', rectangle)

circle = cv.circle(blank.copy(), (230,230),200, 255, -1)
cv.imshow('circle', circle)

#Bitwise and --> intersection
bitwise_and = cv.bitwise_and(rectangle, circle)
cv.imshow("bitwise_and", bitwise_and)

#Bitwise or --> intersection and non-intersection
OR = cv.bitwise_or(rectangle,circle)
cv.imshow("bitwise_or", OR)

#Bitwise xor --> non-intersection
BIT_xor = cv.bitwise_xor(rectangle,circle)
cv.imshow("bitwise_xor", BIT_xor)

#Bitwise not --> invert
BIT_NOT = cv.bitwise_not(rectangle,circle)
cv.imshow("bitwise_not", BIT_NOT)



cv.waitKey(0)
