# -*- coding: utf-8 -*-
"""
Created on Thu Feb 16 11:12:41 2017

@author: mitsakos
"""

def calculateHandlen(hand):
    """ 
    Returns the length (number of letters) in the current hand.
    
    hand: dictionary (string int)
    returns: integer
    """
    
    length = 0
    
    for letter in hand:
        length += hand[letter]
    
    return length