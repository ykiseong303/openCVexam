import numpy as np
import cv2

def showVideo() :
    try :
        print("Turn on Camera")
        cap = cv2.VideoCapture(1)
        #create VideoCapture object, 0 = self cam, 1 = usbcam
    except :
        print("FAIL")
        return
    #cap.set(3, 480)
    #cap.set(4,320)

    while True :
        ret, frame = cap.read()
        #You can check the video correctly with 'ret'
        #If video is error, ret is False
        #ret is boolean

        if not ret :
        #checking ret which is correctly reading frame
            print("ERROR")
            break
        gray = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
        cv2.imshow('gray_video', gray)

        k = cv2.waitKey(1) & 0xFF
        if k == 27 :
            break
        # esc : 27(ASCII)

    cap.release()
    #opened object close (release)
    cv2.destroyAllWindows

showVideo()
