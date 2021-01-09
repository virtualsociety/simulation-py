'''
Function to calculate the age probability

By Dr. Raymond Hoogendoorn
Copyright 2020
'''

def calculateAgeProbability(df_age, baseyear):
    year = str(baseyear)
    ageprobability = list()
    ageprobability.append(df_age[year].iloc[0])
    ageprobability.append(df_age[year].iloc[1])
    ageprobability.append(df_age[year].iloc[2])
    ageprobability.append(df_age[year].iloc[3])
    ageprobability.append(df_age[year].iloc[4])
    sum_age = sum(ageprobability)
    ageprobability = ageprobability / sum_age
    return ageprobability