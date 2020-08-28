from _signal import pause

from gpiozero import Button
from picamera import PiCamera
from datetime import datetime

import os


btn1 = Button(26)
btn2 = Button(19)
btn3 = Button(13)
btn4 = Button(6)

shutter = Button(5)

cam = PiCamera()

os.system('fbcp &')


def capture():
    today = datetime.now().strftime('%Y-%m-%d_%H-%M-%S')
    cam.capture('/home/pi/{0}.jpg'.format(today))


btn1.when_pressed = cam.start_preview
btn2.when_pressed = cam.stop_preview

shutter.when_pressed = capture

pause()

cam.close()
