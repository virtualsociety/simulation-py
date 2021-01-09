'''
Function to generate the marriage duration

By Dr. Raymond Hoogendoorn
Copyright 2020
'''

from numpy.random import choice

def generateMarriageDuration(prob_distribution, maritalstatus):
    elements = range(0, 71)
    if maritalstatus == 'Married':
        marriageduration = choice(elements, p = prob_distribution)
    else:
        marriageduration = 0
    return marriageduration
