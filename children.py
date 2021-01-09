'''
Function to calculate probability
of gender and determine gender

By Dr. Raymond Hoogendoor
Copyright 2020
'''
from numpy.random import choice

def generateChildren(prob_distribution):
    elements = ['No', 'Yes']
    children = choice(elements, p = prob_distribution)
    return children
