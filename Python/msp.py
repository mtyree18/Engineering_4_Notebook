# Python Program 04 - MSP (ENGR4)

#Written by Max Tyree

#9.23.2021

def clearScreen(): #This function clears the screen so that player two cannot see the word
    print ("\n" * 50)
    
def wordLength(): #This function displays the length of the word
    print (emptyString)
    
def pinata(): #This function provides the basis for how the actual hangman graphics work
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

word = input("Player 1 what's the word") #Gets the word
length = len(word)
emptyString = ("_" * length) #displaying the length of the word
correctGuess = "" #establishing the correct and missed words banks
missedGuess = ""

wordLength()

while (emptyString != word): #runs only when you have not guessed the word
    guess = input("Player 2, guess a letter") #gathers the players guessed letter
    if (guess in word):
        correctGuess = correctGuess + guess
        print("Correct Guesses: " + correctGuess) #adding the correct guess to the correct guess bank
    else:
        missedGuess = missedGuess + guess
        pinata() #calls the function to build the hangman
        
    for i in range (0, len(word)):
        if ((word[i]) in correctGuess):
            emptyString = emptyString[:i] + word[i] + emptyString [i+1:] #displays the empty string up to the point where the correct guess matches the letter, then adds the correct letter to the empty string, then displays the rest of the empty string
    print(emptyString)
    if(len(correctGuess) == len(emptyString)): #if the correct guess bank matches the empty string (which is now filled with correct guesses), then you win and the code ends       
        print("YOU WONNNNNNN!!!!!! YAYYYYYYYY")
        break
    if(len(missedGuess) == 6): #if missed guesses gets to six then you lose
        print("smh u suck")
        break
