import numpy as np
import cv2


def Undistort(frame):
    camera_matrix=np.array([[999.1982933932153, 0.0, 644.6254385658015], [0.0, 1036.0246943682293, 356.0518358525304], [0.0, 0.0, 1.0]])
    dist_coefs=np.array([[-0.23440000955155973, 0.04006162073823348, 0.0034977324574391074, 0.004051180386141409, 0.07402326031102507]])
    K_undistort=np.array([[999.1982933932153, 0.0, 644.6254385658015], [0.0, 1036.0246943682293, 356.0518358525304], [0.0, 0.0, 1.0]])
    frame = cv2.undistort(frame, camera_matrix, dist_coefs,newCameraMatrix=K_undistort)
    return frame
    


def Crop(frame, objetivo):
    width, height=frame.shape[:2]
    if objetivo== 'Buffer':
        height_inicio=height*405/1080
        height_final=height*930/1080
        width_inicio=width*215/720
        width_final=width*640/720
    elif objetivo== 'SDV':
        height_inicio=height*360/1080
        height_final=height*720/1080
        width_inicio=width*240/720
        width_final=width*480/720
    else:
        height_inicio=1
        height_final=height
        width_inicio=1
        width_final=720
    frame=frame[width_inicio:width_final, height_inicio: height_final]
    return frame
    
def Suavizar(frame):
    frame = cv2.GaussianBlur(frame,(5,5),0)
    frame = cv2.medianBlur(frame,15)
    return frame
