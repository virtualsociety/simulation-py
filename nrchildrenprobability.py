'''
Function to calculate the number of children probability

By Dr. Raymond Hoogendoorn
Copyright 2020
'''

def calculateNrChildrenProbability(df_nrchildren, baseyear):
    year = str(baseyear)
    nrchildrenprobability = list()
    nrchildrenprobability.append(df_nrchildren[year].iloc[0])
    nrchildrenprobability.append(df_nrchildren[year].iloc[1])
    nrchildrenprobability.append(df_nrchildren[year].iloc[2])
    nrchildrenprobability = nrchildrenprobability / sum(nrchildrenprobability)
    return nrchildrenprobability