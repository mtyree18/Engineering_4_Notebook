# Python Program 04 - MSP (ENGR4)

#Written by Max Tyree

#9.23.2021

def clearScreen():
    print ("\n" * 50)

word = input("Player 1 what's the word")
length = len(word)
print ("_" * length)

clearScreen()

guess = input("Player 2, guess a letter")
