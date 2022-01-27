import time
import picamera

with picamera.PiCamera() as camera:
	print("running")
	camera.resolution = (1024, 768)
	camera.start_preview()
	time.sleep(2)
	camera.capture('pic.jpg')
	print("done")
