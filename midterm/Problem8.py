# -*- coding: utf-8 -*-
"""
Created on Sun Mar 12 13:10:01 2017

@author: Mitsakos
"""

def applyF_filterG(L, f, g):
    """
    Assumes L is a list of integers
    Assume functions f and g are defined for you. 
    f takes in an integer, applies a function, returns another integer 
    g takes in an integer, applies a Boolean function, 
        returns either True or False
    Mutates L such that, for each element i originally in L, L contains  
        i if g(f(i)) returns True, and no other elements
    Returns the largest element in the mutated L or -1 if the list is empty
    """
    
    newL = []
    for i in L:
        if g(f(i)) == True:
            newL.append(i)
    L[:] = newL
    if len(L) == 0:
        return -1
    else:
        return max(L)