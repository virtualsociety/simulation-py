'''
Function to generate the life expectancy

By Dr. Raymond Hoogendoorn
Copyright 2021
'''

from numpy.random import choice

def generateLifeExpectancy(probability):
    elements = range(99)
    lifeexpectancy = choice(elements, p = probability)
    return lifeexpectancy
    
