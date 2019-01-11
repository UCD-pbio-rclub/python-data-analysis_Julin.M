"""
Import the "Tomato.csv" data set from this repository
Make a new data frame that retains the "trt", "hyp", and "species" columns.
Now subset the new data frame do that it only has the S. chilense data.
Calculate the mean of the hyp column separately for the "H" and "L" treatments.
"""

import numpy as np
import pandas as pd
from pandas import Series, DataFrame

tomato = pd.read_csv("data/Tomato.csv")

tomato

tomato.head()

tomato_small = tomato[['trt', 'hyp', 'species']]

tomato_small.head()

# alternative, using loc
tomato_small = tomato.loc[:,['trt', 'hyp', 'species']]

tomato_chilense = tomato_small[tomato_small['species']=="S. chilense"]

tomato_chilense.head()

# alternative
tomato_chilense = tomato_small[tomato_small.species=="S. chilense"]

tomato_chilense.head()

np.mean(tomato_chilense.hyp[tomato_chilense.trt=="H"])

tomato_chilense.hyp[tomato_chilense.trt=="H"].mean()

tomato_chilense.hyp[tomato_chilense.trt=="L"].mean()

trts = tomato_chilense.trt.unique()

[tomato_chilense.hyp[tomato_chilense.trt==t].mean() for t in trts]
# Min Yao
"""
Import the data that we used last week as a DataFrame.
We want to only focus on wyo_leaf_FPsc samples, so please slice out these samples.
In addition, assuming that wyo_leaf_FPsc_02_052 is our control sample, we want to only select the genes having expression level > 1 based on their expression level in wyo_leaf_FPsc_02_052. Please slice out a new DataFrame based on these criteria.
How many genes and samples we have in this new DataFrame?
"""

data = pd.read_csv("data/Brapa_cpm.csv")

data_small = data.iloc[:,:18]

data_small.head()

data_small1 = data_small[data_small.wyo_leaf_FPsc_02_052 > 1]

data_small1.head(10)

data_small1.shape

  