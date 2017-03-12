# -*- coding: utf-8 -*-
"""
Created on Mon Feb  6 17:35:40 2017

@author: mitsakos
"""
aDict = {'u': [10, 15, 5, 2, 6], 'B': [15]}

total = 0
biggest = len(aDict['B'])
biggest_key = 'B'

for key in aDict:
    if len(aDict[key]) > biggest:
        biggest = len(aDict[key])
        biggest_key = str(key)
    for value in aDict[key]:
        total += 1

print (total)
print (biggest_key)
