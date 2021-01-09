'''
Function to calculate the capital probability

By Dr. Raymond Hoogendoorn
Copyright 2020
'''

def calculateCapitalProbability(df_capital, baseyear):
    year = str(baseyear)
    prob_distribution = df_capital[year]
    prob = list()
    for i in range(len(prob_distribution)):
        prob.append(prob_distribution.iloc[i] / sum(prob_distribution))
    return prob