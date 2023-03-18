import cv2

capture = cv2.VideoCapture('videos\Greenscreen.mp4')

def resizeVideo(frames, scale):
    width = int(frames.shape[1] * scale)
    height = int(frames.shape[0] * scale)
    dimention = (width, height)
    return cv2.resize(frames, dimention, interpolation = cv2.INTER_AREA)
     

while True:
    isTrue, frame = capture.read()
   
    if isTrue:   
        resized_video = resizeVideo(frame, scale=0.5)
        cv2.imshow("video",resized_video)

        if cv2.waitKey(20) & 0xFF==('q'):
            break   
    else:
        break
capture.release()
cv2.destroyAllWindows()    