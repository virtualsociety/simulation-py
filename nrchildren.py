'''
Function to generate the number of children

By Dr. Raymond Hoogendoorn
Copyright 2020
'''

from numpy.random import choice

def generateNrChildren(prob_distribution, maritalstatus, age, children):
    elements = [1, 2, 3]
    if maritalstatus == 'Married'  and age >= 18:
        nrchildren = choice(elements, p = prob_distribution)
    else:
        nrchildren = 0
    return nrchildren