# -*- coding: utf-8 -*-
"""
Created on Sun Mar 12 12:57:19 2017

@author: Mitsakos
"""

chars = 0
vowels = 0
cons = 0

s = 'azcbobobegghakl'

for i in s:
    chars += 1
    if i == "a":
        vowels += 1
    elif i == "i":
        vowels += 1
    elif i == "e":
        vowels += 1
    elif i == "o":
        vowels += 1
    elif i == "u":
        vowels += 1
    else:
        cons += 1

print ("Number of vowels: " + str(vowels))