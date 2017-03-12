# -*- coding: utf-8 -*-
"""
Created on Tue Feb 28 23:31:38 2017

@author: Mitsakos
"""
from ps6 import *

def decrypt_story():
    
    secret = get_story_string()
    cipher = CiphertextMessage(secret)
    
    return cipher.decrypt_message()