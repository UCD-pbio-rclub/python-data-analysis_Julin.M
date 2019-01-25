import pandas as pd
import numpy as np
import requests
import re

### Kae's problem:

# I want to bake a cake for my friend's birthday. I found this API with lots of recipes, and I want to find a recipe for a cake with nutella in it. However, my friend is allergic to eggs, so I can't use any recipes that include eggs.

# Please find recipes (and their URLs) of cakes that won't make my friend sick!

# more info about the api is at http://www.recipepuppy.com/about/api/

url = 'http://www.recipepuppy.com/api/'

parameters = {"i": "nutella", "q" : "cake", } #from Kae

resp = requests.get(url, parameters)

resp

data = resp.json()

recipes = pd.DataFrame(data['results'], columns=['title', 'ingredients', 'href'])

recipes.head()

# now I need to filter...

recipes[[not bool(re.search('egg', i)) for i in recipes.ingredients]]
# but this only gets us the first page of recipes...

blank = False

url = 'http://www.recipepuppy.com/api/'

page = 1
recipes = pd.DataFrame(columns=['title', 'ingredients', 'href'])

while True:
    parameters = {"i": "nutella", "q": "cake", "p": page } #from Kae
    resp = requests.get(url, parameters)
    data = resp.json()
    if len(data['results']) == 0:
        break
    recipes = recipes.append(
        pd.DataFrame(
            data['results'], columns=['title', 'ingredients', 'href']))
    page += 1

len(recipes)

recipes[[not bool(re.search('egg', i)) for i in recipes.ingredients]]


### John's problem:

# We are going to being looking at NFL player stats for the 2018 season

# Using the information provided here create the proper url to use with
# requests.get(url) to get the overall stats for each player for the season.

# Process the JSON of the response and create a pandas data frame with columns 
# for each player's name, position, team, and season points

# Find the top five quarterbacks this season based on points

url = 'http://api.fantasy.nfl.com/v1/players/stats'

parameters = {'position': 'QB'}

response = requests.get(url, parameters)

data = response.json()

data.items()

stats = pd.DataFrame(data['players'], columns=['name', 'teamAbbr', 'position', 'seasonPts'])


stats.sort_values('seasonPts', ascending=False).head()
