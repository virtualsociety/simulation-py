'''
Function to calculate the life expectancy

By Dr. Raymond Hoogendoorn
Copyright 2021
'''

def calculateLifeExpectancyProbability(df_lifeexpectancy, year, gender):

    df = df_lifeexpectancy.loc[df_lifeexpectancy['Jaar'] == year]
    if gender == 'Male':
        df = df['Levende mannen']
    else:
        df = df['Levende vrouwen']
    df = 1 / df
    probability = df / sum(df)
    return probability