from picamera import PiCamera, camera
from time import sleep

camera = PiCamera()

camera.stop_preview()
sleep(5)
camera.capture('/home/pi/Desktop/image.jpg')
camera.stop_preview()