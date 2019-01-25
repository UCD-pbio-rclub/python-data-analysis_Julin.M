import pandas as pd
import numpy as np
from numpy import nan as NA

data = pd.DataFrame(np.random.randn(5,5))

data.iloc[3] = NA

data.iloc[2:, 3] 

data

data.mean()

data.fillna(data.mean())

datafill = len(data) - data.count() < 3  # the lhs gives number of NAs per column

datafill

colmeans = data.mean()

colmeans[[not i for i in datafill]] = NA # replace the colmeans with NA

colmeans

data.fillna(colmeans)
