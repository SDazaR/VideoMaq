import numpy as np
import cv2

cap = cv2.VideoCapture('rtsp://maya:maya@192.168.1.71:88/videoMain')

j=0

while(True):
    ret, frame = cap.read()    

    cv2.imshow('frame',frame)
    frame = cv2.medianBlur(frame,5)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
    if cv2.waitKey(33) == ord('a'): 
        print "pressed a"
        cv2.imwrite('save%s.jpg'%(j), frame)
        j=j+1


cap.release()
cv2.destroyAllWindows()
