# -*- coding: utf-8 -*-
"""
Created on Tue Jan 31 22:47:23 2017

@author: Mitsakos
"""

"""
def creditCard(b,r):
    """
#Calculates credit card balance payments.
#b: balance
#r: monthly payment rate
#ar: annual interest rate
#ub: unpaid balaance at the start of each month
#Returns remaining balance each month
"""
#initial credit card parameters
b = 42
r = 0.04
ar = 0.2

#monthly calculations     
while b != 0:
    
p = b*r
ub = b - p
b = ub + ub*(ar/12)
    
return round(b, 2)
"""

#initial credit parameters
b0 = 4773
balance = 4773
annualInterestRate = 0.2
mRate = annualInterestRate/12
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
        
