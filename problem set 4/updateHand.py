# -*- coding: utf-8 -*-
"""
Created on Wed Feb 15 19:02:40 2017

@author: Mitsakos
"""

def updateHand(hand, word):
    """
    Assumes that 'hand' has all the letters in word.
    In other words, this assumes that however many times
    a letter appears in 'word', 'hand' has at least as
    many of that letter in it. 

    Updates the hand: uses up the letters in the given word
    and returns the new hand, without those letters in it.

    Has no side effects: does not modify hand.

    word: string
    hand: dictionary (string -> int)    
    returns: dictionary (string -> int)
    """
    # create hand copy    
    updated = hand.copy()
    wordlen = 0
    
    # remove letters used in word
    for letter in updated:
        if letter in word:
            updated[letter] = updated.get(letter, 0) - word.count(letter)
            wordlen += word.count(letter)
        
    if wordlen == len(word):
            hand = updated
    
    return hand