'''
Function to determine the age

By Dr. Raymond Hoogendoorn
Copyright 2020
'''

from numpy.random import choice
from random import randint


def generateAge(ageprobability):
    elements = [0, 1, 2, 3, 4]
    age_class = choice(elements, p = ageprobability)
    min_age = [0, 20, 40, 65, 80]
    max_age = [20, 40, 65, 80, 105]
    age = randint(min_age[age_class], max_age[age_class])
    return age
    