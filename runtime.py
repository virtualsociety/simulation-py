'''
Function to calculate the runtime

By Dr. Raymond Hoogendoorn
Copyright 2020
'''

from datetime import datetime

def generateRuntime(startdate, enddate):
    date_format = "%Y-%m-%d"
    a = datetime.strptime(startdate, date_format)
    b = datetime.strptime(enddate, date_format)
    delta = b - a
    runtime = delta.days 
    return runtime
