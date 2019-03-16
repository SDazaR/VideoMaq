import numpy as np
import math
from numpy.linalg import inv
import Configuraciones as conf

def Pix2Coor(frame,coorinvpix,objetivo):
    width, height=frame.shape[:2]
    coorpix=np.empty([1,1])
    #camara saca coor x,y. Se requiere que cambiarlo a y,x
    coorpix=np.array([coorinvpix[0,1], coorinvpix[0,0]])
    maq=conf.Maquina(objetivo)

    MT1=np.array([[1,0,0,-maq.O[0]],[0,1, 0, -maq.O[1]],[0,0,1,-maq.O[2]],[0,0,0,1]])#Matriz de transformacion por traslacion
    MT2=np.array([[math.cos(maq.Ang),-math.sin(maq.Ang),0,0],[math.sin(maq.Ang), math.cos(maq.Ang), 0, 0],[0,0,1,0],[0,0,0,1]])#Matriz de transformacion de rotacion
    MT=MT2.dot(MT1) #Matriz de transformacion para pasar de S1 a S2
    MTinv=inv(MT) #Matriz de transformacion para pasar de S2 a S1
    
    CFosp=MT.dot(np.append(maq.CFos,[1]))
    CFosp=CFosp[0:-1] #Coordenadas de la camara respecto a S2
    
    coo=np.array([coorpix[0]*maq.xp2co/height,coorpix[1]*maq.yp2co/width,0]) #Coordenadas en milimetros de la pieza segun S2
    vec=CFosp-coo #Vector director d la recta que pasa a traves del punto observado por la camara y las coordenadas de la camara en S2
    t=(maq.H-coo[2])/vec[2] #parametro para la forma parametrica de la recta
    puntoCam=coo+t*vec #Punto en coordenadas de la camara en milimetros donde esta la pieza segun S2
    punto=MTinv.dot(np.append(puntoCam,[1]))
    punto=punto[0:-1] #Punto donde esta la pieza en S1
    punto=(punto+[0, 0,0])/1000
    
    return punto
