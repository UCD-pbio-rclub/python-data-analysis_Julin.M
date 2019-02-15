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


## 8.2, combining and joining

df1 = pd.DataFrame({'key': ['b', 'b', 'a', 'c', 'a', 'a', 'b'],
   'data1': range(7)})

df2 = pd.DataFrame({'key': ['a', 'b', 'd'],
   'data2': range(3)})

df1

df2

pd.merge(df1, df2)

pd.merge(df1, df2, on='key')

pd.merge(df2, df1, on='key')

## merging on index

## join method

## concatenate for binding on an axis

arr = np.arange(12).reshape((3, 4))
arr

np.concatenate([arr, arr], axis=1)
### for pandas objects, concat

### simple case, no overlap in labels

s1 = pd.Series([0, 1], index=['a', 'b'])

s2 = pd.Series([2, 3, 4], index=['c', 'd', 'e'])

s3 = pd.Series([5, 6], index=['f', 'g'])

pd.concat([s1, s2, s3])

pd.concat([s1, s2, s3], axis=1, sort=True)

s4 = pd.concat([s1, s3])
s4
pd.concat([s1, s4], axis=1)

pd.concat([s1, s4], axis=1, join='inner')

result = pd.concat([s1, s1, s3], keys=['one', 'two', 'three'])

result

result = pd.concat([s1, s1, s3], keys=['one', 'two', 'three'], axis=1, sort=True)

result

# combining data with overlap
# neither join nor concatenate are appropriate

a = pd.Series([np.nan, 2.5, 0.0, 3.5, 4.5, np.nan],
   index=['f', 'e', 'd', 'c', 'b', 'a'])

b = pd.Series([0., np.nan, 2., np.nan, np.nan, 5.],
   index=['a', 'b', 'c', 'd', 'e', 'f'])
   
   a

b
np.where(pd.isnull(a), b, a)

# so where a is null, use b, otherwise a

# equivalent in pandas is combine_first

b.combine_first(a)
# also on data frames, works column by column

df1 = pd.DataFrame({'a': [1., np.nan, 5., np.nan],
   'b': [np.nan, 2., np.nan, 6.],
   'c': range(2, 18, 4)})
   
df2 = pd.DataFrame({'a': [5., 4., np.nan, 3., 7.],
   'b': [np.nan, 3., 4., 6., 8.]})
   
df1

df2

df1.combine_first(df2)

## reshape with hierarchical indexing

# stack from columns to rows

# unstack rotates or pivots rows into columns

data = pd.DataFrame(
   np.arange(6).reshape((2, 3)),
   index=pd.Index(['Ohio', 'Colorado'], name='state'),
   columns=pd.Index(['one', 'two', 'three'], name='number'))

data

result = data.stack() # column names become a column and values become a column

result # a hierarchically arranged series

result.unstack() #innermost level, or "number"

result.unstack(0)

result.unstack('state')

df = pd.DataFrame({'left': result, 'right': result + 5},
                  columns=pd.Index(['left', 'right'], name='side'))

df

df.unstack("state")

df

df.unstack('state').stack('side')

# long to wide

data = pd.read_csv('examples/macrodata.csv')

data.head()

periods = pd.PeriodIndex(year=data.year, quarter=data.quarter,
                         name='date')

periods

columns = pd.Index(['realgdp', 'infl', 'unemp'], name='item')

columns

data = data.reindex(columns=columns)

data.head()

data.index = periods.to_timestamp('D', 'end')

data.head()

ldata = data.stack().reset_index().rename(columns={0: 'value'})

# "0" in "rename because that is the first unamed column and gets 0 by default

ldata[:10]

pivoted = ldata.pivot('date', 'item', 'value')

# first argument is what should be row index, 
# second is col index, and last is what to fill with

pivoted.head()

# if more than one value column:

ldata['value2'] = np.random.randn(len(ldata))

ldata[:10]

pivoted = ldata.pivot('date', 'item')

pivoted.head() # hierarchical columns

# sane as creating a hierarchical index and then unstacking

ldata.set_index(['date', 'item']).unstack('item').head()

# pivot from wide to long

df = pd.DataFrame({'key': ['foo', 'bar', 'baz'],
                   'A': [1, 2, 3],
                   'B': [4, 5, 6],
                   'C': [7, 8, 9]})

df

melted = pd.melt(df, ['key'])

melted

reshaped = melted.pivot('key', 'variable', 'value')

reshaped

reshaped.reset_index() #if we want the key to be a column

pd.melt(df, id_vars=['key'], value_vars=['A', 'B'])

pd.melt(df, value_vars=['A', 'B', 'C'])

pd.melt(df, value_vars=['key', 'A', 'B'])
