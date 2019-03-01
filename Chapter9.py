# Chapter 9 part 1 notes

import pandas as pd
import numpy as np

import matplotlib.pyplot as plt

# %matplotlib

data = np.arange(10)

data

plt.plot(data)

# plots are inside of figures
# creat a figure object

fig = plt.figure()

ax1 = fig.add_subplot(2, 2, 1)
#(rows, columns, subplot#)
ax2 = fig.add_subplot(2, 2, 2)

ax3 = fig.add_subplot(2, 2, 3)

fig

plt.plot(np.random.randn(50).cumsum(), 'k--')

#run these together to get on same plot.
fig = plt.figure()
ax1 = fig.add_subplot(2, 2, 1)
ax2 = fig.add_subplot(2, 2, 2)
ax3 = fig.add_subplot(2, 2, 3)
plt.plot(np.random.randn(50).cumsum(), 'k--')
#adds to last subplot worked on

_ = ax1.hist(np.random.randn(100), bins=20, color='k', alpha=0.3)

ax2.scatter(np.arange(30), np.arange(30) + 3 * np.random.randn(30))

fig

# create subplots all at once

fig, axes = plt.subplots(2, 3)

axes

# adjusting spacing between subplots
plt.subplots_adjust(left=None, bottom=None, right=None, top=None, wspace=None, hspace=None)
 
fig, axes = plt.subplots(2, 2, sharex=True, sharey=True)
for i in range(2):
    for j in range(2):
        axes[i, j].hist(np.random.randn(500), bins=50, color='k', alpha=0.5)
plt.subplots_adjust(wspace=0, hspace=0)
