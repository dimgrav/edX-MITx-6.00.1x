# -*- coding: utf-8 -*-
"""
Created on Thu Feb 23 18:33:38 2017

@author: Mitsakos
"""

def genPrimes():
    prime_list = []
    prime = 1
    
    while True:
        prime += 1
        for n in prime_list:
            if prime % n == 0:
                break
        else:
            prime_list.append(prime)
            next = prime
            yield next
        