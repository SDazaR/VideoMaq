import requests
import time

def LlevarA(PresetPoint):
    try:
        params = (('cmd', 'ptzGotoPresetPoint'),('name', PresetPoint),('usr', 'maya'),('pwd', 'maya'),)

        response = requests.get('http://192.168.1.71:88//cgi-bin/CGIProxy.fcgi', params=params)

        time.sleep(1)
    except:
        print "No existe el Preset Point especificado"
