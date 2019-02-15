# chapter 8 notes

import pandas as pd
import numpy as np

## hierarchical indexing
## Two or index levels on an axis

data = pd.Series(np.random.randn(9),
    index=[['a', 'a', 'a', 'b', 'b', 'c', 'c', 'd', 'd'],
    [1, 2, 3, 1, 3, 1, 2, 2, 3]])
    
data

data.index
data['b']

data['b':'c']

data.loc[:, 2]

data.unstack()

data.unstack().stack()

## with a data frame, either (or both) axes can have a hierarchical index

frame = pd.DataFrame(np.arange(12).reshape((4, 3)),
   index=[['a', 'a', 'b', 'b'], [1, 2, 1, 2]],
   columns=[['Ohio', 'Ohio', 'Colorado'],
   ['Green', 'Red', 'Green']])

frame

frame.index.names = ['key1', 'key2']

frame.columns.names = ['state', 'color']

frame
frame['Ohio']

frame.swaplevel('key1', 'key2')
frame.sort_index(level=1)
frame.sort_index(level='key2')
frame.sort_index(level=1, axis=1)
frame.swaplevel(0, 1).sort_index(level=0) #faster when sorting with the outermost level

## summary stats by level

frame.sum(level='key2')

frame.sum(level='color', axis=1)

## moving index to column and vice-versa

frame = pd.DataFrame({'a': range(7), 'b': range(7, 0, -1),
   'c': ['one', 'one', 'one', 'two', 'two',
   'two', 'two'],
   'd': [0, 1, 2, 0, 1, 2, 3]})

frame

frame2 = frame.set_index(['c', 'd'])

frame2

## keep the columns

frame.set_index(['c', 'd'], drop=False)

## reverse it

frame2.reset_index()















