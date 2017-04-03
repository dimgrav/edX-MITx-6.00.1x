# -*- coding: utf-8 -*-
"""
Created on Mon Feb 27 14:50:14 2017

@author: Mitsakos
"""
from ps6 import *

class PlaintextMessage(Message):
    def __init__(self, text, shift):
        '''
        Initializes a PlaintextMessage object        
        
        text (string): the message's text
        shift (integer): the shift associated with this message

        A PlaintextMessage object inherits from Message and has five attributes:
            self.message_text (string, determined by input text)
            self.valid_words (list, determined using helper function load_words)
            self.shift (integer, determined by input shift)
            self.encrypting_dict (dictionary, built using shift)
            self.message_text_encrypted (string, created using shift)
        '''
        Message.__init__(self, text)
        self.shift = shift
        self.encrypting_dict = Message.build_shift_dict(self, self.shift)
        self.message_text_encrypted = Message.apply_shift(self, self.shift)

    def get_shift(self):
        '''
        Returns: self.shift
        '''
        
        return self.shift

    
    def get_encrypting_dict(self):
        '''
        Returns: a COPY of self.encrypting_dict
        '''
         
        return self.encrypting_dict.copy()

    
    def get_message_text_encrypted(self):
        '''
        Returns: self.message_text_encrypted
        '''
        self.message_text_encrypted = Message.apply_shift(self, self.shift)
        return self.message_text_encrypted

    
    def change_shift(self, shift):
        '''
        Changes self.shift of the PlaintextMessage and updates other 
        attributes determined by shift (ie. self.encrypting_dict and 
        message_text_encrypted).
        
        shift (integer): the new shift that should be associated with this message.
        0 <= shift < 26

        Returns: nothing
        '''
        assert shift >= 0 and shift < 26, "Invalid shift value"
        
        self.shift = shift
        self.encrypting_dict = (Message.build_shift_dict(self, self.shift)).copy()
        self.message_text_encrypted = Message.apply_shift(self, self.shift)
        
        
        
        
        
        
