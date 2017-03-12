# -*- coding: utf-8 -*-
"""
Created on Sun Mar 12 13:10:01 2017

@author: Mitsakos
"""

def dict_interdiff(d1, d2):
    intersect = {}
    difference = {}
    for key in d1.keys():
        if key in d2.keys():
            intersect[key] = f(d1[key], d2[key])
        else:
            difference[key] = d1[key]
    for key in d2.keys():
        if key not in d1.keys():
            difference[key] = d2[key]
    return (intersect, difference)