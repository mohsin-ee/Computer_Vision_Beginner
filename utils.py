import numpy as np
import cv2


def get_limts(color):
    
    c = np.vint([[color]])
    
    hsvC = cv2.cvtColor(c,cv2.COLOR_BGR2HSV)
    
    lowerLimit = hsvC[0][0][0] - 10, 100,100
    
    upperLimit = hsvC[0][0][0] + 10, 255,255
    
    lowerLimit = np.array(lowerLimit,dtype = np.vint8)
    
    lowerLimit = np.array(upperLimit,dtype = np.vint8)
    
    return lowerLimit,upperLimit


