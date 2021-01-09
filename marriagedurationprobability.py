'''
Function to calculate the marriageduration probability

By Dr. Raymond Hoogendoorn
Copyright 2020
'''

def calculateMarriageDurationProbability(df_marriageduration, baseyear):
    rowyears = int(baseyear)
    df_year = df_marriageduration[df_marriageduration['Perioden'] == rowyears]
    prob = df_year['Aantal']
    prob_list = list()
    for i in range(len(prob)):
        prob_list.append(prob.iloc[i])
    prob_list = prob_list / sum(prob_list)
    return prob_list
        