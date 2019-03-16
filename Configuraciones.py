import math
import numpy as np
        
###Atributos de las Maquinas

#S1: Sistema coordenado de la maquina
#S2: Sistema coordenado en el piso con las esquinas de lo observado por la camara
#O: Coordenadas del origen de S2 respecto a S1
#Ang: Angulo de rotacion sobre el eje Z de S2 respecto a S1
#CFos: Coordenadas de la camara respecto a S1
#H: Altura de la pieza
#xp2co: Constante para escalar/pasar de pixeles a mm en el eje X (alto en mm/heigh de muestra tomada)
#yp2co: Constante para escalar/pasar de pixeles a mm en el eje Y (ancho en mm/width de muestra tomada)
        
#width_inicio: Limite izquierdo para el crop de la imagen
#width_final: Limite derecho para el crop de la imagen
#height_inicio: Limite superior para el crop de la imagen
#height_final: Limite inferior para el crop de la imagen


###Atributos de las Camaras

#camera_matrix: Matriz de calibracion de la camara utilizada
#dist_coefs: Coeficentes de distorcion de la camara utilizada
#K_undistort: Constante K de distorsion de la camara utilizada
        
#fuente: Direccion ip de la camara
#usr: Usuario valido para usar la camara
#pwd: Contrasen_a para el usuario especificado
        
#par1: Parametro 1 para deteccion de circulos segun la camara
#par2: Parametro 2 para deteccion de circulos segun la camara

class Maquina:
    def __init__(self, objetivo):
        if objetivo== 'Buffer': #Actualizado
            self.O=(1775,-105,50) 
            self.Ang=-math.pi/2+math.pi*0.07
            self.CFos=np.array([[1435],[195],[2210]])
            self.H=1040
            self.xp2co= 890
            self.yp2co= 1514
                
            self.width_inicio=405.0/1080.0
            self.width_final=930.0/1080.0
            self.height_inicio=215.0/720.0
            self.height_final=640.0/720.0
        elif objetivo== 'SDVMaya':
            self.O=(900,58,0)
            self.Ang=math.pi/2+math.pi/36
            self.CFos=np.array([[480],[1375],[2190]])
            self.H=400 
            self.xp2co= 550.0
            self.yp2co= 960.0
        
            self.width_inicio=360.0/1080.0
            self.width_final=720.0/1080.0
            self.height_inicio=240.0/720.0
            self.height_final=480.0/720.0
        elif objetivo== 'SDVMotoman': #Actualizado
            self.O=(108.018+25,-545.98-25,-1785.76)
            self.Ang=math.pi
            self.CFos=np.array([[-293.285+95+25],[-910.184-25],[-110.724-141]])
            self.H=370
            self.xp2co= 690.0
            self.yp2co= 690.0
    
            self.width_inicio=360.0/1080.0
            self.width_final=720.0/1080.0
            self.height_inicio=150.0/720.0
            self.height_final=600.0/720.0
        else:
            self.O=(900,58,0)
            self.Ang=math.pi/2+math.pi/36
            self.CFos=np.array([[480],[1375],[2190]])
            self.H=400
            self.xp2co= 550.0
            self.yp2co= 960.0
        
            self.width_inicio=1/1080
            self.width_final=1
            self.height_inicio=1/720
            self.height_final=1
class Cam:
    def __init__(self, Camara):
        if Camara== 'Web':#Actualizado
            self.fuente=0
            self.usr=0
            self.pwd=0
            
            self.camera_matrix=np.array([[999.1982933932153, 0.0, 644.6254385658015], [0.0, 1036.0246943682293
            , 356.0518358525304], [0.0, 0.0, 1.0]])
            self.dist_coefs=np.array([[-0.23440000955155973, 0.04006162073823348, 0.0034977324574391074
            , 0.004051180386141409, 0.07402326031102507]])
            self.K_undistort=np.array([[999.1982933932153, 0.0, 644.6254385658015], [0.0, 1036.0246943682293
            , 356.0518358525304], [0.0, 0.0, 1.0]])
            
            self.par1=200
            self.par2=40
        elif Camara== 'FoscamMotoman':#Actualizado
            self.fuente='192.168.1.34:88'
            self.usr='motoman'
            self.pwd='motoman'
            
            self.camera_matrix=np.array([[999.1982933932153, 0.0, 644.6254385658015], [0.0, 1036.0246943682293
            , 356.0518358525304], [0.0, 0.0, 1.0]])
            self.dist_coefs=np.array([[-0.23440000955155973, 0.04006162073823348, 0.0034977324574391074
            , 0.004051180386141409, 0.07402326031102507]])
            self.K_undistort=np.array([[999.1982933932153, 0.0, 644.6254385658015], [0.0, 1036.0246943682293
            , 356.0518358525304], [0.0, 0.0, 1.0]])
            self.par1=180
            self.par2=30
        elif Camara== 'FoscamMaya': #Actualizado
            self.fuente='192.168.1.71:88'
            self.usr='maya'
            self.pwd='maya'
        
            self.camera_matrix=np.array([[999.1982933932153, 0.0, 644.6254385658015], [0.0, 1036.0246943682293
            , 356.0518358525304], [0.0, 0.0, 1.0]])
            self.dist_coefs=np.array([[-0.23440000955155973, 0.04006162073823348, 0.0034977324574391074
            , 0.004051180386141409, 0.07402326031102507]])
            self.K_undistort=np.array([[999.1982933932153, 0.0, 644.6254385658015], [0.0, 1036.0246943682293
            , 356.0518358525304], [0.0, 0.0, 1.0]])
            
            self.par1=180
            self.par2=30
        else:
            self.fuente=0
            self.usr=0
            self.pwd=0
            
            self.camera_matrix=np.array([[999.1982933932153, 0.0, 644.6254385658015], [0.0, 1036.0246943682293
            , 356.0518358525304], [0.0, 0.0, 1.0]])
            self.dist_coefs=np.array([[-0.23440000955155973, 0.04006162073823348, 0.0034977324574391074
            , 0.004051180386141409, 0.07402326031102507]])
            self.K_undistort=np.array([[999.1982933932153, 0.0, 644.6254385658015], [0.0, 1036.0246943682293
            , 356.0518358525304], [0.0, 0.0, 1.0]])
            
            self.par1=200
            self.par2=20


