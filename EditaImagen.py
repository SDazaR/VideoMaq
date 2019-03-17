import numpy as np
import cv2
import Configuraciones as conf


def Undistort(frame,Camara):
    cam=conf.Cam(Camara)
    frame = cv2.undistort(frame, cam.camera_matrix, cam.dist_coefs,newCameraMatrix=cam.K_undistort)
    return frame
    

def Crop(frame, objetivo):
    width, height=frame.shape[:2]
    maq=conf.Maquina(objetivo)
    frame=frame[int(maq.height_inicio*width): int(maq.height_final*width), int(maq.width_inicio*height):int(maq.width_final*height)]
    return frame
    
def Suavizar(frame):
    frame = cv2.GaussianBlur(frame,(5,5),0)
    frame = cv2.medianBlur(frame,15)
    return frame
