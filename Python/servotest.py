import time
import board
import adafruit_mpl3115a2
from gpiozero import Servo

myGPIO = 18

servo = Servo(myGPIO)

while True:
	servo.mid()

	time.sleep(1)

	servo.max()

	time.sleep(1)

	servo.min()

	time.sleep(1)
