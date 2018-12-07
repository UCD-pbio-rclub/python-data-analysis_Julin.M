# notes from Chapter 5

import pandas as pd
from pandas import Series, DataFrame
import numpy as np

# Series and DataFrame are the workhorse data structures

## Series

### A Series is a 1D array-like object with values and names (caled an index)

obj = pd.Series([4,7, -5, 3])

obj

obj.values #an array

obj.index # like range(4) 

### Can create your own index:

obj2 = pd.Series([4, 7, -5, 3], index=['d', 'b', 'a', 'c'])

obj2

# can use index names for single or multiple selection

obj2['d']

obj2[['a', 'a', 'd', 'c']]

### and operations will keep the index

np.exp(obj2)

### these are very similar to a dict.  fixed-length, ordered dict.

'b' in obj2

'e' in obj2

### can convert dict to Series

sdata = {'Ohio': 35000, 'Texas': 71000, 'Oregon': 16000, 'Utah': 5000}

obj3 = pd.Series(sdata)

obj3

sdata

### Series is nicer!

### Can pass an index when converting a dict to select what is kept:

states = ['California', 'Ohio', 'Oregon', 'Texas']

obj4 = pd.Series(sdata, index=states)

obj4

### looking for missing data

pd.isnull(obj4)

pd.notnull(obj4)

### or

obj4.isnull()

### cool alignment feature

obj3 + obj4

## DataFrames

2D

data = {'state': ['Ohio', 'Ohio', 'Ohio', 'Nevada', 'Nevada', 'Nevada'],
        'year': [2000, 2001, 2002, 2001, 2002, 2003],
        'pop': [1.5, 1.7, 3.6, 2.4, 2.9, 3.2]}
frame = pd.DataFrame(data)

frame

frame.head()

frame.head(2)

### specify the order

pd.DataFrame(data, columns=['year', 'state', 'pop'])


frame2 = pd.DataFrame(data, columns=['year', 'state', 'pop', 'debt'], index=['one', 'two', 'three', 'four', 'five', 'six'])

frame2

#if column with no data, then fills with Nas

frame2.columns

frame2['state']

frame2.state #only works in iPython context?  must be valid python variable name

# get a row:
frame2.loc['three']

# add a column.  if as a series, then indexes get matched.

val = pd.Series([-1.2, -1.5, -1.7], index=['two', 'four', 'five'])

frame2['debt'] = val

frame2

## Index objects

### hold axis labels and other meta data.


# 5.2 essential functionality

### reindex

obj = pd.Series([4.5, 7.2, -5.3, 3.6], index=['d', 'b', 'a', 'c'])

obj

obj2 = obj.reindex(['a', 'b', 'c', 'd', 'e'])

obj2

#### can use forward fill to interpolate missing values

obj3 = pd.Series(['blue', 'purple', 'yellow'], index=[0, 2, 4])

obj3

obj3.reindex(range(6), method='ffill')

#### can reindix rows or columns

frame = pd.DataFrame(np.arange(9).reshape((3, 3)), index=['a', 'c', 'd'], columns=['Ohio', 'Texas', 'California'])

frame

frame2 = frame.reindex(['a', 'b', 'c', 'd'])

frame2

#### for columns:

states = ['Texas', 'Utah', 'California']

frame.reindex(columns=states)

### dropping entries from an axis...use the drop method

obj = pd.Series(np.arange(5.), index=['a', 'b', 'c', 'd', 'e'])

obj

new_obj = obj.drop('c')

new_obj

#### columns:

data = pd.DataFrame(np.arange(16).reshape((4, 4)),
        index=['Ohio', 'Colorado', 'Utah', 'New York'],
        columns=['one', 'two', 'three', 'four'])

data

data.drop(['Colorado', 'Ohio'])

data.drop('two', axis=1)

data.drop(['two', 'four'], axis='columns')

obj.drop('c', inplace=True) #caution!!

obj.drop

## Indexing, selecting, filtering

### Indexing of Series works as expected:

obj = pd.Series(np.arange(4.), index=['a', 'b', 'c', 'd'])

obj[obj < 2]

obj[2:4]

obj['b']

### slicing with labels is inclusive

obj['a':'c']

### can also set

obj['b':'c'] = 5

obj

### indexing DataFrames extracts columns

data

data['two']

data[['three', 'one']]

### slicing slice out rows

data[1:3]

### but

data[3] #gives an error

data['three'] #gives a column

# WTF? WTF? WTF? 


### and you can do a boolean array to select rows

data[data['three'] > 5]

### for more sane behavior use the .loc (for labels)  or .iloc (for integers) methods

data.loc['Colorado', ['two', 'three']]

data.iloc[2, [3, 0, 1]]

data.iloc[2]

### Arithmetic and Data Alignment

s1 = pd.Series([7.3, -2.5, 3.4, 1.5], index=['a', 'c', 'd', 'e'])

s2 = pd.Series([-2.1, 3.6, -1.5, 4, 3.1],index=['a', 'c', 'e', 'f', 'g'])

 s1

s2

s1+s2

df1 = pd.DataFrame(np.arange(9.).reshape((3, 3)), columns=list('bcd'),
        index=['Ohio', 'Texas', 'Colorado'])

df2 = pd.DataFrame(np.arange(12.).reshape((4, 3)), columns=list('bde'),
        index=['Utah', 'Ohio', 'Texas', 'Oregon'])

df1

df2

df1 + df2
