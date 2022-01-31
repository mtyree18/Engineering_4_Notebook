import time
import picamera

effects = ['colorswap', 'blur', 'colorpoint', 'film', 'solarize']

for i in effects:
	with picamera.PiCamera() as camera:
		print("running")
		camera.resolution = (1024, 768)
		camera.start_preview()
		time.sleep(2)
		camera.image_effect = i
		camera.capture('pic"{i}".jpg')
		print("done")
