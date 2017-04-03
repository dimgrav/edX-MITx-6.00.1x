# -*- coding: utf-8 -*-
"""
Created on Sat Mar 11 00:42:36 2017

@author: Mitsakos
"""

def general_poly(L):
    """ L, a list of numbers (n0, n1, n2, ... nk)
    Returns a function, which when applied to a value x, returns the value 
    n0 * x^k + n1 * x^(k-1) + ... nk * x^0 """
    
    def applied_for(x):
        nums = []
    
        for i in range(len(L), 0, -1):
            print(str(L[len(L) - i])+"*10^"+str(i - 1)) # optional print
            nums.append(L[len(L) - i]*(x**(i - 1)))
    
        return sum(nums)
    return applied_for
