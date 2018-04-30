# -*- coding: utf-8 -*-

import csv

filename = 'sydney_weather_high.csv'

with open(filename) as f:
    reader = csv.reader(f)
    month_highs = []    # Used to store
    highs = []  # Used to store the
    months = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October',
              'November', 'December']
    for month in range(1,13):  # Iterate each month of the year.
        # Make the list empty for the next "for" iteration.
        # Otherwise, all data will be appended to the same list.
        month_highs = []
        for row in reader:
            if row[1] == str(month):
                month_highs.append(float(row[2]))
        # Store the monthly data in a single list for future queries
        highs.append(month_highs)
        print("The highest temperature in",months[month-1],"is",month_highs)
        f.seek(0)  # For the next iteration, returning the file point to the start of the file

    f.seek(0) # For the following iteratin, returning the file point to the start of the file
    # Find out for each month, which year has the highest temperature and what the temperature is.
    for month in range(0,12):
        for row in reader:
            if row[1] == str(month+1) and row[2] == str(max(highs[month])):
                print('In',months[month],',','the max temperature is',max(highs[month]),'and the year is',row[0])
        f.seek(0)

"""Output
The highest temperature in April is [27.0, 28.3, 28.7, 29.9, 31.7, 34.2, 28.7]
The highest temperature in May is [23.3, 29.1, 26.4, 27.1, 27.5, 28.2, 26.2]
The highest temperature in June is [21.0, 20.9, 22.2, 22.8, 22.9, 22.2, 20.4]
The highest temperature in July is [21.4, 22.9, 24.3, 25.0, 21.0, 25.7, 26.5]
The highest temperature in August is [25.7, 29.2, 24.7, 23.2, 28.3, 25.2, 25.9]
The highest temperature in September is [32.5, 33.2, 31.8, 33.5, 29.8, 24.6, 33.8]
The highest temperature in October is [34.3, 34.2, 37.3, 33.8, 37.0, 33.6, 35.4]
The highest temperature in November is [37.2, 33.3, 34.2, 36.5, 40.9, 32.5, 27.7]
The highest temperature in December is [26.8, 33.0, 36.0, 32.0, 35.3, 37.8, 38.3]
In January , the max temperature is 45.8 and the year is 2013
In February , the max temperature is 41.5 and the year is 2011
In March , the max temperature is 36.4 and the year is 2015
In April , the max temperature is 34.2 and the year is 2016
In May , the max temperature is 29.1 and the year is 2012
In June , the max temperature is 22.9 and the year is 2015
In July , the max temperature is 26.5 and the year is 2017
In August , the max temperature is 29.2 and the year is 2012
In September , the max temperature is 33.8 and the year is 2017
In October , the max temperature is 37.3 and the year is 2013
In November , the max temperature is 40.9 and the year is 2015
In December , the max temperature is 38.3 and the year is 2017
"""
