'''
Function to transform the timestamp to datetime format

By Dr. Raymond Hoogendoorn
Copyright 2020
'''

import datetime

def transformTimestamp(start_date, timestamp):
    start_date_temp = datetime.datetime.strptime(start_date, "%Y-%m-%d")
    new_date = start_date_temp + datetime.timedelta(days=int(timestamp))
    return new_date

