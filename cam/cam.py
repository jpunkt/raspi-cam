#!/usr/bin/env python3
import os
import signal
from subprocess import Popen

from gpiozero import Button
from picamera import PiCamera
from datetime import datetime

_must_stop = False


def main():
    btn1 = Button(26)
    btn2 = Button(19)
    btn3 = Button(13)
    btn4 = Button(6)
    shutter = Button(5)
    cam = PiCamera()
    pid = Popen(["fbcp", "&"]).pid

    def capture():
        today = datetime.now().strftime('%Y-%m-%d_%H-%M-%S')
        cam.capture('/home/pi/{0}.jpg'.format(today))

    def stop():
        global _must_stop
        _must_stop = True

    btn1.when_pressed = cam.start_preview
    btn2.when_pressed = cam.stop_preview
    btn4.when_pressed = stop
    shutter.when_pressed = capture
    try:
        while not _must_stop:
            pass
    except KeyboardInterrupt:
        pass
    finally:
        cam.stop_preview()
        os.kill(pid, signal.SIGKILL)
        cam.close()


if __name__ == '__main__':
    main()
