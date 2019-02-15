# John

# Find me Beer using this https://api.openbrewerydb.org/breweries?
# 
# Create a dataframe using the api address above with every brewery in the database. Will need to use page and per_page as parameters. per_page max is 50
# 
# Filter this data set down to only micro breweries in states that with begin and end with the same letter
# 
# From the breweries found in part 2, find the farthest north, south, east, and west breweries. You may need to change the dtype of the columns


import requests
import pandas as pd
import numpy as np
import re

url = "https://api.openbrewerydb.org/breweries"

breweries = pd.DataFrame()

page = 1

while True:
    parameters = {"page": page, "per_page": "50"}
    resp = requests.get(url, params=parameters)
    if not resp.json():
        break
    breweries = breweries.append(pd.DataFrame(resp.json()))
    page += 1

len(breweries)

test = "test"

regex = re.compile("(.{1}).*\\1$")

print(regex.match(test))


breweries_small = breweries[
[regex.match(s) for s in breweries.state]
]
