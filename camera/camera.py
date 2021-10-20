from picamera import PiCamera, camera
from time import sleep

camera = PiCamera()

camera.start_preview()
sleep(5)
camera.stop_preview()