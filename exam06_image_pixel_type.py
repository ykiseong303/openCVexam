import numpy as np
import cv2

def showVideo() :
    x = 0
    y = 0
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

        ###########################################################

        pixel = frame[320,240]
        print(pixel)

        frame[300:400,300:400] = [255,0,0]

        print(frame.shape) # height, width, color channel
        print(frame.size) # image size(bite)
        print(frame.dtype) # image datatype

        subframe = frame[100:300,0:200]
        cv2.imshow('subframe',subframe)
        ###########################################################


        cv2.imshow('frame',frame)
        k = cv2.waitKey(1) & 0xFF
        if k == 27 :
            break
        # esc : 27(ASCII)

    cap.release()
    #opened object close (release)
    cv2.destroyAllWindows

showVideo()
