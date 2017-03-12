# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
print("Please think of a number between 0 and 100!")
low = 0
high = 100
correct = False

while not correct:
    guess = int(low + (high - low)/2)
    print("Is your secret number ", guess, "?")
    hint = str(input("Enter 'h' to indicate the guess is too high. Enter 'l' to indicate the guess is too low. Enter 'c' to indicate I guessed correctly."))
    if hint == "c":
        print("Game over. Your secret number was: " + str(guess))
        correct = True
    elif hint == "h":
        high = guess
    elif hint == "l":
        low = guess
    else:
        print("Sorry, I did not understand your input.")
        