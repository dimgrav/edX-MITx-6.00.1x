# -*- coding: utf-8 -*-
"""
Created on Thu Feb 16 11:18:42 2017

@author: mitsakos
"""

def playHand(hand, wordList, n):
    """
    Allows the user to play the given hand, as follows:

    * The hand is displayed.
    * The user may input a word or a single period (the string ".") 
      to indicate they're done playing
    * Invalid words are rejected, and a message is displayed asking
      the user to choose another word until they enter a valid word or "."
    * When a valid word is entered, it uses up letters from the hand.
    * After every valid word: the score for that word is displayed,
      the remaining letters in the hand are displayed, and the user
      is asked to input another word.
    * The sum of the word scores is displayed when the hand finishes.
    * The hand finishes when there are no more unused letters or the user
      inputs a "."

      hand: dictionary (string -> int)
      wordList: list of lowercase strings
      n: integer (HAND_SIZE; i.e., hand size required for additional points)
      
    """
    
    # Keep track of the total score
    total = 0
    updated = hand.copy()
    # As long as there are still letters left in the hand:
    while calculateHandlen(hand) > 0:
        # Display the hand
        print("Current hand: ", end = "")
        displayHand(updated)
        # Ask user for input
        word = str(input('Enter word, or a "." to indicate that you are finished: '))
        # If the input is a single period:
        if word == ".":
            # End the game (break out of the loop)
            return "Goodbye! Total score: " + str(total) + " points."
            break
            
        # Otherwise (the input is not a single period):
        else:
            # If the word is not valid:
            if isValidWord(word, hand, wordList) == False:
                # Reject invalid word (print a message followed by a blank line)
                print("Invalid word, please try again.")
                print()
            # Otherwise (the word is valid):
            else:
                # Tell the user how many points the word earned, and the updated total score, in one line followed by a blank line
                total += getWordScore(word, n)
                print(' " ' + str(word) + ' " ' + " earned " + str(getWordScore(word, n)) + " points. Total: " + str(total) + " points")
                # Update the hand
                for letter in updated:
                    if letter in word:
                        updated[letter] = updated.get(letter, 0) - word.count(letter)
        
                if all(value == 0 for value in updated.values()):
                    break
                
    # Game is over (user entered a '.' or ran out of letters), so tell user the total score
    return "Run out of letters. Total score: " + str(total) + " points."