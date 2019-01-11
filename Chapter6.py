# notes on chapter 6 python data analysis

import pandas as pd
import numpy as np

# 6.1 Reading and wrting data in text format

# first get unix to print file content

!cat examples/ex1.csv

df = pd.read_csv("examples/ex1.csv")

df

# what if no header?

!cat examples/ex2.csv

# use default header names

pd.read_csv("examples/ex2.csv", header=None)

# sepcify which column in index

names = ['a', 'b', 'c', 'd', 'message']

pd.read_csv("examples/ex2.csv", names=names, index_col='message')


# can use hierarchical index from multiple columns:

!cat examples/csv_mindex.csv

parsed = pd.read_csv("examples/csv_mindex.csv", index_col=['key1', 'key2'])

parsed

list(open('examples/ex3.txt'))

!cat examples/ex3.txt

result = pd.read_csv('examples/ex3.txt', sep='\s+')

result

!cat examples/ex4.csv

pd.read_csv('examples/ex4.csv', skiprows=[0, 2, 3])

#Or

pd.read_csv("examples/ex4.csv", comment="#")


## Reading text filesin pieces

### show only a few rows:

pd.options.display.max_rows = 10

pd.read_csv('examples/ex6.csv')
### read only a few rows:

pd.read_csv('examples/ex6.csv', nrows=5)

### read in chunks

# first make a chunker

chunker = pd.read_csv('examples/ex6.csv', chunksize=1000)

chunker

tot = pd.Series([])
for piece in chunker:
    tot = tot.add(piece['key'].value_counts(), fill_value=0)

tot = tot.sort_values(ascending=False)

tot

# This sums up the numberof occurences of each key, one chunk at a time

## Writing Data to Text format

# first get some data

data = pd.read_csv('examples/ex5.csv')

data

data.to_csv("examples/out.csv")

!cat examples/out.csv

## shortcut to see what is being written without creating a file

import sys

# use different separator

data.to_csv(sys.stdout, sep="!")

# specify NA value

data.to_csv(sys.stdout, na_rep="MISSING!")


data.to_csv(sys.stdout, index=False, header=False)
data.to_csv(sys.stdout, index=False, columns=['a', 'b', 'c'])

## working with delimited formats

!cat examples/ex7.csv

pd.read_csv("examples/ex7.csv")

## can also use builtin csv reader

import csv

f = open('examples/ex7.csv')

reader = csv.reader(f)

for line in reader:
    print(line)

with open("examples/ex7.csv") as f:
    lines = list(csv.reader(f))

header, values = lines[0], lines[1:]

header

values    

data_dict = {h: v for h, v in zip(header, zip(*values))}

data_dict

## JSON Data

import json

obj = """
    {"name": "Wes",
     "places_lived": ["United States", "Spain", "Germany"],
     "pet": null,
     "siblings": [{"name": "Scott", "age": 30, "pets": ["Zeus", "Zuko"]},
                  {"name": "Katie", "age": 38,
                   "pets": ["Sixes", "Stache", "Cisco"]}]
    }
"""
result = json.loads(obj)

result

asjson = json.dumps(result)

asjson
siblings = pd.DataFrame(result['siblings'], columns=['name', 'age'])

siblings

siblings = pd.DataFrame(result['siblings'], columns=['name', 'age', 'pets'])

siblings

# also a pandas function

!cat examples/example.json

data = pd.read_json('examples/example.json')

data

## XML and HTML: Web Scraping

tables = pd.read_html('examples/fdic_failed_bank_list.html')

len(tables)

failures = tables[0]

failures.head()



from lxml import objectify

path = 'datasets/mta_perf/Performance_MNR.xml'
parsed = objectify.parse(open(path))
root = parsed.getroot()

data = []

skip_fields = ['PARENT_SEQ', 'INDICATOR_SEQ',
               'DESIRED_CHANGE', 'DECIMAL_PLACES']

for elt in root.INDICATOR:
    el_data = {}
    for child in elt.getchildren():
        if child.tag in skip_fields:
            continue
        el_data[child.tag] = child.pyval
    data.append(el_data)
    
perf = pd.DataFrame(data)

perf.head()
