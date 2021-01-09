'''
Function to generate marriage intention

By Dr. Raymond Hoogendoorn
Copyright 2020
'''

from numpy.random import choice

def generateMarriageIntention(marriageintentionprobability):
    elements = ['No', 'Yes']
    marriageintention = choice(elements, p = marriageintentionprobability)
    return marriageintention

