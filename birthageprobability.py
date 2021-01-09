'''
Function to calculate the birth age probability

By Dr. Raymond Hoogendoorn
Copyright 2020
'''

def calculateBirthAgeProbability(df_birthage, baseyear):
    year = str(baseyear)
    birthageprobability = list()
    df_temp = df_birthage[year]
    for i in range(len(df_temp)):
        birthageprobability.append((df_temp.iloc[i]) / sum(df_temp))
    return birthageprobability
