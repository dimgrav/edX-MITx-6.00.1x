# -*- coding: utf-8 -*-
"""
Created on Sun Mar 12 13:00:35 2017

@author: Mitsakos
"""
# calculate the credit card balance after one year
# if a person only pays the minimum monthly payment
# required by the credit card company each month.

# monthly calculations     
for i in range(12):
    
    pay = balance*monthlyPaymentRate
    unpaidb = balance - pay
    balance = unpaidb + unpaidb*(annualInterestRate/12)
    
print(round(balance, 2))