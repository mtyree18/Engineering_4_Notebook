import time
import board
import adafruit_mpl3115a2


# Create sensor object, communicating over the board's default I2C bus
i2c = board.I2C()  # uses board.SCL and board.SDA

# Initialize the MPL3115A2.
sensor = adafruit_mpl3115a2.MPL3115A2(i2c)
# Alternatively you can specify a different I2C address for the device:
# sensor = adafruit_mpl3115a2.MPL3115A2(i2c, address=0x10)

# You can configure the pressure at sealevel to get better altitude estimates.
# This value has to be looked up from your local weather forecast or meteorological
# reports.  It will change day by day and even hour by hour with weather
# changes.  Remember altitude estimation from barometric pressure is not exact!
# Set this to a value in pascals:
sensor.sealevel_pressure = 102250

start = sensor.altitude

print(start)

max = 0

# Main loop to read the sensor values and print them every second.
while True:
    altitude = sensor.altitude - start
    print("Altitude: {0:0.3f} meters".format(altitude))
    time.sleep(1.0)
	if current > max:
		max = current
