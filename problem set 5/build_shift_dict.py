# -*- coding: utf-8 -*-
"""
Created on Fri Feb 24 21:21:20 2017

@author: Mitsakos
"""

def build_shift_dict(self, shift):
    '''
    Creates a dictionary that can be used to apply a cipher to a letter.
    The dictionary maps every uppercase and lowercase letter to a
    character shifted down the alphabet by the input shift. The dictionary
    should have 52 keys of all the uppercase letters and all the lowercase
    letters only.        
        
    shift (integer): the amount by which to shift every letter of the 
    alphabet. 0 <= shift < 26

    Returns: a dictionary mapping a letter (string) to 
    another letter (string). 
    '''
    assert shift >= 0 and shift < 26, "Invalid shift value"

    az = "abcdefghijklmnopqrstuvwxyz"
    AZ = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
#    shift = 3

    keys = []
    vals_az = []
    vals_AZ = []
    
    for i in range(26):
        keys.append(i)
        vals_az.append(az[i])
        vals_AZ.append(AZ[i])

    shift_keys = list(az) + list(AZ)
    shift_vals = vals_az[shift:] + vals_az[:shift] + vals_AZ[shift:] + vals_AZ[:shift]

    self.shift_aZ = dict(zip(shift_keys, shift_vals))
    
    return self.shift_aZ