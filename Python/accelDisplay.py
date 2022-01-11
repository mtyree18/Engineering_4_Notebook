import time
import RPi.GPIO as GPIO

import Adafruit_GPIO.SPI as SPI
import Adafruit_SSD1306
import Adafruit_LSM303

lsm303 = Adafruit_LSM303.LSM303()

from PIL import Image
from PIL import ImageDraw
from PIL import ImageFont

# Raspberry Pi pin configuration:
RST = 24
# Note the following are only used with SPI:
DC = 23
SPI_PORT = 0
SPI_DEVICE = 0

disp = Adafruit_SSD1306.SSD1306_128_64(rst=RST, i2c_address=0x3d)

# Initialize library.
disp.begin()

# Clear display.
disp.clear()
disp.display()

# Create blank image for drawing.
# Make sure to create image with mode '1' for 1-bit color.
width = disp.width
height = disp.height
image = Image.new('1', (width, height))

#get drawing object to draw on image.
draw = ImageDraw.Draw(image)

#load font
font = ImageFont.load_default()

# Alternatively load a TTF font.  Make sure the .ttf font file is in the same directory as the python script!
# Some other nice fonts to try: http://www.dafont.com/bitmap.php
#font = ImageFont.truetype('Minecraftia.ttf', 8)

#black filled rectangle to clear space
draw.rectangle((0,0,width,height), outline=0, fill=0)

#defining spacing
padding = 2
top = padding
bottom = height-padding
x = padding

accel = lsm303.read()
accel_x, accel_y = accel
time.sleep(0.5)

# Write two lines of text.
draw.text((x, top),    accel_x,  font=font, fill=255)
draw.text((x, top+20), accel_y, font=font, fill=255)

disp.image(image)
# Pin definition
reset_pin = 24
