'''
Function to calculate the genderprobability

By Dr. Raymond hoogendoorn
Copyright 2020
'''

def calculateGenderProbability(df_gender, baseyear):
    year = str(baseyear)
    genderprobability = list()
    genderprobability.append(df_gender[year].iloc[1])
    genderprobability.append(df_gender[year].iloc[2])
    genderprobability = genderprobability / sum(genderprobability)
    return genderprobability
    