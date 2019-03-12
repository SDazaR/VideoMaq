import numpy as np
import math
from numpy.linalg import inv

def Pix2Coor(frame,coorinvpix,objetivo):
    width, height=frame.shape[:2]
    coorpix=np.empty([1,1])
    #camara saca coor x,y. Hay que cambiarlo a y,x
    coorpix=np.array([coorinvpix[0,1], coorinvpix[0,0]])
    if objetivo== 'Buffer':
        O=(1870,-68,0) #Coordenadas del origen del sistema cartesiano de la camara (S2) respecto al sistema coordenado de la Maya (S1)
        Ang=-math.pi/2+math.pi*0.02    #Angulo de rotacion sobre el eje Z de S2 respecto a S1
        CFos=np.array([[1520],[280],[2210]]) #Coordenadas de la camara respecto a S1
        H=1000 #Altura de la pieza.
        xp2co= 925/width #Constante para escalar/pasar de pixeles a mm en el eje X
        yp2co= 1420/height #Constante para escalar/pasar de pixeles a mm en el eje Y
    elif objetivo== 'SDV':
        O=(900,58,0) #Coordenadas del origen del sistema cartesiano de la camara (S2) respecto al sistema coordenado de la Maya (S1)
        Ang=math.pi/2+math.pi/36 #Angulo de rotacion sobre el eje Z de S2 respecto a S1
        CFos=np.array([[480],[1375],[2190]]) #Coordenadas de la camara respecto a S1
        H=400 #Altura de la pieza.
        xp2co= 550.0/width #Constante para escalar/pasar de pixeles a mm en el eje X
        yp2co= 960.0/height #Constante para escalar/pasar de pixeles a mm en el eje Y
    else:
        O=(900,58,0) #Coordenadas del origen del sistema cartesiano de la camara (S2) respecto al sistema coordenado de la Maya (S1)
        Ang=math.pi/2+math.pi/36 #Angulo de rotacion sobre el eje Z de S2 respecto a S1
        CFos=np.array([[480],[1375],[2190]]) #Coordenadas de la camara respecto a S1
        H=400 #Altura de la pieza.
        xp2co= 550.0/width #Constante para escalar/pasar de pixeles a mm en el eje X
        yp2co= 960.0/height #Constante para escalar/pasar de pixeles a mm en el eje Y

  
    
    MT1=np.array([[1,0,0,-O[0]],[0,1, 0, -O[1]],[0,0,1,O[2]],[0,0,0,1]])#Matriz de transformacion por traslacion
    MT2=np.array([[math.cos(Ang),-math.sin(Ang),0,0],[math.sin(Ang), math.cos(Ang), 0, 0],[0,0,1,0],[0,0,0,1]])#Matriz de transformacion de rotacion
    MT=MT2.dot(MT1) #Matriz de transformacion para pasar de S1 a S2
    MTinv=inv(MT) #Matriz de transformacion para pasar de S2 a S1
    
    CFosp=MT.dot(np.append(CFos,[1]))
    CFosp=CFosp[0:-1] #Coordenadas de la camara respecto a S2
    

    
    coo=np.array([coorpix[0]*xp2co,coorpix[1]*yp2co,0]) #Coordenadas en milimetros de la pieza segun S2
    vec=CFosp-coo #Vector director d la recta que pasa a traves del punto observado por la camara y las coordenadas de la camara en S2
    t=(H-coo[2])/vec[2] #parametro para la forma parametrica de la recta
    puntoCam=coo+t*vec #Punto en coordenadas de la camara en milimetros donde esta la pieza segun S2
    punto=MTinv.dot(np.append(puntoCam,[1]))
    punto=punto[0:-1] #Punto donde esta la pieza en S1
    punto=(punto+[0, 0,25])/1000
    #distancia=math.sqrt(math.pow((CFos-punto)[0],2)+math.pow((CFos-punto)[1],2)+math.pow((CFos-punto)[2],2))
    
    return punto

