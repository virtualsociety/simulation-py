'''
Function to generate the marital status

By Dr. Raymond Hoogendoorn
Copyright 2020
'''

from numpy.random import choice

def generateMaritalStatus(prob_distribution):
    elements = ['Single', 'Married', 'Widowed', 'Divorced']
    maritalstatus = choice(elements, p = prob_distribution)
    return maritalstatus