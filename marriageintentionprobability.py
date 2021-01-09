'''
Function to calculate the probability of getting married

By Dr. Raymond Hoogendoorn
Copyright 2020
'''


def calculateMarriageIntentionProbability(df_marriage2, baseyear):
    year = int(baseyear)
    df_current = df_marriage2[df_marriage2['Perioden'] == year]
    marriageintentionprob = list()
    for i in range(len(df_current)):
        marriageintentionprob.append((df_current['Totaal leeftijd'].iloc[i]) / sum(df_current['Totaal leeftijd']))
    return marriageintentionprob
    
    