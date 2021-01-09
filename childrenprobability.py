'''
Function to calculate the probability of having children

By Dr. Raymond Hoogendoorn
Copyright 2020
'''

def calculateChildrenProbability(df_withchildren, baseyear):
    year = str(baseyear)
    childrenprobability = list()
    childrenprobability.append(df_withchildren[year].iloc[1])
    childrenprobability.append(df_withchildren[year].iloc[2])
    childrenprobability = childrenprobability / sum(childrenprobability)
    return childrenprobability