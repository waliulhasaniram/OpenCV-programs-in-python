import cv2

img = cv2.imread('E:\OpenCV Image detections\images\cars.jpg')
cv2.imshow('image', img)

#grayscale
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY) #grayscale
cv2.imshow('grayscale', gray)

color = cv2.cvtColor(img, cv2.COLOR_BGR2HLS)
cv2.imshow('color', color)

#blur
blur = cv2.GaussianBlur(img, (3,3), cv2.BORDER_DEFAULT)
cv2.imshow('blue', blur)

#Edge cascade
canny = cv2.Canny(blur, 125, 175)
cv2.imshow('edge', canny)

#dilate
dilated = cv2.dilate(canny, (3,3), iterations=3)
cv2.imshow('dialet', dilated)

#eroded
eroded = cv2.erode(img, (3,3), iterations=3)
cv2.imshow('eroded', eroded)

#resized
resized = cv2.resize(img, (500,400), interpolation=cv2.INTER_CUBIC)
cv2.imshow('resize', resized)


#crop
cropped = img[50:300, 300:500]
cv2.imshow('corp', cropped)

cv2.waitKey(0)
