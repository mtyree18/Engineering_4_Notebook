# Python Program 04 - MSP (ENGR4)

#Written by Max Tyree

#9.23.2021

def clearScreen():
    print ("\n" * 50)
    
def wordLength():
    print (emptyString)
    
word = input("Player 1 what's the word")
guess = input("Player 2, guess a letter")
length = len(word)
emptyString = ("_ " * length)
correctGuess = ""
missedGuess = ""

wordLength()

while (True):
    guess = input("Player 2, guess a letter")
    for x in word:
        if (guess == x):
            correctGuess = correctGuess + guess
        else:
            missedGuess = missedGuess + guess
    for i in range (0, len(word)):
        if ((word[i]) in correctGuess):
            emptyString = emptyString[:i] + guess + emptyString [i+1:]
        else:
            break
    print (emptyString)
