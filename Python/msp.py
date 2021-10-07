# Python Program 04 - MSP (ENGR4)

#Written by Max Tyree

#9.23.2021

def clearScreen():
    print ("\n" * 50)
    
def wordLength():
    print (emptyString)
    
def pinata():
    if (len(missedGuess) >= 1):
        print("_______")
        print("      |")
        print("      O")
    if (len(missedGuess) == 2):
        print("      |")
    elif (len(missedGuess) == 3):
        print("      |--  ")
    elif (len(missedGuess) >= 4):
        print("    --|--  ")
    if (len(missedGuess) == 5):
        print("      \ ")
    elif (len(missedGuess) >= 6):
        print("     /\ ")
        print("YOU LOSE HAHAHA")
        
        
word = input("Player 1 what's the word")
length = len(word)
emptyString = ("_" * length)
correctGuess = ""
missedGuess = ""

wordLength()

while (True):
    guess = input("Player 2, guess a letter")
    if (guess in word):
        correctGuess = correctGuess + guess
        print("Correct Guesses: " + correctGuess)
    else:
        missedGuess = missedGuess + guess
        pinata()
        
    for i in range (0, len(word)):
        if ((word[i]) in correctGuess):
            emptyString = emptyString[:i] + word[i] + emptyString [i+1:]
    print (emptyString)
