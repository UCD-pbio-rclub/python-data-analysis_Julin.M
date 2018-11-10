import pandas as pd

import numpy as np

# problems for Nov 16

# import the data set

data = pd.read_csv("data/Brapa_cpm.csv")

data = np.array(data)

data.shape

# rows are genes (100 genes), columns are samples (36)

# Q1: make a new array where the values are converted to log2 cpm

# Q2: Which gene has the highest expression?

# Q3: Make a new array in which each row is sorted by expression

# Q4: Make a new array in which the samples are sorted according to average expression.  NOTE this is different than sorting each row...explain how

# Q5: what is the total number of unique values in the table?

# Q6: Make a new array in which any cell that has less than 10 cpm is replaced with 0

# Q7: Make a new array that only retains genes that are expressed at > 10 cpm in at least half the samples.  (I haven't checked, maybe all genes will pass)

# Q8 calculate the standard deviation for each gene using the builtin function

# Q9 calcualte the standard deviation for each gene WITHOUT using the builtin function

# Q10 create a slice that contains the first 10 samples

# Q11 Changing topics...generate and plot a 2D random walk (see Chapter 4.7)


