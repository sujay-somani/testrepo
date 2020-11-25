# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

import numpy as np 
import pandas as pd
import matplotlib as mp
import matplotlib.pyplot as plt
import datetime as dt 
import scipy as sc

# Hello World ! Program #

for i in range(8):
    print("Hello World!")
    
#Change Directory#

import os 
from os import listdir , system 

pwd
os.getcwd()
os.chdir('C:\\Users\\sujsoman\\Data')
os.mkdir('New Folder')

os.listdir()
os.system("ls")
os.system("dir")

os.chdir('C:\\Users\\sujsoman\\Data\\noaa-weather-data-jfk-airport.tar\\noaa-weather-data-jfk-airport')
os.chdir('C:\\Users\\sujsoman\\Data\\trade data')

# UN Trade Data #

trade_data = pd.read_csv('SYB63_123_202009_Total Imports, Exports and Balance of Trade.csv')
trade_data.head()
trade_data.columns

# JFK Weather Data #

jfk_data = pd.read_csv('C:/Users/sujsoman/Data/noaa-weather-data-jfk-airport.tar/noaa-weather-data-jfk-airport/jfk_weather_cleaned.csv')
jfk_data.head()
jfk_data.columns
jfk_data.describe()
print(jfk_data)

#Covid Charting Program #

covid19_data = pd.read_csv('C:/Users/sujsoman/Data/results-20201029-for_use.csv')
print(covid19_data)
covid19_data.head()
covid19_data.columns

z1 = covid19_data[covid19_data['countries_and_territories'] == 'India' ]
z2 = covid19_data[covid19_data['countries_and_territories'] == 'Italy' ]
z3 = covid19_data[covid19_data['countries_and_territories'] == 'France' ]
z4 = covid19_data[covid19_data['countries_and_territories'] == 'Germany' ]
z5 = covid19_data[covid19_data['countries_and_territories'] == 'United_States_of_America' ]

plt.plot(z1['date'],z1['daily_confirmed_cases'],color ='blue',linewidth= 1,label='India')
plt.plot(z2['date'],z2['daily_confirmed_cases'],color ='red',linewidth= 1,label='Italy')
plt.plot(z3['date'],z3['daily_confirmed_cases'],color ='green',linewidth= 1,label='France')
plt.plot(z4['date'],z4['daily_confirmed_cases'],linestyle='--',color ='brown',linewidth= 1,label='Germany')
plt.plot(z5['date'],z5['daily_confirmed_cases'],color ='black',linewidth= 1,label='USA')
plt.legend()
plt.ylim(0,100000)
plt.xticks(z1['date'].iloc[::30],rotation = 30)
plt.xlabel('date')
plt.ylabel('daily confirmed cases')
plt.title('Trend of Daily Cases for 5 Countries')
plt.show()

