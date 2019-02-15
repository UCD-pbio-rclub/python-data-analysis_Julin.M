import pandas as pd
import numpy as np
import re

# John

""" Read these 3 files into python and make them data frames: 
    flights.xlsx, weather.tsv, airlines.csv

Remove the 'hour' column from the weather data frame

Inner join these three data frames. You will have to modify certain columns
 and be explicit about which columns to merge on. (should have 29 columns in the end)

Set year,month,day,and origin to indexes
"""

flights = pd.read_excel('https://github.com/UCD-pbio-rclub/python-data-analysis_JohnD/raw/master/datasets/nycflights13/flights.xlsx', 'flights')

flights.head()

flights.shape

flights.time_hour.head()

flights.time_hour = np.datetime_as_string(flights.time_hour,'s')

flights.time_hour.head()

weather = pd.read_csv('https://github.com/UCD-pbio-rclub/python-data-analysis_JohnD/raw/master/datasets/nycflights13/weather.tsv', sep='\s+')

weather.head()

weather.shape

weather = weather.drop('hour', axis=1)

weather.time_hour = weather.time_hour.str.replace('Z', '')

weather.head()

airlines = pd.read_csv('https://github.com/UCD-pbio-rclub/python-data-analysis_JohnD/raw/master/datasets/nycflights13/airlines.csv')

airlines.head()

airlines.shape

flight_weather = pd.merge(
    flights, weather, 
    on = ['year', 'month', 'day', 'time_hour', 'origin'],
    how = 'left')

flight_weather.shape

flight_weather.head()

flight_weather_air = pd.merge(flight_weather, airlines, on='carrier')

flight_weather_air.shape

flight_weather_air.head()

