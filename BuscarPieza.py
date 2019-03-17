import sys
import cv2
import numpy as np
import argparse
import EditaImagen as edit
import FiltroColor as filtro
import MoverFoscam
import EncontrarGeometria as findO
import Pixels2Coor
import Configuraciones as conf



global pt
pt=(0 , 0)
global k
k=1


def on_mouse(event, x, y, flags, param): #funcion al pulsar click izquierdo en ventana Varias Piezas

    global start
    global pt
    global k
    if event == cv2.EVENT_LBUTTONDOWN:
        pt = (x, y)
        k=1
        print 'Punto seleccionado'
        print pt

if __name__ == '__main__':
    
    #Define inputs del modulo
    parser = argparse.ArgumentParser(description='Busca y determina la posicion de objetos circulares para ejecutar Pick and Place')
    parser.add_argument('Objetivo', help='Objetivo de la maquina')
    parser.add_argument('Color', help='Color del objeto a tomar')
    parser.add_argument('Camara', help='Camara usada')
    parser.add_argument('Muestras', help='Cantidad de imagenes usadas para encontrar la pieza')
    args = parser.parse_args()
    
    maq= conf.Maquina(args.Objetivo)
    cam= conf.Cam(args.Camara)

    raw_input("Lleve maquina a "+ str(maq.home)+ "[m] y presione Enter")
    
    if cam.fuente==0:
        cap = cv2.VideoCapture(cam.fuente)
    else:
        cap = cv2.VideoCapture('rtsp://%s:%s@%s/videoMain'%(cam.usr,cam.pwd,cam.fuente))
        #MoverFoscam.LlevarA('TopMost',fuente);
    
    j=0 #Contador de muestras tomadas
    muestras=int(args.Muestras)
    centros=np.empty([muestras, 2])#Matriz con centros de cada muestra
    suma=np.empty([1,2]) #Suma de las coordenadas de centros
    coorinvpix=np.empty([1,2]) #Coordenadas en pixeles (invertido x con y) de la pieza observada
       
    while True:
        ret, frame = cap.read()
        
        #Edicion de imagen tomada 
        try:
            #frame=edit.Undistort(frame)
            frame=edit.Crop(frame, args.Objetivo)
            mask=filtro.Color(frame, args.Color)
            mask=edit.Suavizar(mask) 
        except:
            print 'No se pudo obtener imagen'
            break
        
        #Busca circulos    
        circles=findO.Circulos(mask,args.Camara) 
        
        #En caso de que se haya activado multipieza, filtra solo la escogida por el usuario
        if pt[1] is not int(0) and pt[0] is not int (0):
            if circles is not None and j<muestras and circles.shape[1] is not int(1):
                for i in circles[0,:]:
                    if pt[0]-10<i[0] and pt[0]+10>i[0] and pt[1]-10<i[1] and pt[1]+10>i[1]:
                        circles[0,0]=[i[0],i[1], i[2]]                        
                circles=np.resize(circles,(1,1,3))
        
        if circles is not None: 
            
            #Existen multipiezas, crea ventana Varias Piezas hasta que el usuario selecciona centro de la pieza objetivo
            if circles.shape[1] is not int(1) and k==1 and j<muestras:
                cv2.namedWindow('Varias Piezas')
                cv2.setMouseCallback('Varias Piezas', on_mouse, 0)
                cv2.moveWindow('Varias Piezas', 740, 0)
                print "Seleccione el centro de la pieza objetivo"
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
                    centros[j]=[i[0],i[1]]
                    if j==0:
                        print "Tomando ", args.Muestras, " muestras"
                        suma[0]=centros[j]
                    else:
                        sys.stdout.write("\r" + str((j+1)*100/muestras)+'/% Completado')
                        sys.stdout.flush()
                        #print('{}',format(, end='\r')
                        suma[0]=centros[j]+suma[0]
                    j=j+1
                # draw the outer circle
                cv2.circle(frame,(i[0],i[1]),i[2],(0,255,0),2)
                # draw the center of the circle
                cv2.circle(frame,(i[0],i[1]),2,(0,0,255),3)
             
        #Una vez tomadas todas las muestras, calcula el promedio   
        if j==muestras:
            print
            coorinvpix=suma/muestras
            
            #Convertir coordenadas en pixeles invertidas a un punto segun la Maya
            punto=Pixels2Coor.Pix2Coor(frame,coorinvpix,args.Objetivo)
            print "Las coordenadas de la pieza en ", args.Objetivo, " son ", punto, "[m]"
            j=j+1
            break          

        #Abre ventana para observar la imagen analizada
        #cv2.imshow('frame', frame)
        #cv2.imshow('mask', mask)
        
        #Se interrumpe en caso de oprimir "q"
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    
    cap.release()
    cv2.destroyAllWindows()
    del(cap)
