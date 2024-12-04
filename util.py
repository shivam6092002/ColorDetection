import numpy as np 
import cv2
def get_limits(color):
    c=np.uint8([[color]])
    hsvc=cv2.cvtColor(c, cv2.COLOR_BGR2HSV)
    lower_limit=hsvc[0][0][0]-15,100,100
    upper_limit=hsvc[0][0][0]+15,255,255
    lower_limit=np.array(lower_limit,dtype=np.uint8)
    upper_limit=np.array(upper_limit,dtype=np.uint8)
    return lower_limit,upper_limit


