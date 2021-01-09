'''
Function to generate the marriage age

By Dr. Raymond Hoogendoorn
Copyright 2020
'''

from numpy.random import choice
from random import randint

def generateMarriageAge(marriageageprobability, maritalstatus, marriageintention):
    elements = range(11)
    marriageageclass = choice(elements, p = marriageageprobability)
    if maritalstatus =='Single' and marriageintention == 'Yes':
        if marriageageclass == 0:
            marriageage = randint(0, 20)
        elif marriageageclass == 1:
            marriageage = randint(20, 25)
        elif marriageageclass == 2:
            marriageage = randint(25, 30)
        elif marriageageclass == 3:
            marriageage = randint(30, 35)
        elif marriageageclass == 4:
            marriageage = randint(35, 40)
        elif marriageageclass == 5:
            marriageage = randint(40, 45)
        elif marriageageclass == 6:
            marriageage = randint(45, 50)
        elif marriageageclass == 7:
            marriageage = randint(50, 55)
        elif marriageageclass == 8:
            marriageage = randint(55, 60)
        elif marriageageclass == 9:
            marriageage = randint(60, 65)
        elif marriageageclass == 10:
            marriageage = randint(65, 100)
    else:
        marriageage = None
    return marriageage

    
         
    
    