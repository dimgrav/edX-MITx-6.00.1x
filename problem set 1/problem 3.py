# -*- coding: utf-8 -*-
"""
Created on Sun Mar 12 12:59:48 2017

@author: Mitsakos
"""

string = ""
count = 0
maxcount = 0
maxstring = ""
s = 'azcbobobegghakl'

for i in range(len(s)):
    if i == 0:
        string += s[i]
        count += 1
    elif s[i] >= s[i - 1]:
        string += s[i]
        count += 1
    elif s[i] < s[i - 1]:
        if count > maxcount:
            maxcount = count
            maxstring = string
        count = 0
        count = 1
        string = ""
        string += s[i]
    if i == len(s) - 1:
        if count > 1:
            if count > maxcount:
                maxcount = count
                maxstring = string
                
print("Longest substring in alphabetical order is: " + maxstring)