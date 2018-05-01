# -*- coding: utf-8 -*-

# Python’s csv module in the standard library parses the lines in a CSV file
# and allows us to quickly extract the values we’re interested in.
import csv

filename = 'sydney_weather_high.csv'


with open(filename) as f:
    reader = csv.reader(f)  # Return a reader object which will iterate over lines in the given CSV file.
    highs_2017 = []
    highs = []
    for row in reader:      # Read each rows in the csv file. Each role represents a list.
        if row[0] == '2017':
            highs_2017.append(float(row[2]))  # Store the highest temperature in each month of 2017.
        if row[1] == '1':  # Store the highest temperature in each January from 2011 to 2017
            highs.append(float(row[2]))
    print("The highest temperature in each month of 2017 is", highs_2017)
    print("The highest temperature in each January from 2011 to 2017 is", highs)
# The file pointer reaches the End of File (EOF).
# Return the file point to the starting position so you can iterate again.
    f.seek(0)
    for row in reader: # Find the highest temperature in January from 2011 to 2017.
        if row[1] == '1' and row[2] == str(max(highs)):
            print("The year of", row[0], "has the highest temperature in January.", "The highest temperature in January is", max(highs))

"""Output
The highest temperature in each month of 2017 is [39.4, 37.5, 31.9, 28.7, 26.2, 20.4, 26.5, 25.9, 33.8, 35.4, 27.7, 38.3]
The highest temperature in each January from 2011 to 2017 is [35.4, 33.2, 45.8, 36.5, 35.7, 39.2, 39.4]
The year of 2013 has the highest temperature in January. The highest temperature in January is 45.8
"""