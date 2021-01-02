# -*- coding: utf-8 -*-
"""
Created on Thu Aug 30 22:49:52 2018

@author: Jonathan
"""
#Ask input
annual_salary = int(input("What's your starting salary?"))
original_as=annual_salary
#initialization for a 1M house
total_cost=1000000
portion_down_payment=0.25 
current_savings = 0
r = 0.04
semi_annual_raise = 0.07
savings_necessary = total_cost*portion_down_payment

#function to calculate expected savings (after 36 months in this case)
#given the annual_salary and savings rate
def exp_savings(annual_salary,save_rate,current_savings=0,months=36):
    for i in range(months):
        current_savings += save_rate*annual_salary/12+current_savings*r/12
        if i%6==0:
             annual_salary *= (1+semi_annual_raise)   
    return current_savings

#bisection search
#initalizing factors
low=0
high=10000
guess=(high+low)/2
    
#search
num_of_steps = 0
while abs(exp_savings(annual_salary,guess/10000)-savings_necessary)>=100:
    
    if exp_savings(annual_salary,1)<savings_necessary:
        print("It is not possible to pay the payment in three years.")
        break
    if exp_savings(annual_salary,guess/10000)<savings_necessary :
        low=guess
    elif exp_savings(annual_salary,guess/10000)>savings_necessary :
        high=guess
    annual_salary=original_as
    guess=(high+low)/2
    num_of_steps+=1

#print output
print("Best savings rate:"+str(guess/10000))
print("Steps on bisection search:"+str(num_of_steps)) 