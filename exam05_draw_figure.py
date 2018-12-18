import numpy as np
import cv2

def showVideo() :
    try :
        print("Turn on Camera")
        cap = cv2.VideoCapture(1)
    except :
        print("FAIL")
        return

    while True :
        ret, frame = cap.read()

        if not ret :
            print("ERROR")
            break
        #print(cap.get(3), cap.get(4))
        #3 : column, 4 : row
        #640 x 480
        cv2.line(frame, (0,0),(640,480),(0,255,0),3)
        cv2.rectangle(frame,(100,100),(300,300),(255,0,0),3)
        cv2.circle(frame,(320,240),60,(0,0,255),-1)
        # -1 : The color specified by the parameter

        font = cv2.FONT_HERSHEY_SIMPLEX
        cv2.putText(frame,'OpenCV',(10,400),font,4,(255,255,255),5)
        cv2.imshow('frame',frame)

        k = cv2.waitKey(1) & 0xFF
        if k == 27 :
            break
        # esc : 27(ASCII)

    cap.release()
    #opened object close (release)
    cv2.destroyAllWindows

showVideo()
