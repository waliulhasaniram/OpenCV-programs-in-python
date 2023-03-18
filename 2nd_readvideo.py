import cv2 

capture = cv2.VideoCapture('videos\Greenscreen.mp4') 

while True:
    isTrue, frame = capture.read()
    

    if isTrue:
        cv2.imshow('Video', frame)

        if cv2.waitKey(20) & 0xFF==ord('d'):
            break

    else:
        break

capture.release()    
cv2.destroyAllWindows()