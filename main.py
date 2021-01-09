'''
Main script VS DES

By Dr. Raymond Hoogendoorn
Copyright 2020
'''

import pandas as pd
import simpy
import sys

from genderprobability import calculateGenderProbability
from ageprobability import calculateAgeProbability
from lifeexpectancyprobability import calculateLifeExpectancyProbability
from maritalstatusprobability import calculateMaritalStatusProbability
from marriagedurationprobability import calculateMarriageDurationProbability
from marriageintentionprobability import calculateMarriageIntentionProbability
from marriageageprobability import calculateMarriageAgeProbability
from employmentstatusprobability import calculateEmploymentStatusProbability
from incomeprobability import calculateIncomeProbability
from capitalprobability import calculateCapitalProbability
from childrenprobability import calculateChildrenProbability
from nrchildrenprobability import calculateNrChildrenProbability
from birthageprobability import calculateBirthAgeProbability

from gender import generateGender
from age import generateAge
from lifeexpectancy import generateLifeExpectancy
from maritalstatus import generateMaritalStatus
from marriageduration import generateMarriageDuration
from marriageintention import generateMarriageIntention
from marriageage import generateMarriageAge
from employmentstatus import generateEmploymentStatus
from income import generateIncome
from capital import generateCapital
from children import generateChildren 
from nrchildren import generateNrChildren
from birthage import generateBirthAge

from runtime import generateRuntime

#Create a function for citizens
def Citizen(env, name, year):
    genderprobability = calculateGenderProbability(df_gender, baseyear)
    gender = generateGender(genderprobability)
    ageprobability = calculateAgeProbability(df_age, baseyear)
    age = generateAge(ageprobability)
    lifeexpectancyprobability = calculateLifeExpectancyProbability(df_lifeexpectancy, baseyear, gender)
    lifeexpectancy = generateLifeExpectancy(lifeexpectancyprobability)
    maritalstatusprobability = calculateMaritalStatusProbability(df_maritalstatus, baseyear, age)
    maritalstatus = generateMaritalStatus(maritalstatusprobability)
    marriagedurationprobability = calculateMarriageDurationProbability(df_marriageduration, baseyear)
    marriageduration = generateMarriageDuration(marriagedurationprobability, maritalstatus)
    marriageintentionprobability = calculateMarriageIntentionProbability(df_marriage2, baseyear)
    marriageintention = generateMarriageIntention(marriageintentionprobability)
    marriageageprobability = calculateMarriageAgeProbability(df_marriage, baseyear, gender)
    marriageage = generateMarriageAge(marriageageprobability, maritalstatus, marriageintention)
    employmentstatusprobability = calculateEmploymentStatusProbability(df_employmentstatus, baseyear)
    employmentstatus = generateEmploymentStatus(employmentstatusprobability, age)
    incomeprobability = calculateIncomeProbability(df_income, baseyear)
    income = generateIncome(incomeprobability, age)
    capitalprobability = calculateCapitalProbability(df_capital, baseyear)
    capital = generateCapital(capitalprobability, age)
    childrenprobability = calculateChildrenProbability(df_withchildren, baseyear)
    children = generateChildren(childrenprobability)
    nrchildrenprobability = calculateNrChildrenProbability(df_nrchildren, baseyear)
    nrchildren = generateNrChildren(nrchildrenprobability, maritalstatus, age, children)
    birthageprobability = calculateBirthAgeProbability(df_birthage, baseyear)
    birthage = generateBirthAge(birthageprobability, gender, age, nrchildren, maritalstatus)
    
    #Append to lists
    citizen_event_list.append("Life event: Created")
    citizen_ID_list.append(name)
    citizen_timestamp_list.append(env.now)
    citizen_gender_list.append(gender)
    citizen_age_list.append(age)
    citizen_lifeexpectancy_list.append(lifeexpectancy)
    citizen_maritalstatus_list.append(maritalstatus)
    citizen_marriageduration_list.append(marriageduration)
    citizen_marriageintention_list.append(marriageintention)
    citizen_marriageage_list.append(marriageage)
    citizen_employmentstatus_list.append(employmentstatus)
    citizen_income_list.append(income)
    citizen_capital_list.append(capital)
    citizen_children_list.append(children)
    citizen_nrchildren_list.append(nrchildren)
    citizen_birthage_list.append(birthage)
    
    while True:
        #Adulthood
        if age < 18:
            delta_adulthood = (18- age) * 365
            yield env.timeout(delta_adulthood)
            age = 18
            employmentstatus = generateEmploymentStatus(employmentstatusprobability, age)
            marriageintention = generateMarriageIntention(marriageintentionprobability)
            marriageage = generateMarriageAge(marriageageprobability, maritalstatus, marriageintention)
            income = income = generateIncome(incomeprobability, age)
            capital = generateCapital(capitalprobability, age)
            citizen_event_list.append("Life event: Adulthood")
            citizen_ID_list.append(name)
            citizen_timestamp_list.append(env.now)
            citizen_gender_list.append(gender)
            citizen_age_list.append(age)
            citizen_lifeexpectancy_list.append(lifeexpectancy)
            citizen_maritalstatus_list.append(maritalstatus)
            citizen_marriageduration_list.append(marriageduration)
            citizen_marriageintention_list.append(marriageintention)
            citizen_marriageage_list.append(marriageage)
            citizen_employmentstatus_list.append(employmentstatus)
            citizen_income_list.append(income)
            citizen_capital_list.append(capital)
            citizen_children_list.append(children)
            citizen_nrchildren_list.append(nrchildren)
            citizen_birthage_list.append(birthage)
        
        #Married
        if marriageintention == 'Yes' and not (marriageage is None):
            if marriageage > age:
                delta_marriage = (marriageage - age) * 365
                yield env.timeout(delta_marriage)
                age = marriageage
                maritalstatus = 'Married'
                citizen_event_list.append("Life event: Married")
                citizen_ID_list.append(name)
                citizen_timestamp_list.append(env.now)
                citizen_gender_list.append(gender)
                citizen_age_list.append(age)
                citizen_lifeexpectancy_list.append(lifeexpectancy)
                citizen_maritalstatus_list.append(maritalstatus)
                citizen_marriageduration_list.append(marriageduration)
                citizen_marriageintention_list.append(marriageintention)
                citizen_marriageage_list.append(marriageage)
                citizen_employmentstatus_list.append(employmentstatus)
                citizen_income_list.append(income)
                citizen_capital_list.append(capital)
                citizen_children_list.append(children)
                citizen_nrchildren_list.append(nrchildren)
                citizen_birthage_list.append(birthage)
        
        #Divorced
        if maritalstatus == 'Married':
            delta_divorce = (env.now + (marriageduration * 365))
            yield env.timeout(delta_divorce)
            age += int(env.now / 365)
            maritalstatus = 'Divorced'
            citizen_event_list.append("Life event: Divorced")
            citizen_ID_list.append(name)
            citizen_timestamp_list.append(env.now)
            citizen_gender_list.append(gender)
            citizen_age_list.append(age)
            citizen_lifeexpectancy_list.append(lifeexpectancy)
            citizen_maritalstatus_list.append(maritalstatus)
            citizen_marriageduration_list.append(marriageduration)
            citizen_marriageintention_list.append(marriageintention)
            citizen_marriageage_list.append(marriageage)
            citizen_employmentstatus_list.append(employmentstatus)
            citizen_income_list.append(income)
            citizen_capital_list.append(capital)
            citizen_children_list.append(children)
            citizen_nrchildren_list.append(nrchildren)
            citizen_birthage_list.append(birthage)
        
        #Deceased
        if lifeexpectancy > age:
            delta_deceased = (lifeexpectancy - age) * 365
            yield env.timeout(delta_deceased)
            age = lifeexpectancy + 1
            citizen_event_list.append("Life event: Deceased")
            citizen_ID_list.append(name)
            citizen_timestamp_list.append(env.now)
            citizen_gender_list.append(gender)
            citizen_age_list.append(age)
            citizen_lifeexpectancy_list.append(lifeexpectancy)
            citizen_maritalstatus_list.append(maritalstatus)
            citizen_marriageduration_list.append(marriageduration)
            citizen_marriageintention_list.append(marriageintention)
            citizen_marriageage_list.append(marriageage)
            citizen_employmentstatus_list.append(employmentstatus)
            citizen_income_list.append(income)
            citizen_capital_list.append(capital)
            citizen_children_list.append(children)
            citizen_nrchildren_list.append(nrchildren)
            citizen_birthage_list.append(birthage)
            
            
        yield env.timeout(180)
            
        
# Read input files
df_gender = pd.read_csv('./Input/Bevolking__kerncijfers_07122020_100024.csv', delimiter = ';')
df_age = pd.read_csv('./Input/Bevolking__kerncijfers_07122020_112736.csv', delimiter = ';')
df_lifeexpectancy = pd.read_csv('./Input/Levensverwachting__geslacht__leeftijd__per_jaar_en_periode_van_vijf_jaren__06012021_105805.csv', delimiter = ';')
df_maritalstatus = pd.read_csv('./Input/Bevolking__geslacht__leeftijd_en_burgerlijke_staat__1_januari_08122020_110015.csv', delimiter = ';')
df_marriageduration = pd.read_csv('./Input/Bestaande_huwelijken_en_partnerschappen__relatieduur__1_januari_08122020_121148.csv', delimiter = ';')
df_employmentstatus = pd.read_csv('./Input/Arbeidsdeelname__kerncijfers__08122020_130106.csv', delimiter = ';')
df_income = pd.read_csv('./Input/Inkomen_van_personen__inkomensklassen__persoonskenmerken_09122020_094158.csv', delimiter = ';')
df_marriage = pd.read_csv('./Input/Huwen_en_huwelijksontbinding__geslacht__leeftijd__31_december___regio_11122020_100116.csv', delimiter = ';')
df_marriage2 = pd.read_csv('./Input/Bevolking__geslacht__leeftijd_en_burgerlijke_staat__1_januari_11122020_105220.csv', delimiter = ';')
df_withchildren =  pd.read_csv('./Input/Particuliere_huishoudens_naar_samenstelling_en_grootte__1_januari_14122020_114929.csv', delimiter = ';')
df_nrchildren = pd.read_csv('./Input/Huishoudens__kindertal__leeftijdsklasse_kind__regio__1_januari_14122020_114332.csv', delimiter = ';')
df_birthage =  pd.read_csv('./Input/Levend_geboren_kinderen__migratieachtergrond_moeder_en_leeftijd_moeder_14122020_112329.csv', delimiter = ';')
df_capital = pd.read_csv('./Input/vermogensklassen.csv', delimiter = ';')

#Create empty lists for data collection
citizen_event_list = []
citizen_ID_list = []
citizen_timestamp_list = []
citizen_gender_list = []
citizen_age_list = []
citizen_lifeexpectancy_list = []
citizen_maritalstatus_list = []
citizen_marriageduration_list = []
citizen_marriageintention_list = []
citizen_marriageage_list = []
citizen_employmentstatus_list = []
citizen_income_list = []
citizen_capital_list = []
citizen_children_list = []
citizen_nrchildren_list = []
citizen_birthage_list = []

#Initialize main variables
start_date = '2011-01-01' #Set the start date of the simulation
end_date = '2011-12-31' #Set the end data of the simulation
baseyear = int(start_date[:4])
runtime =generateRuntime(start_date, end_date)

# Run Simulation
populationsize = 1000
env = simpy.Environment()
for i in range(populationsize):
    env.process(Citizen(env, i, baseyear))
    b = ("Creating citizens: " + str(i))
    sys.stdout.write('\r'+b)
print("")
print("Running simulation")
env.run(until=runtime)  

#Construct and save the dataframe
df_data = pd.DataFrame(
    {'Life event': citizen_event_list,
     'ID': citizen_ID_list,
     'Timestamp': citizen_timestamp_list,
     'Gender': citizen_gender_list,
     'Age': citizen_age_list,
     'Life expectancy': citizen_lifeexpectancy_list,
     'Marital status': citizen_maritalstatus_list,
     'Marriage duration': citizen_marriageduration_list,
     'Marriage intention': citizen_marriageintention_list,
     'Marriage age:': citizen_marriageage_list,
     'Employment status': citizen_employmentstatus_list,
     'Income': citizen_income_list,
     'Capital': citizen_capital_list,
     'Children': citizen_children_list,
     'Nr children': citizen_nrchildren_list,
     'Birth age': citizen_birthage_list
    })

df_data = df_data.sort_values(['ID', 'Timestamp'])

df_data.to_csv('simulatedpopulation.csv') 