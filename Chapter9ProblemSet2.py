# Julin

# %% load packages
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
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

# %% John

# Recreate the two plots below using this dataset: diamonds

diamonds = pd.read_csv("https://raw.githubusercontent.com/UCD-pbio-rclub/python-data-analysis_JohnD/master/datasets/diamonds.csv")

diamonds.head()

# %% plot 1

diamonds['bin'] = pd.cut(diamonds.carat, bins=27)

diamonds.head()

diamondsgroup = diamonds.groupby('bin')

diamonds['binmeans'] = diamondsgroup['carat'].transform(np.mean)

diamonds['binmeans'] = np.round(diamonds.binmeans, 2)

ax = sns.boxplot(x='binmeans', y = 'price', data = diamonds)
ax.set_xlabel('carat')
plt.xticks(rotation=90)

# %% plot2 

diamonds['qbin'] = pd.qcut(diamonds.carat, 19)

diamondsgroup = diamonds.groupby('qbin')

diamonds['qbinmeans'] = diamondsgroup['carat'].transform(np.mean)

diamonds['qbinmeans'] = np.round(diamonds.qbinmeans, 2)

diamondslist = [diamonds.price[diamonds.qbinmeans==qb] for qb in np.unique(diamonds['qbinmeans']) ]


widths = diamondsgroup['carat'].max() - diamondsgroup['carat'].min()

fig = plt.boxplot(x=diamondslist,
                  positions = np.unique(diamonds['qbinmeans'])*1.5,
                  widths = widths,
                  labels=np.unique(diamonds['qbinmeans']))


# %% Joel

# Use the weather data from the nycflights13 dataset (https://raw.githubusercontent.com/hadley/nycflights13/master/data-raw/weather.csv) to have some fun plotting.

weather = pd.read_csv("https://raw.githubusercontent.com/hadley/nycflights13/master/data-raw/weather.csv")

weather.head()

# %% How would you look at the overall distribution of temperatures in each airport (origin). For now, don't filter by month/day/hour.

sns.violinplot(x='origin', y='temp', data=weather)

# %% Plot the temperatures over a warm and a cold month. Is the scale in farenheit or celsius?

weathersmall = weather[weather.month.isin([2, 8])]


sns.violinplot(x='origin', y='temp', hue='month', split=True, data=weathersmall)

# %% Kae

# Using the data here please make a bar graph showing the number of men and the number of women (a bar for each) that survived the trip on the titanic at each age point.

titanic = pd.read_csv("https://raw.githubusercontent.com/UCD-pbio-rclub/python-data-analysis_KaeL/master/titanic.csv")

titanic.head()

titanicgroups = titanic.groupby(['Sex', 'Age'])

survived = pd.DataFrame(titanicgroups.Survived.sum()).reset_index()

survived

sns.barplot(x='Age', y='Survived', hue='Sex',  data=survived)
