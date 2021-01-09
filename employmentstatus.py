# -*- coding: utf-8 -*-
"""
Created on Tue Dec  8 13:23:33 2020

@author: Raymo
"""

from numpy.random import choice

def generateEmploymentStatus(prob_dist, age):
    elements = ['Permanent contract', 'Flexible contract', 'Entrepreneur without personnel',
                'Entrepreneur with personel', 'Family business', 'Unknown', 'Unemployed']
    if age < 18:
        employmentstatus = 'Child'
    elif age > 67:
        employmentstatus = 'Retired'
    else:
        employmentstatus = choice(elements, p = prob_dist)
    return employmentstatus
    