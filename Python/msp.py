# Python Program 04 - MSP (ENGR4)

#Written by Max Tyree

#9.23.2021

def clearScreen():
    print ("\n" * 50)
    
def wordLength():
    length = len(word)
    print ("_" * length)

word = input("Player 1 what's the word")

clearScreen()
wordLength()

guess = input("Player 2, guess a letter")
