#!/usr/bin/python
# Deepak Ramanath

import sys
import os
import pandas as pd
import random
import collections
import datetime
import matplotlib.pyplot as plt

# Function
def dateList():
	startDate = datetime.date(2015, 01, 1)
	endDate = datetime.date(2015, 01, 8)
	stepDate = datetime.timedelta(days = 1)
	while startDate < endDate:
		dates.append(startDate.strftime("%d"))
		startDate = startDate + stepDate
	

def tempCities():
	day = 0
	while day < len(dates):
		tempCanberra.append(random.uniform(10.0, 20.0))
		tempMelbourne.append(random.uniform(15.0, 25.0))
		tempSydney.append(random.uniform(17.0, 30.0))
		day = day + 1

# Essential empty lists
dates = []
tempCanberra = []
tempMelbourne = []
tempSydney = []

# Calling the functions
dateList()	
tempCities()

# Dictionary generation
dictTemp = {'Date': dates, 'Canberra': tempCanberra, 'Melbourne': tempMelbourne, 'Sydney': tempSydney }
dictTempOrdered = collections.OrderedDict(dictTemp)

# Pandas Data Frame
dateTemp = pd.DataFrame(dictTempOrdered)

# Changind the index to 'Date'
dateTemp = dateTemp.set_index('Date')
print dateTemp


# Plotting the temperature variation
plt.plot(dateTemp.index, dateTemp.Canberra, marker = 'o', color = 'b', label = 'Canberra')
plt.plot(dateTemp.index, dateTemp.Melbourne, marker = 'o', color = 'g', label = 'Melbourne')
plt.plot(dateTemp.index, dateTemp.Sydney, marker = 'o', color = 'r', label = 'Sydney')
plt.xlabel('Days [Index]')
plt.ylabel('Temperature [C]')
plt.title('Temperature variation for different cities')
plt.legend(loc = 'upper right')
plt.show()
