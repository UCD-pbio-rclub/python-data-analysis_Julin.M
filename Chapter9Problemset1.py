Chapter 9 problem set 1

# %% packages

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.patches as mpatch

# %% John 1

# Create a smiley face using 4 subplots

fig, axes = plt.subplots(2,2, sharex=True, sharey=True, subplot_kw = {'aspect': 'equal'}, figsize=(5,5))

plt.subplots_adjust(wspace=0, hspace=0)

# the overall face
axes[0,0].add_patch(plt.Circle((1,0), radius=1))
axes[0,1].add_patch(plt.Circle((0,0), radius=1))
axes[1,0].add_patch(plt.Circle((1,1), radius=1))
axes[1,1].add_patch(plt.Circle((0,1), radius=1))

# eyes
axes[0,0].add_patch(plt.Circle((.5,.5), radius=.1, color="k"))
axes[0,1].add_patch(plt.Circle((.5,.5), radius=.1, color="k"))

# mouth
axes[1,0].add_patch(mpatch.Arc(xy=(1,.6), width=1, height=.6, theta1=180, theta2=270))
axes[1,1].add_patch(mpatch.Arc(xy=(0,.6), width=1, height=.6, theta1=270, theta2=360))