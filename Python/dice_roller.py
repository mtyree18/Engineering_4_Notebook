# Automatic Dice Roller

# Written by Max Tyree

from random import randint

print ("Automatic Dice Roller")

x = ""

while x != "x":
    x = input("Press Enter to Roll")
    print(randint(0,6))
