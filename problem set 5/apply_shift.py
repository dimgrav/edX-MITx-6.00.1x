# -*- coding: utf-8 -*-
"""
Created on Sat Feb 25 20:35:16 2017

@author: Mitsakos
"""
import string
from ps6 import *

def apply_shift(self, shift):
    '''
    Applies the Caesar Cipher to self.message_text with the input shift.
    Creates a new string that is self.message_text shifted down the
    alphabet by some number of characters determined by the input shift        
        
    shift (integer): the shift with which to encrypt the message.
    0 <= shift < 26

    Returns: the message text (string) in which every character is shifted
    down the alphabet by the input shift
    '''
    assert shift >= 0 and shift < 26, "Invalid shift value"

    message_text = self.message_text

    univ_lst = list(string.digits) + list(string.punctuation) + list(" ")
    shifted_dict = self.build_shift_dict(shift)
    message_lst = list(message_text)
    
    cipher_lst = [shifted_dict[char] if char not in univ_lst else char for char in message_lst]
    self.cipher_text = "".join(cipher_lst)
    
    return self.cipher_text