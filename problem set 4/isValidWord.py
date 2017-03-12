# -*- coding: utf-8 -*-
"""
Created on Wed Feb 15 21:17:21 2017

@author: Mitsakos
"""

def isValidWord(word, hand, wordList):
    """
    Returns True if word is in the wordList and is entirely
    composed of letters in the hand. Otherwise, returns False.

    Does not mutate hand or wordList.
   
    word: string
    hand: dictionary (string -> int)
    wordList: list of lowercase strings
    """
    if word in wordList:
        for letter in word:
            if letter in hand.keys() and word.count(letter) == hand[letter]:
                return True
            else:
                return False
    else:
        return False