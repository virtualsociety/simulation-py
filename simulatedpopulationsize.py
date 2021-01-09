'''
Function to determine the simulated populationsize

By Dr. Raymond Hoogendoorn
Copyright 2021
'''

from datetime import date

def calculateSimulatedPopulationSize(df, start_date, end_date, scalar):
    start_date_temp = str(start_date)
    end_date_temp = str(end_date)
    year_start = int(start_date_temp[:4])
    year_end = int(end_date_temp[:4])
    month_start = int(start_date_temp[5:7])
    month_end = int(end_date_temp[5:7])
    day_start = int(start_date_temp[8:10])
    day_end = int(end_date_temp[8:10])
    
    d0 = date(year_start, month_start, day_start)
    d1 = date(year_end, month_end, day_end)
    delta = d1 - d0
    delta_days = (delta.days + 1)
    
    nr_years = (year_end - year_start) + 1
    
    births = list()
    
    for year in range(year_start, year_end + 1):
        year = str(year)
        births.append(sum(df[year]))
    total_population = sum(births) * (delta_days / (nr_years * 365))
    total_population = int(total_population / scalar)
    return total_population

