from foscam import FoscamCamera
from time import sleep

mycam = FoscamCamera('192.168.1.71', 88, 'maya', 'maya')
mycam.ptz_move_down()
sleep(0.1)
mycam.ptz_stop_run()

#mycam.mirror_video(0)

#mycam.open_infra_led()

#http://192.168.1.61/cgi-bin/camctrl.cgi?[move=up]

