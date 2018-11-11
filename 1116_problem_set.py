import pandas as pd

import numpy as np

# problems for Nov 16

# import the data set

data = pd.read_csv("data/Brapa_cpm.csv")

data = np.array(data)

data.shape

# rows are genes (100 genes), columns are samples (36)

# Q1: make a new array where the values are converted to log2 cpm

data.min()

data.max()

data_log2 = np.log2(data - np.min(data) + .001)

# Q2: Which gene has the highest expression?

gene_index = np.array(range(data.shape[0]))

gene_index[data.mean(1) == data.mean(1).max()]

# Q3: Make a new array in which each row is sorted by expression

data2 = np.sort(data, axis=1)

data[0:5, 0:5]

data2[0:5,0:5]

# Q4: Make a new array in which the samples are sorted according to average expression.  NOTE this is different than sorting each row...explain how

# This is different because in Q3 each row is sorted independently of the other rows.  Q4 asks us to sort by average expression level so that the relationships within columns is preserved.  That is readings remain with their samples.

sort_order = np.argsort(data.mean(0))

sort_order
sort_order.shape

data3 = data[:,sort_order].copy()

data3[0:5, 0:5]

data3.mean(0)

# Q5: what is the total number of unique values in the table?

np.unique(data).shape

# Q6: Make a new array in which any cell that has less than 10 cpm is replaced with 0

data4 = np.where(data < 10, 0, data)

data4[0:5, 0:5]

data[0:5, 0:5]

# Q7: Make a new array that only retains genes that are expressed at > 10 cpm in at least half the samples.  (I haven't checked, maybe all genes will pass)

data_boolean10cpm = data > 10

data_boolean10cpm[0:5, 0:5]

data_gt10cpm_keep = data_boolean10cpm.mean(1) > 0.5

data_gt10cpm_keep

data_small = data[data_gt10cpm_keep, :]

data_small.shape

data_small[0:5, 0:5]
# Q8 calculate the standard deviation for each gene using the builtin function

data.std(1)

# Q9 calculate the standard deviation for each gene WITHOUT using the builtin function



# Q10 create a slice that contains the first 10 samples

# Q11 Changing topics...generate and plot a 2D random walk (see Chapter 4.7)


