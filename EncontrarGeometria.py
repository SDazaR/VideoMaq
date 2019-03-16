import cv2
import numpy as np
import Configuraciones as conf

def Circulos(mask,camara):
    cam=conf.Cam(camara)
    circles = cv2.HoughCircles(mask, cv2.HOUGH_GRADIENT,1,20,param1=cam.par1,param2=cam.par2,minRadius=0,maxRadius=0)
    return circles
