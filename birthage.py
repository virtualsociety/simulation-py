'''
Function to generate the birthing age

By Dr. Raymond Hoogendoorn
Copyright 2020
'''

from numpy.random import choice
    
def generateBirthAge(prob_distribution, gender, age, nrchildren, maritalstatus):
    elements = range(15, 50)
    if gender == 'Female':
        birthage = choice(elements, p = prob_distribution)
        if birthage >= age:
            return birthage
        else:
            return None
    else:
        return None

        