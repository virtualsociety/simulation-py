'''
Function to generate capital

By Dr. Raymond Hoogendoorn
Copyright 2020
'''

from numpy.random import choice
from random import randint
    
def generateCapital(prob_distribution, age):
    elements = range(0,12)
    min_range = [-50000, -5000, 0, 1000, 5000, 10000, 20000, 50000, 100000, 200000, 500000, 1000000]
    max_range = [-5000, 0, 1000, 5000, 10000, 20000, 50000, 100000, 200000, 500000, 1000000, 5000000]
    if age >= 18:
        capitalclass = choice(elements, p = prob_distribution)
        min_capital = min_range[capitalclass]
        max_capital = max_range[capitalclass]
        capital = randint(min_capital, max_capital)
        return capital
    else:
        return 0
        
        