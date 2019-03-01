# plotting problem

# %% load packages
import pandas as pd
import numpy as np
import seaborn as sns

# %% get the data

tomato = pd.read_csv("data/Tomato.csv")

tomato.head()

# %% make a boxplot of hypocotyl length ("hyp") with the data plotted separately for species and trt

# try doing this both with and without using facets

sns.boxplot(x='species', y='hyp', hue='trt', data=tomato)

# %% facets

sns.catplot(x='trt',
            hue='trt',
            y='hyp',
            kind='box',
            col='species',
            data=tomato)
    
# %% Make a plot of the internode data, int1, int2, int3, and int4 where each internode is in a
# different facet.  plot values for each trt and species.  Layout the plot so that it is a 2X2 grid 

tomato_long = pd.melt(tomato[['trt','species','int1','int2','int3','int4']],
                       id_vars=['trt', 'species'],
                       var_name='internode',
                       value_name='length')

tomato_long.head()

sns.catplot(x='species', y='length', hue='trt', col='internode', kind='box', data=tomato_long, col_wrap=2)


