'''
Function to generate income

By Dr. Raymond Hoogendoorn
Copyright 2020
'''

from numpy.random import choice
from random import randint
    
def generateIncome(prob_distribution, age):
    elements = range(0,8)
    min_range = [0, 10000, 20000, 30000, 40000, 50000, 100000, 200000]
    max_range = [10000, 20000, 30000, 40000, 50000, 100000, 200000, 500000]
    if age >= 18:
        incomeclass = choice(elements, p = prob_distribution)
        min_income = min_range[incomeclass]
        max_income = max_range[incomeclass]
        income = randint(min_income, max_income)
        return income
    else:
        return 0
        
        
    
        
        