# -*- coding: utf-8 -*-
"""
Created on Tue Feb 14 18:24:36 2017

@author: Mitsakos
"""

def closest_power(base, num):
    '''
    base: base of the exponential, integer > 1
    num: number you want to be closest to, integer > 0
    Find the integer exponent such that base**exponent is closest to num.
    Note that the base**exponent may be either greater or smaller than num.
    In case of a tie, return the smaller value.
    Returns the exponent.
    '''
    assert base > 1, "wrong base input"
    assert num > 0, "wrong num input"
    
    exponent = 0
    
    while True:
        if base**exponent > num:
            if abs(num - base**(exponent - 1)) == abs(base**exponent - num):
                return exponent - 1 
                break
            else:
                return exponent
                break
        elif base**exponent == num:
            return exponent
            break            
        else:
            exponent += 1
    
    return exponent
