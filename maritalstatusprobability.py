'''
Function to calculate the maritalstatus probability

By Dr. Raymond Hoogendoorn
Copyright 2020
'''

def calculateMaritalStatusProbability(df_maritalstatus, baseyear, age):
    df_year = df_maritalstatus[df_maritalstatus['Perioden'] == baseyear]
    if age >= 0 and age < 5:
        prob = df_year['0 tot 5 jaar']
    elif age >= 5 and age < 10:
        prob = df_year['5 tot 10 jaar']
    elif age >=10 and age < 15:
        prob = df_year['10 tot 15 jaar']
    elif age >= 15 and age < 20:
        prob = df_year['15 tot 20 jaar']
    elif age >= 20 and age < 25:
        prob = df_year['20 tot 25 jaar']
    elif age >= 25 and age < 30:
        prob = df_year['25 tot 30 jaar']
    elif age >= 30 and age < 35:
        prob = df_year['30 tot 35 jaar']
    elif age >= 35 and age < 40:
        prob = df_year['35 tot 40 jaar']
    elif age >= 40 and age < 45:
        prob = df_year['40 tot 45 jaar']
    elif age >= 45 and age < 50:
        prob = df_year['45 tot 50 jaar']
    elif age >= 50 and age < 55:
        prob = df_year['50 tot 55 jaar']
    elif age >= 55 and age < 60:
        prob = df_year['55 tot 60 jaar']
    elif age >= 60 and age < 65:
        prob = df_year['60 tot 65 jaar']
    elif age >= 65 and age < 70:
        prob = df_year['65 tot 70 jaar']
    elif age >= 70 and age < 75:
        prob = df_year['70 tot 75 jaar']
    elif age >= 75 and age < 80:
        prob = df_year['75 tot 80 jaar']
    elif age >= 80 and age < 85:
        prob = df_year['80 tot 85 jaar']
    elif age >= 85 and age < 90:
        prob = df_year['85 tot 90 jaar']
    elif age >= 90 and age < 95:
        prob = df_year['90 tot 95 jaar']
    elif age >= 95 and age < 100:
        prob = df_year['95 tot 100 jaar']
    elif age >= 100:
        prob = df_year['100 jaar of ouder']
    probabilitydist = list()
    for i in range(len(prob)):
        probabilitydist.append(prob[i] / sum(prob))
    return probabilitydist