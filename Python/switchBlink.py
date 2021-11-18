from gpiozero import LED
import RPi.GPIO as GPIO
from time import sleep
GPIO.setmode(GPIO.BCM)

green = LED(21)
blue = LED(20)

while(True):
	blue.on()
	green.off()
	sleep(1)
	blue.off()
	green.on()
	sleep(1)

