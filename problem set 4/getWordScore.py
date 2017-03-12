# -*- coding: utf-8 -*-
"""
Created on Wed Feb 15 10:56:55 2017

@author: mitsakos
"""

def getWordScore(word, n):
    
    SCRABBLE_LETTER_VALUES = {
    'a': 1, 'b': 3, 'c': 3, 'd': 2, 'e': 1, 'f': 4, 'g': 2, 'h': 4, 'i': 1, 'j': 8, 'k': 5, 'l': 1, 'm': 3, 'n': 1, 'o': 1, 'p': 3, 'q': 10, 'r': 1, 's': 1, 't': 1, 'u': 1, 'v': 4, 'w': 4, 'x': 8, 'y': 4, 'z': 10
}
    
    # inital word score and letters sum score
    wscore = 0
    lscore = 0
    
    # calculate letters sum score
    for letter in word:
        if letter in SCRABBLE_LETTER_VALUES.keys():
            lscore += SCRABBLE_LETTER_VALUES[letter]
            
    # calculate word score
    if len(word) == n:
        wscore = lscore*n + 50
    else:
        wscore = lscore*len(word)
    
    return wscore