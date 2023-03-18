import cv2
img = cv2.imread('E:\OpenCV Image detections\images\cars.jpg')

cv2.imshow('image', img)
cv2.waitKey(0)

#/////////////  Resize image  //////////////////////////////////////


def resizeImage(frame, scale):
    width = int(frame.shape[1] * scale)
    height = int(frame.shape[0] * scale)
    dimention = (width, height)
    return cv2.resize(frame, dimention, interpolation=cv2.INTER_AREA)

resized_Image = resizeImage(img, scale=1.5)
cv2.imshow('image', resized_Image)
cv2.waitKey(0)