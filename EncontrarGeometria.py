import cv2
import numpy as np

def Circulos(mask,camara):
    if camara=='Foscam':
        circles = cv2.HoughCircles(mask, cv2.HOUGH_GRADIENT,1,20,
                            param1=180,param2=35,minRadius=0,maxRadius=0)
    else:
        circles = cv2.HoughCircles(mask, cv2.HOUGH_GRADIENT,1,20,
                            param1=200,param2=40,minRadius=0,maxRadius=0)
    return circles

