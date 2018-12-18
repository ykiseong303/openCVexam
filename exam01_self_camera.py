import cv2



def run_camera(frame) :
    cv2.imshow('frame',frame)#, cv2.waitKey(1) & 0xFF



cap = cv2.VideoCapture(1)
if __name__ =='__main__' :

    while True :
        ret, frame = cap.read()
        run_camera(frame)
