# -*- coding: utf-8 -*-
"""
Created on Sun Mar 12 13:10:01 2017

@author: Mitsakos
"""

def dotProduct(listA, listB):
    '''
    listA: a list of numbers
    listB: a list of numbers of the same length as listA
    '''
    # Your code here
    total = 0 
    
    for n in range(len(listA)):
        total += listA[n]*listB[n]
    
    return total