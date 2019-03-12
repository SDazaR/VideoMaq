import cv2
import numpy as np
import requests
import time
import argparse
import EditaImagen as edit
import FiltroColor as filtro
import MoverFoscam
import EncontrarGeometria as findO
import Pixels2Coor


global pt
pt=(0 , 0)
global k
k=1

def on_mouse(event, x, y, flags, param): #funcion al pulsar click izquierdo en ventana frame2

    global start
    global pt
    global k
    if event == cv2.EVENT_LBUTTONDOWN:
        pt = (x, y)
        k=1
        print "Punto seleccionado"
        print pt


if __name__ == '__main__':
    
    #Define inputs del modulo
    parser = argparse.ArgumentParser(description='Busca y determina la posicion de objetos circulares para ejecutar Pick and Place con el Robot Maya')
    parser.add_argument('Objetivo', help='Objetivo de la Maya (SDV, Buffer)')
    parser.add_argument('Color', help='Color del objeto a tomar (rojo, verde, azul)')
    parser.add_argument('Camara', help='Marca de la camara usada')
    parser.add_argument('Muestras', help='Cantidad de imagenes usadas para encontrar la pieza')
    args = parser.parse_args()
    
    if args.Camara=='Foscam': #Mueve la Foscam a TopMost y elije la Foscam como fuente de video
        MoverFoscam.LlevarA('TopMost');
        fuente="rtsp://maya:maya@192.168.1.71:88/videoMain"
    else: #Elije la camara web como fuente
        fuente=0
        
    cap = cv2.VideoCapture(fuente);#Captura video segun la fuente
    
    j=0 #Contador de muestras tomadas
    muestras=int(args.Muestras)
    centros=np.empty([muestras, 2])#Matriz con centros de cada muestra
    suma=np.empty([1,2]) #Suma de las coordenadas de centros
    coorinvpix=np.empty([1,2]) #Coordenadas en pixeles (invertido x con y) de la pieza observada
    
    
    while True:
        ret, frame = cap.read()
        
        #Edicion de imagen tomada
        
        try:
            frame=edit.Undistort(frame)
            frame=edit.Crop(frame, args.Objetivo)
            mask=filtro.Color(frame, args.Color)
            mask=edit.Suavizar(mask) 
        except:
            print ('No se pudo obtener imagen')
            break
        
        #Busca circulos
              
        circles=findO.Circulos(mask,args.Camara) 
        
        #En caso de que se haya activado multipieza, filtra solo la escogida por el usuario
        if pt[1] is not int(0) and pt[0] is not int (0):
            if circles is not None and j<muestras and circles.shape[1] is not int(1):
                for i in circles[0,:]:
                    if pt[0]-30<i[0] and pt[0]+30>i[0] and pt[1]-30<i[1] and pt[1]+30>i[1]:
                        circles[0,0]=[i[0],i[1], i[2]]
                        print "circulo", circles
                    else:
                        circles[0,0]=[centros[j-1][0],centros[j-1][1],i[2]]
                        
                circles=np.resize(circles,(1,1,3))
        

        
        if circles is not None:
            
            
            #Existen multipiezas, crea ventana frame2 hasta que el usuario selecciona centro de la pieza objetivo
            if circles.shape[1] is not int(1) and k==1 and j<muestras:
                cv2.namedWindow('Varias Piezas')
                cv2.setMouseCallback('Varias Piezas', on_mouse, 0)
                cv2.moveWindow('Varias Piezas', 540, 260)
                print "Seleccione el centro de la pieza objetivo"
                print circles
                for i in circles[0,:]:
                    # draw the outer circle
                    cv2.circle(frame,(i[0],i[1]),i[2],(0,255,0),2)
                    # draw the center of the circle
                    cv2.circle(frame,(i[0],i[1]),2,(0,0,255),3)
                    cv2.imshow('Varias Piezas', frame)
                k=0
                    
            #Toma las muestras y guarda los centros hayados
            for i in circles[0,:]:
                if j<muestras and k==1:
                    print "muestra ",j+1, [i[0],i[1]]
                    centros[j]=[i[0],i[1]]
                    if j==0:
                        suma[0]=centros[j]
                    else:
                        suma[0]=centros[j]+suma[0]
                    j=j+1
                # draw the outer circle
                cv2.circle(frame,(i[0],i[1]),i[2],(0,255,0),2)
                # draw the center of the circle
                cv2.circle(frame,(i[0],i[1]),2,(0,0,255),3)
             
        #Una vez tomadas todas las muestras, calcula el promedio   
        if j==muestras:
            coorinvpix=suma/muestras
            
            #Convertir coordenadas en pixeles invertidas a un punto segun la Maya
            punto=Pixels2Coor.Pix2Coor(frame,coorinvpix,args.Objetivo)
            print "El punto es ", punto
            j=j+1          
        
        #Abre ventana para observar la imagen analizada
        cv2.imshow('frame', frame)
        cv2.imshow('mask', mask)
        
        #Se interrumpe en caso de oprimir "q"
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    
    cap.release()
    cv2.destroyAllWindows()
    del(cap)
