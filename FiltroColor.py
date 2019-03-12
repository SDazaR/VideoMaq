import numpy as np
import cv2

def Color(frame, color):
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
    if color=='rojo':
        lim_bajos = np.array([160,100,75])
        lim_altos = np.array([180, 255, 255])
        
        mask = cv2.inRange(hsv, lim_bajos, lim_altos)
    elif color=='verde':
        lim_bajos = np.array([49,100,100])
        lim_altos = np.array([107, 255, 255])
        mask = cv2.inRange(hsv, lim_bajos, lim_altos)
    elif color=='azul':
        lim_bajos = np.array([100,65,75])
        lim_altos = np.array([130, 255, 255])
        mask = cv2.inRange(hsv, lim_bajos, lim_altos)
    else:
        lim_bajos = np.array([0,0,0])
        lim_altos = np.array([180, 255, 255])
        mask = cv2.inRange(hsv, lim_bajos, lim_altos)
    return mask
    
