# Automatic Dice Roller

# Written by Max Tyree

from random import randint

print ("Automatic Dice Roller")

while True:
    y = int(float(input("How many sides do you want on your dice?: ")))
    z = int(float(input("How many dice do you want to roll?: ")))
    x = int(float(input("Press Enter to Roll")))
    print(randint(0,z*y*6))
