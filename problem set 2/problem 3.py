# -*- coding: utf-8 -*-
"""
Created on Sun Mar 12 13:00:35 2017

@author: Mitsakos
"""
#initial credit parameters
b0 = balance
air = annualInterestRate
mRate = air/12.0
fixed = b0/12.0
fixed_lower = b0/12.0
fixed_upper = (b0*(1 + air)**12)/12.0
unpaidb = balance


#fixed payment calculations
while True:
    
    #balance at the start of a new month
    for i in range(12):
        unpaidb = balance - fixed
        balance = unpaidb + mRate*unpaidb

    #check to see if balance is paid after 12 months
    #if not, reset balance and use bisection to find fixed
    if abs(balance) < 0.1:
        print("Lowest Payment: ", round(fixed, 2))
        break
    else:
        #for balance < 0, fixed is higher than required
        if balance < 0:
            fixed_upper = fixed
        #for balance > 0, fixed is lower than required    
        elif balance > 0:
            fixed_lower = fixed
        
        #new fixed computation and balance reset here
        fixed = (fixed_lower + fixed_upper)/2
        balance = b0