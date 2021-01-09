'''
Function to calculate the base population
size

By Dr. Raymond Hoogendoorn
Copyright 2020
'''

def calculateBasePopulationSize(df, baseyear, scalar):
    year = str(baseyear)
    populationsize = df[year].iloc[0]
    populationsize = populationsize / scalar
    populationsize = int(populationsize)
    return populationsize

    