# -*- coding: utf-8 -*-

# Python’s csv module in the standard library parses the lines in a CSV file
# and allows us to quickly extract the values we’re interested in.
import csv
# Matplotlib is a Python 2D plotting library which produces publication quality
# figures in a variety of hardcopy formats and interactive environments across platforms.
# The matplotlib.pyplot module contains functions that allow you to generate many kinds of plots quickly.
from matplotlib import pyplot as plt

filename = 'sydney_weather_high.csv'

with open(filename) as f:
    reader = csv.reader(f)
    highs_2016 = []     # Store monthly temperature data of 2016
    highs_2017 = []     # Store monthly temperature data of 2017
    highs = []          # Store January temperature data
    for row in reader:
        if row[0] == '2017':
            highs_2017.append(float(row[2]))
        if row[0] == '2016':
            highs_2016.append(float(row[2]))
        if row[1] == '1':       # January data
            highs.append(float(row[2]))

fig = plt.figure(dpi=128, figsize=(10, 6))
plt.plot(list(range(2011,2018)),highs)     # The X-axis is the year and the Y-axis is the temperature in January

# Format plot.
plt.title("Highest Temperature in January", fontsize=18)
plt.xlabel("Year", fontsize=16)
plt.ylabel("Temperature (C)", fontsize=16)
plt.tick_params(axis='both', which='major', labelsize=16)
plt.show()


fig = plt.figure(dpi=128, figsize=(10, 6))
plt.plot(list(range(1,13)), highs_2016, c='red', label='2016')  # The X-axis is each month of the year. The Y-axis is the monthly highest temperature in 2016
plt.plot(list(range(1,13)), highs_2017, c='blue', label='2017')  # The X-axis is each month of the year. The Y-axis is the monthly highest temperature in 2016

# Format plot.
plt.title("Monthly high temperatures of Sydney in 2016 and 2017", fontsize=18)
plt.xlabel("Month", fontsize=16)
plt.ylabel("Temperature (C)", fontsize=16)
plt.tick_params(axis='both', which='major', labelsize=16)
plt.legend()  # Add the legend
plt.show()