'''
Function to calculate the income probability

By Dr. Raymond Hoogendoorn
Copyright 2020
'''

def calculateIncomeProbability(df_incomedistribution, baseyear):
    year = str(baseyear)
    prob_distribution = df_incomedistribution[year]
    prob = list()
    for i in range(len(prob_distribution)):
        prob.append(prob_distribution.iloc[i] / sum(prob_distribution))
    return prob

