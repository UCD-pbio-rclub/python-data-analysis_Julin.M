import pandas as pd
import numpy as np

## 7.1 Handling missing data

# missing data left out of pandas summary stats by default

# NaN represents missing data

string_data = pd.Series(['aardvark', 'artichoke', np.nan, 'avocado'])

string_data

string_data.isnull()

# can also use None

string_data[0] = None

string_data

string_data.isna()

string_data.isnull()

# can use dropna to drop nas from a series

from numpy import nan as NA

data = pd.Series([1, NA, 3.5, NA, 7])

data.dropna()

# for data frame:

# by default dropna drops any row containing a missing number:

data = pd.DataFrame([[1., 6.5, 3.], [1., NA, NA],[NA, NA, NA], [NA, 6.5, 3.]])

data


data.dropna()

# but to only drop rows that are all NA

 data.dropna(how='all')

# can also so the same for columns:

data[4] = NA

data

data.dropna(axis=1, how='all')

# can set thresholds

 df = pd.DataFrame(np.random.randn(7, 3))
 df.iloc[:4, 1] = NA
df.iloc[:2, 2] = NA
df

df.dropna(thresh=2) #thresh is the number of non NA values...

df.dropna(axis=1, thresh=4) 


# filling in missing

df

df.fillna(0)

# difft values per column:

df.fillna({1: 0.5, 2: 0})

# to modify in place

df.fillna(0, inplace=True)

df

### 7.2

## duplicates

data = pd.DataFrame({'k1': ['one', 'two'] * 3 + ['two'], 'k2': [1, 1, 2, 3, 3, 4, 4]})

data

data.duplicated()

data.drop_duplicates()

data['v1'] = range(7)

data

# drop based on duplicates in a subset of columns:

data.drop_duplicates(['k1'])

# specify which duplicate to keep

data.drop_duplicates(['k1', 'k2'], keep='last')

# transforming using a function or mapping

data = pd.DataFrame({'food': ['bacon', 'pulled pork', 'bacon','Pastrami', 'corned beef', 'Bacon', 'pastrami', 'honey ham', 'nova lox'], 'ounces': [4, 3, 12, 6, 7.5, 8, 3, 5, 6]})

data

meat_to_animal = {
  'bacon': 'pig',
  'pulled pork': 'pig',
  'pastrami': 'cow',
  'corned beef': 'cow',
  'honey ham': 'pig',
  'nova lox': 'salmon'
}

lowercased = data['food'].str.lower()

 data['animal'] = lowercased.map(meat_to_animal)
 
 data
 
 # so map fills in values based on a dictionary
 
 # or pass a function:
 
 data['food'].map(lambda x: meat_to_animal[x.lower()])

## replace values

data = pd.Series([1., -999., 2., -999., -1000., 3.]) 

data.replace(-999, np.nan)

data.replace([-999, -1000], np.nan)

data.replace([-999, -1000], [np.nan, 0])

# or pass a dict

data.replace({-999: np.nan, -1000: 0})

## rename axis indexes

data = pd.DataFrame(np.arange(12).reshape((3, 4)), index=['Ohio', 'Colorado', 'New York'], columns=['one', 'two', 'three', 'four'])

data

# like a series the indexes have  map method

transform = lambda x: x[:4].upper()

data.index.map(transform)

# to modify in place, assign to index

data.index = data.index.map(transform)

data

# modify index and create new data frame using rename
data.rename(index=str.title, columns=str.upper)

# can also rename a subset using a dict:

data.rename(index={'OHIO': 'INDIANA'}, columns={'three': 'peekaboo'})

# can rename in place

data.rename(index={'OHIO': 'INDIANA'}, inplace=True)

data

### discretization and binning

 ages = [20, 22, 25, 27, 21, 23, 37, 31, 61, 45, 41, 32]
 
 bins = [18, 25, 35, 60, 100]
 
 cats = pd.cut(ages, bins)
 
 cats
 cats.codes

cats.categories 

pd.value_counts(cats)

# provide your own names
group_names = ['Youth', 'YoungAdult', 'MiddleAged', 'Senior']

pd.cut(ages, bins, labels=group_names)

# specify number of bins instead of bins

data = np.random.rand(20)
pd.cut(data, 4, precision=2)

# related is qcut that splits by quantiles

data = np.random.randn(1000)  # Normally distributed
cats = pd.qcut(data, 4) 

cats

pd.value_counts(cats)

# pass your own quantiles

pd.qcut(data, [0, 0.1, 0.5, 0.9, 1.])

### Detecting and filtering outliers

data = pd.DataFrame(np.random.randn(1000, 4))


data.describe()

col=data[2]

col[np.abs(col) > 3]

data[(np.abs(data) >3).any(1)]

data[np.abs(data) > 3] = np.sign(data) * 3

data.describe()

### permutation and random sampling

 df = pd.DataFrame(np.arange(5 * 4).reshape((5, 4)))
 
 df
 
 sampler = np.random.permutation(5)
 
 sampler
 
 df.take(sampler)
 
df.sample(n=3) 

choices = pd.Series([5, 7, -1, 6, 4])

draws = choices.sample(n=10, replace=True)

draws

### indicator and dummy variables

df = pd.DataFrame({'key': ['b', 'b', 'a', 'c', 'a', 'b'],'data1': range(6)})

df

pd.get_dummies(df['key'])

dummies = pd.get_dummies(df['key'], prefix='key')

df_with_dummy = df[['data1']].join(dummies)

df_with_dummy


mnames = ['movie_id', 'title', 'genres']

movies = pd.read_table('datasets/movielens/movies.dat', sep='::', header=None, names=mnames)
movies[:10]


all_genres = []

for x in movies.genres:
  all_genres.extend(x.split('|'))
  
genres = pd.unique(all_genres)


genres

zero_matrix = np.zeros((len(movies), len(genres)))

dummies = pd.DataFrame(zero_matrix, columns=genres)

gen = movies.genres[0]

gen.split('|')

dummies.columns.get_indexer(gen.split('|'))

for i, gen in enumerate(movies.genres):
  indices = dummies.columns.get_indexer(gen.split('|'))
  dummies.iloc[i, indices] = 1

## 7.3 String manipulation

val = 'a,b,  guido'

val.split(',')

pieces = [x.strip() for x in val.split(',')]

pieces

'::'.join(pieces)

'guido' in val

val.index("b")

val.index(",")

val.find("test")
val.index("test")

val.find(",")

val.find("gui")

val.count(",")

val.replace(",", "::")

### regular expressions

import re

text = "foo    bar\t baz  \tqux"

re.split('\s+', text)

regex = re.compile('\s+')

regex.split(text)

regex.findall(text)

# findall, findsall.  search finds the first occurence.  match only matches at the beginning.

text = """Dave dave@google.com
Steve steve@gmail.com
Rob rob@gmail.com
Ryan ryan@yahoo.com
"""

text

pattern = r'[A-Z0-9._%+-]+@[A-Z0-9.-]+\.[A-Z]{2,4}'

regex = re.compile(pattern, flags=re.IGNORECASE)

regex.findall(text)

m = regex.search(text)

m

text[m.start():m.end()]

print(regex.match(text))

print(regex.sub('REDACTED', text))
pattern = r'([A-Z0-9._%+-]+)@([A-Z0-9.-]+)\.([A-Z]{2,4})'

regex = re.compile(pattern, flags=re.IGNORECASE)

m = regex.match('wesm@bright.net')

m.groups()

regex.findall(text)

print(regex.sub(r'Username: \1, Domain: \2, Suffix: \3', text))

## 7.4 Vectorized string functions

data = {'Dave': 'dave@google.com', 'Steve': 'steve@gmail.com', 'Rob': 'rob@gmail.com', 'Wes': np.nan}

data = pd.Series(data)

data

data.isnull()

data.str.contains('gmail')

pattern = r'([A-Z0-9._%+-]+)@([A-Z0-9.-]+)\.([A-Z]{2,4})'

data.str.findall(pattern, flags=re.IGNORECASE)

matches = data.str.findall(pattern, flags=re.IGNORECASE).str[0]

matches

matches.str.get(1)

data.str[:5]

