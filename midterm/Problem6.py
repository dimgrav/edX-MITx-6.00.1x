# -*- coding: utf-8 -*-
"""
Created on Sun Mar 12 13:10:01 2017

@author: Mitsakos
"""

def deep_reverse(L):
    """ assumes L is a list of lists whose elements are ints
    Mutates L such that it reverses its elements and also 
    reverses the order of the int elements in every element of L. 
    It does not return anything.
    """
    # Your code here
   
    if len(L) == 1:
        for i in range(len(L)):
            L[i].reverse()
    else:
        for li in L:
            for i in li:
                li.reverse()
        L.reverse()
