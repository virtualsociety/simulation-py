'''
Function to calculate the employment status probability

By Dr. Raymond Hoogendoorn
Copyright 2020
'''

def calculateEmploymentStatusProbability(df_employment, baseyear):
    year = str(baseyear)
    prob_dist = df_employment[year]
    prob_dist = prob_dist / sum(prob_dist)
    return prob_dist
    