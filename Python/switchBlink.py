from gpiozero import LED #this library makes it easier to assign LEDs to pins.
import RPi.GPIO as GPIO #imports the gpio library
from time import sleep #makes it so that you just have to type sleep instead of time.sleep.
GPIO.setmode(GPIO.BCM) #sets the GPIO mode to BCM

green = LED(21) #assigning leds to variables
blue = LED(20)

while(True):
	blue.on() #blue goes on while green goes off for one second, then they switch
	green.off()
	sleep(1)
	blue.off()
	green.on()
	sleep(1)

