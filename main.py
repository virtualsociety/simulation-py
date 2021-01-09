'''
Main script for VS DES

By Dr. Raymond Hoogendoorn
Copyright 2021
'''

import pandas as pd
import simpy
import sys
import random

from basepopulationsize import calculateBasePopulationSize
from simulatedpopulationsize import calculateSimulatedPopulationSize
from runtime import generateRuntime

from readinputfiles import readInputFiles
from emptylists import createEmptyLists

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
    lifeevent = 'Life event: Created'
    
    #Append to lists                                                                                                                                                                                                                                                                                                                                                                                                                              citizen_children_list, citizen_nrchildren_list, citizen_birthage_list)
    citizen_event_list.append(lifeevent)
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
            income = generateIncome(incomeprobability, age)
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
        
        #Births
        if children == 'Yes' and not (birthage is None):
            if birthage > age:
                delta_birth = (birthage - age) * 365
                yield env.timeout(delta_birth)
                age = birthage
                nrchildren += 1
                citizen_event_list.append("Life event: Birth")
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
        
def Newborn(env, name, year, runtime):
    genderprobability = calculateGenderProbability(df_gender, baseyear)
    gender = generateGender(genderprobability)
    age = 0
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
    lifeevent = 'Life event: Created'
    
    #Time until birth
    time_until_birth = random.randint(0, runtime)
    yield env.timeout(time_until_birth)
    
    #Append to lists                                                                                                                                                                                                                                                                                                                                                                                                                              citizen_children_list, citizen_nrchildren_list, citizen_birthage_list)
    citizen_event_list.append(lifeevent)
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
                
        #Births
        if children == 'Yes' and not (birthage is None):
            if birthage > age:
                delta_birth = (birthage - age) * 365
                yield env.timeout(delta_birth)
                age = birthage
                nrchildren += 1
                citizen_event_list.append("Life event: Birth")
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

#Initialize main variables
scalar = 1000
start_date = '2011-01-01' #Set the start date of the simulation (minumum 2011)
end_date = '2012-12-31' #Set the end data of the simulation (maximum 2019)
baseyear = int(start_date[:4])
runtime =generateRuntime(start_date, end_date)

#Read the inputfiles
df_gender, df_age, df_lifeexpectancy, df_maritalstatus, df_marriageduration, df_employmentstatus, df_income, df_marriage, df_marriage2, df_withchildren, df_nrchildren, df_birthage, df_capital = readInputFiles()

#Create empty lists
citizen_event_list, citizen_ID_list, citizen_timestamp_list, citizen_gender_list, citizen_age_list, citizen_lifeexpectancy_list, citizen_maritalstatus_list, citizen_marriageduration_list, citizen_marriageintention_list, citizen_marriageage_list, citizen_employmentstatus_list, citizen_income_list, citizen_capital_list, citizen_children_list, citizen_nrchildren_list, citizen_birthage_list = createEmptyLists()

#Determine the size of the base population
populationsize_base = int(calculateBasePopulationSize(df_gender, baseyear, scalar))
populationsize_simulated = int(calculateSimulatedPopulationSize(df_birthage, start_date, end_date, scalar))
populationsize_total = populationsize_base + populationsize_simulated

#Run simulation
env = simpy.Environment()
for i in range(populationsize_base):
    env.process(Citizen(env, i, baseyear))
    b = ("Creating citizens: " + str(i))
    sys.stdout.write('\r'+b)

print("")

for j in range(populationsize_simulated):
    env.process(Newborn(env, (j + populationsize_base), baseyear, runtime))
    b = ("Creating newborns: " + str(j))
    sys.stdout.write('\r'+b)

print("")
print("Running simulation with runtime {} days".format(runtime))
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
        
    
    