'''
Function to calculate probability
of gender and determine gender
By Dr. Raymond Hoogendoor
Copyright 2020
'''
from numpy.random import choice

def generateGender(prob_distribution):
    elements = ['Male', 'Female']
    gender = choice(elements, p = prob_distribution)
    return gender
