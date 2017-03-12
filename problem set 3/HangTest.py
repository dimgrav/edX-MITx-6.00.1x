# -*- coding: utf-8 -*-
"""
Created on Mon Feb  6 20:47:29 2017

@author: Mitsakos
"""
secretWord = 'apple'
#lettersGuessed = ['a', 'e', 'i', 'k', 'p', 'r', 's']
lettersGuessed = []

# code to check if all word letters are guessed
count = 0
for letter in lettersGuessed:
    if letter in secretWord:
        count += 1
    
if count == len(secretWord):
    print(True)
else:
    print(False)

# code to check if a letter exists in the secret word
wordUI = list(secretWord)

for i in range(len(wordUI)):
    if wordUI[i] not in lettersGuessed:
        wordUI[i] = "_"

print (" ".join(wordUI))

# code for remaining available letters to guess
az = list("abcdefghijklmnopqrstuvwxyz")

avail = sorted(set(az) - set(lettersGuessed))

print ("".join(avail))

# hangman implementation
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

secretWord = chooseWord(wordlist).lower()
hangman(secretWord)