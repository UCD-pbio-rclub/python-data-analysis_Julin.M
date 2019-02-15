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

# Min Yao

""". Using the same data from last week. (Import my RNA-Seq CPM data from 'Expression Browser_CPM_practice.xlsx' file. Expression Browser_CPM_practice.xlsx) In column labels, the first number means plant genotype and the second part is one letter and a number which means the treatment conditions and sample numbers. please change them to multilevel hierarchical columns labels with column name in front of the whole data. For example, '6_c1' change it to genotype = '6', treatments = 'c', sample_number = '1'.
2. In row labels, these numbers are Solyc ID for tomatoes. "Solyc" is the 5 letter abbreviation of Solanum lycopersicum, the 2 digit number following the 'Solyc' denotes the chromosome, 'g' denotes that the sequence is a gene, and the 6 digit number following the 'g' identifies the gene on the chromosome. The '.1' denotes the annotation version number of the locus. Please use hierarchical indexing to label another level of index to show which chromosome each gene on and give the index name 'chromosome'.
3. In order to compare genotypes and treatments, you want to know the summary statistics of different genotypes and treatments. Please calculate the average expression level of each gene in different genotypes and treatments.
"""

cpm = pd.read_excel('https://github.com/UCD-pbio-rclub/python-data-analysis_MinYaoJ/raw/master/Expression%20Browser_CPM_practice.xlsx')

cpm.head()

cpm = cpm.set_index('Name')

cpm.head()

newcols = pd.DataFrame(cpm.columns)

newcols.head()

newcols = newcols[0].str.split("_", expand=True)

newcols.head()

newcols = pd.concat([newcols[0],newcols[1].str[0], newcols[1].str[1]], axis=1)

newcols.columns = ['genotype', 'treatment', 'sample_number']

newcols.head()


cpm.columns = pd.MultiIndex.from_frame(newcols)

cpm.head()


chrom = cpm.index.str.extract(r'(\d\d)g')[0]

cpm.index = [cpm.index, chrom]

cpm.index.names = ['gene', 'chrom']

cpm.shape

cpm.head()

cpm_means = cpm.mean(level=['genotype', 'treatment'], axis=1)

cpm_means.head()
