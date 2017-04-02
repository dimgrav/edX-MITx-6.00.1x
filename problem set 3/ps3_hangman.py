# Hangman game
import random

WORDLIST_FILENAME = "words.txt"

def loadWords():
    """
    Returns a list of valid words. Words are strings of lowercase letters.
    
    Depending on the size of the word list, this function may
    take a while to finish.
    """
    print("Loading word list from file...")
    # inFile: file
    inFile = open(WORDLIST_FILENAME, 'r')
    # line: string
    line = inFile.readline()
    # wordlist: list of strings
    wordlist = line.split()
    print("  ", len(wordlist), "words loaded.")
    return wordlist

def chooseWord(wordlist):
    """
    wordlist (list): list of words (strings)

    Returns a word from wordlist at random
    """
    return random.choice(wordlist)


# -----------------------------------
wordlist = loadWords()

def isWordGuessed(secretWord, lettersGuessed):
    '''
    secretWord: string, the word the user is guessing
    lettersGuessed: list, what letters have been guessed so far
    returns: boolean, True if all the letters of secretWord are in lettersGuessed;
      False otherwise
    '''
   count = 0
    
    for letter in lettersGuessed:
        if letter in secretWord:
            count += 1
    
    if count == len(secretWord):
        return True
    else:
        return False


def getGuessedWord(secretWord, lettersGuessed):
    '''
    secretWord: string, the word the user is guessing
    lettersGuessed: list, what letters have been guessed so far
    returns: string, comprised of letters and underscores that represents
      what letters in secretWord have been guessed so far.
    '''
    wordUI = list(secretWord)

    for i in range(len(wordUI)):
        if wordUI[i] not in lettersGuessed:
            wordUI[i] = "_"

    return " ".join(wordUI)



def getAvailableLetters(lettersGuessed):
    '''
    lettersGuessed: list, what letters have been guessed so far
    returns: string, comprised of letters that represents what letters have not
      yet been guessed.
    '''
    az = list("abcdefghijklmnopqrstuvwxyz")

    avail = sorted(set(az) - set(lettersGuessed))

    return "".join(avail)
    

def hangman(secretWord):
    '''
    secretWord: string, the secret word to guess.

    Starts up an interactive game of Hangman.

    * At the start of the game, let the user know how many 
      letters the secretWord contains.

    * Ask the user to supply one guess (i.e. letter) per round.

    * The user should receive feedback immediately after each guess 
      about whether their guess appears in the computers word.

    * After each round, you should also display to the user the 
      partially guessed word so far, as well as letters that the 
      user has not yet guessed.

    Follows the other limitations detailed in the problem write-up.
    '''
    # Game start and initial parameters
    print("Welcome to the game Hangman!")
    print("I am thinking of a word that is", len(secretWord), "letters long")
    print("_ _ _ _ _ _ _ _ _")
    
    lettersGuessed = []
    guesses = 8
    # Guessing the word in 8 tries
    while not isWordGuessed(secretWord, lettersGuessed) and guesses > 0:
        print("You have " + str(guesses) + " guesses left")        
        print("Available letters: " + getAvailableLetters(lettersGuessed))
        
        # If letter already used
        while True:
            guessLetter = str(input("Please guess a letter: ").lower())
            if guessLetter in lettersGuessed:
                print("Oops! You've already guessed that letter: " + getGuessedWord(secretWord, lettersGuessed))       
                print("_ _ _ _ _ _ _ _ _")
                print("You have " + str(guesses) + " guesses left")
                print("Available letters: " + getAvailableLetters(lettersGuessed))
            else:
                break
        lettersGuessed += guessLetter
        
        # If word is found
        if isWordGuessed(secretWord, lettersGuessed):
            print("Good guess: " + getGuessedWord(secretWord, lettersGuessed))
            print("_ _ _ _ _ _ _ _ _")
            print("Congratulations, you won!")
        # If guessedLetter in secretWord
        elif guessLetter in secretWord:
            print("Good guess: " + getGuessedWord(secretWord, lettersGuessed))
            print("_ _ _ _ _ _ _ _ _")        
        # If guessedLetter not in secretWord
        else:
            print("Oops! That letter is not in my word: " + getGuessedWord(secretWord, lettersGuessed))
            print("_ _ _ _ _ _ _ _ _")
            guesses -= 1
            
        # If all guesses are used
        if  guesses == 0:
            print("Sorry, you ran out of guesses. The word was " + secretWord + ".")
        

# Code testing
secretWord = chooseWord(wordlist).lower()
hangman(secretWord)
