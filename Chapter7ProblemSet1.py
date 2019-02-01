## John

# Create a DataFrame using

import pandas as pd
import numpy as np
from numpy import NAN as NA
df = pd.DataFrame(np.random.randn(10, 10), columns= ['a','b','c','d','e','f','g','h','i','j'])
df.iloc[:7, 1:3] = NA
df.iloc[4:8, 5:8] = NA
df.iloc[:,9] = NA
df

# 1. Remove all rows where at least half the columns have missing data

df.shape[1]

df1 = df.dropna(thresh = (df.shape[0]/2), axis = 0 )

df1

# 2. Remove all columns where at least half the rows have missing data

df2 = df.dropna(thresh=(df.shape[1]/2), axis=1)
df2

# 3. Combine problems 2 and 3. Does the order matter?

# yes. the order will matter

# row, then columns
df3a = df1.dropna(thresh=(df1.shape[1]/2), axis=1)
df3a

# columns then rows

df3b = df2.dropna(thresh=(df2.shape[0]/2), axis=1)
df3b

# 4. Remove all rows which have NA in either column 'b' or 'f'

df.b.isnull()
df.f.isnull()

keep = [not (df.b.isnull()[x] or df.f.isnull()[x]) for x in range(0,10)]

df[keep]

## Min Yao

# Import my RNA-Seq CPM data from 'Expression Browser_CPM_practice.xlsx' file. Please made the Itag number become the row index. How many genes in this data set?

cpm = pd.read_excel("https://github.com/UCD-pbio-rclub/python-data-analysis_MinYaoJ/raw/master/Expression%20Browser_CPM_practice.xlsx")

cpm.head()

cpm.shape[0] # number of genes

cpm.index = cpm.Name

cpm = cpm.drop("Name", axis=1)

cpm.head()
# Please replace all 0 with NA.

cpm.replace(0, np.nan, inplace = True)

cpm.head()

#We want to remove the genes that have no expression in all samples. How many genes left after we remove these genes.

cpmfilter = cpm[cpm.isna().sum(axis=1) > 0]

cpmfilter.head()

cpmfilter.shape

