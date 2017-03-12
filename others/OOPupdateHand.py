# -*- coding: utf-8 -*-
"""
Created on Sat Feb 18 14:25:51 2017

@author: Mitsakos
"""
def update(self, word):
    """
    Does not assume that self.hand has all the letters in word.

    Updates the hand: if self.hand does have all the letters to make
    the word, modifies self.hand by using up the letters in the given word.

    Returns True if the word was able to be made with the letter in
    the hand; False otherwise.
        
    word: string
    returns: Boolean (if the word was or was not made)
    """
    
    # create hand copy    
    self.updated = self.hand.copy()
    self.wordlen = 0
    
    # remove letters used in word
    for letter in self.updated:
        if letter in word:
            self.updated[letter] = self.updated.get(letter, 0) - word.count(letter)
            self.wordlen += word.count(letter)
        
    if self.wordlen == len(word):
        self.hand = self.updated
        return True
    else:
        return False
    
    