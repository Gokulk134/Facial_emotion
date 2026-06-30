from facial_emotion_recognition import EmotionRecognition
import cv2
ver =EmotionRecognition(device='cpu')
cam=cv2.VideoCapture(0)
while True:
    sucess,frame=cam.read()
    frame=ver.recognise_emotion(frame,return_type='BGR')
    cv2.imshow("frame",frame)
    key=cv2.waitKey(1)
    if key==27:
        break
cam.release()
cv2.destroyAllWindows()