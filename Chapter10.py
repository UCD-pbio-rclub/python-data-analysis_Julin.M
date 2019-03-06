import numpy as np
import pandas as pd

df = pd.DataFrame({'key1': ['a', 'a', 'b', 'b', 'a'],
                   'key2': ['one', 'two', 'one', 'two', 'one'],
                   'data1': np.random.randn(5),
                   'data2': np.random.randn(5)})

df

grouped = df['data1'].groupby(df['key1'])

grouped.mean()

means = df['data1'].groupby([df.key1, df.key2]).mean()

means

means.unstack()

# %% can use any arrays of the right length

states = np.array(['Ohio', 'California', 'California', 'Ohio', 'Ohio'])

years = np.array([2005, 2005, 2006, 2005, 2006])

df['data1'].groupby([states, years]).mean()

# %% if in same data frame, then can pass column names

df.groupby('key1').mean()

df.groupby(['key1', 'key2']).mean()

# %% how may in a group?

df.groupby(['key1', 'key2']).size()

# %% iterating over groups

for name, group in df.groupby('key1'):
    print(name)
    print(group)

# %% if multiple keys, first element is a tuple of keys

for (k1, k2), group in df.groupby(['key1', 'key2']):
    print((k1, k2))
    print(group)

# %% create a dict of the groups

pieces = dict(list(df.groupby('key1')))

pieces

pieces['b']

# %% can group on other axes

df.dtypes

grouped = df.groupby(df.dtypes, axis=1)

for dtype, group in grouped:
    print(dtype)
    print(group)