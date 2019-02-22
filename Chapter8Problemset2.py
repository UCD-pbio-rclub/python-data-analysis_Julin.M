# Problem set Chapter 8 2

import pandas as pd
import numpy as np

# John's

import random
def RandomBingoNumber():
    letter = random.choice('BINGO')
    if letter == 'B':
        number = str(random.randint(1,15))
    if letter == 'I':
        number = str(random.randint(16,30))
    if letter == 'N':
        number = str(random.randint(31,45))
    if letter == 'G':
        number = str(random.randint(46,60))
    if letter == 'O':
        number = str(random.randint(61,75))
    call = {letter:[number]}
    return call

"""Using this function and everything we have learned so far in this book, create a valid bingo card in the form of a data frame. The numbers on your card must be generated using the function above. There are simpler ways to do this, but we going to do it the hard way."""

df = pd.DataFrame(index=range(5), columns=["B", "I", "N", "G", "O"])

df

c = 0

# while any(df.isna()): # why doesn't this work?

while df.isna().sum().sum() > 0:
    entry = RandomBingoNumber()  # get an entry
    i = df[entry.keys()].isna().sum()[0]  # number of NAs
    print(entry, i, df)
    if i == 0:
        next
    else:
        df.loc[(i-1), entry.keys()] = int(list(entry.values())[0][0])

df.loc[2, 'N']='Free'

df
