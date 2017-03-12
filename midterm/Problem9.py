# -*- coding: utf-8 -*-
"""
Created on Sun Mar 12 13:10:01 2017

@author: Mitsakos
"""

def flatten(aList):
    ''' 
    aList: a list 
    Returns a copy of aList, which is a flattened version of aList 
    '''
    # base case for empty list
    if aList == []:
        return aList
    # recursive solution
    if isinstance(aList[0], list):
        return flatten(aList[0]) + flatten(aList[1:])
    
    return aList[:1] + flatten(aList[1:])