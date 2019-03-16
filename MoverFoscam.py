import requests
import time
import Configuraciones as conf

def LlevarA(PresetPoint,Camara):
    cam=conf.Cam(Camara)
    try:
        params = (('cmd', 'ptzGotoPresetPoint'),('name', PresetPoint),('usr', cam.usr),('pwd', cam.pwd),)
        response = requests.get('http://%s/cgi-bin/CGIProxy.fcgi'%cam.fuente, params=params)
        time.sleep(1)
    except:
        print "No existe el Preset Point especificado"
