# -*- coding: utf-8 -*-
"""
Created on Sun Mar 12 13:00:35 2017

@author: Mitsakos
"""
#initial credit parameters
b0 = balance
air = annualInterestRate
mRate = air/12
fixed = 0
unpaidb = balance

#fixed payment calculations
while True:
    
    #balance at the start of a new month
    for i in range(12):
        unpaidb = balance - fixed
        balance = unpaidb + mRate*unpaidb
    
    #check to see if balance is paid after 12 months
    #if not, reset balance and increase step by 10
    if balance <= 0:
        print("Lowest Payment: ", round(fixed, 2))
        break
    else:
        fixed += 10
        balance = b0