import requests

import pandas as pd

url = "https://api.weather.gov/points/38.5449%2C-121.7405/forecast"

resp = requests.get(url)

data = resp.json()

weather = pd.DataFrame(data['properties']['periods'], columns=['name', 'temperature', 'windSpeed', 'windDirection', 'detailedForecast'])

weather
