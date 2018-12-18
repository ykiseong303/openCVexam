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

        ###########################################################
        hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

        lower_blue = np.array([110,100,100])
        upper_blue = np.array([130,255,255])
        """
        lower_green = np.array([50,100,100])
        upper_green = np.array([70,255,255])

        lower_red = np.array([-10,100,100])
        upper_red = np.array([10,255,255])
        """

        mask_blue = cv2.inRange(hsv, lower_blue, upper_blue)
        #mask_green = cv2.inRange(hsv,lower_green, upper_green)
        #mask_red = cv2.inRange(hsv, lower_red, upper_red)

        result1 = cv2.bitwise_and(frame, frame, mask = mask_blue)
        #result2 = cv2.bitwise_and(frame, frame, mask = mask_green)
        #result3 = cv2.bitwise_and(frame, frame, mask = mask_red)

        if not result :
            print("Can not find blue")


        cv2.imshow('BLUE', result1)
        #cv2.imshow('GREEN',result2)
        #cv2.imshow('RED',result3)

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
