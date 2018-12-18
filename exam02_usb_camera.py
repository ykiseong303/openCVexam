# -*- coding: utf-8 -*-

import cv2



def run_camera() :

    cap = cv2.VideoCapture(1)
    print("press q to exit")

    pic_num = 0
    #rect_num = 0
    #circ_num = 0
    while(cap.isOpened()):
    #Capture frame-by-frame
        ret, frame = cap.read()
        if ret==True:
            cv2.imshow('frame',frame)
	    if  pic_num != 0 :
		break
            if cv2.waitKey(1) == 1048689: #if q is pressed
                break

#When everything done, release the capture
   # cap.release()
    cv2.destroyAllWindows()
    cap.release()


if __name__ == '__main__':
    #i = 1
    #pic_num = 0
    #last_pic = 0
    while(True) :
       run_camera()
       #print("while")
       run_inference_on_image()
