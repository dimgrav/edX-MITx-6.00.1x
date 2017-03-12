# -*- coding: utf-8 -*-
"""
Created on Fri Feb 17 19:21:40 2017

@author: Mitsakos
"""

def playGame(wordList):
    """
    Allow the user to play an arbitrary number of hands.
 
    1) Asks the user to input 'n' or 'r' or 'e'.
      * If the user inputs 'n', let the user play a new (random) hand.
      * If the user inputs 'r', let the user play the last hand again.
      * If the user inputs 'e', exit the game.
      * If the user inputs anything else, tell them their input was invalid.
 
    2) When done playing the hand, repeat from step 1
    """
    
    counter = 0
    
    while True:
        start = str(input("Enter n to deal a new hand, r to replay the last hand, or e to end game: "))
        
        if start not in "nre":
            print("Invalid command.")
        elif start == "e":
            break
        elif start == "n":
            
            # deals a hand
            deal = dealHand(HAND_SIZE)
            counter += 1
            # plays the hand
            playHand(deal, wordList, HAND_SIZE)
        elif start == "r":
            if counter == 0:
                print("You have not played a hand yet. Please play a new hand first!")
            else:
                playHand(deal, wordList, HAND_SIZE)