# -*- coding: utf-8 -*-
"""
Created on Wed Aug 29 05:21:12 2018

@author: Jonathan
"""

#retrieving input values
annual_salary = int(input("What's your annual salary?"))
portion_saved= float(input("Enter the percent of your salary to save, as a decimal:"))
total_cost = int(input("Enter the cost of your dream home:"))

#Initializing variables
portion_down_payment = 0.25
current_savings = 0
r = 0.04
months_needed = 0

#while current savings is smaller than cost to pay, keep saving 
while current_savings<portion_down_payment*total_cost:
    current_savings+= portion_saved*annual_salary/12+current_savings*r/12
    months_needed +=1
    
print(months_needed)