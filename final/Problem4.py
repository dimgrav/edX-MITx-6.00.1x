# -*- coding: utf-8 -*-
"""
Created on Fri Mar 10 18:44:22 2017

@author: Mitsakos
"""

def longest_run(L):
    """
    Assumes L is a list of integers containing at least 2 elements.
    Finds the longest run of numbers in L, where the longest run can
    either be monotonically increasing or monotonically decreasing. 
    In case of a tie for the longest run, choose the longest run 
    that occurs first.
    Does not modify the list.
    Returns the sum of the longest run. 
    """
    
    decr = 0
    incr = 0
    longest = 0
    end_i = 0

    for i in range(len(L) - 1):
        # check if decreasing
        if L[i] <= L[i + 1]:
            decr += 1
            if decr > longest:
                longest = decr
                end_i = i + 1
        else:
            decr = 0
        
        # check if increasing
        if L[i] >= L[i + 1]:
            incr += 1            
            if incr > longest:
                longest = incr
                end_i = i + 1
        else:
            incr = 0
        
    start_i = end_i - longest
    longest_sum = sum(L[start_i:end_i + 1])
    
    return longest_sum
    