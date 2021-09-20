# Automatic Dice Roller

# Written by Max Tyree

from random import randint #importing the tools I will need

print ("Automatic Dice Roller")

x = "" #establishing my variable outside the loop

while x != "x": #making it so that when you input x it stops the while loop
    x = input("Press Enter to Roll") #gathering the input for when you want to roll the dice
    print(randint(0,6)) #printing a random number 1-6
