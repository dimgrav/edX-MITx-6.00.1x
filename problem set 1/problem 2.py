# -*- coding: utf-8 -*-
"""
Created on Sun Mar 12 12:58:18 2017

@author: Mitsakos
"""

counter = 0
s = 'azcbobobegghakl

for i in range(len(s)-2):
    if s[i] == "b" and s[i+1] == "o" and s[i+2] == "b":
        counter += 1

print ("Number of times bob occurs is: " + str(counter))