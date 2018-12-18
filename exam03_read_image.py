import numpy as np
import cv2

def showImage() :
    imgfile = 'exam_image/exam03.png'
    img = cv2.imread(imgfile, cv2.IMREAD_COLOR)

    cv2.namedWindow('model',cv2.WINDOW_NORMAL)
    cv2.imshow('exam03',img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

showImage()
