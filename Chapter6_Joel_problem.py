import pandas as pd
import numpy as np

art = pd.read_csv("sf-civic-art-collection.csv")

art.head(5)

# two rows of headers, need to delete first row

art = art.drop(0)

art.head(5)

art.columns

del art['Location 1']

art.columns
art.head(5)

# which artist is most represented, and how many?

art.artist.value_counts().head(1)
art[art.artist=='deSoto, Lewis'][['created_at', 'title']]
