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

## 6.2 binary data formats

### pickle

#Can use python's built in _pickle_ format to store in an efficient binary format.  But don't use this for long term storage.

frame = pd.read_csv("examples/ex1.csv")

frame

frame.to_pickle("examples/ex1.pkl")

pd.read_pickle("examples/ex1.pkl")

### Other options

# other options include HDF5 (below) and feather (Cross compatible with R!) and a few others...

# HDF5 allos accessing subsets of the data on the fly and is fast

frame = pd.DataFrame({'a': np.random.randn(100)})

frame.head

store = pd.HDFStore('mydata.h5')

store['obj1'] = frame

store

store['obj1']
store['obj1_col'] = frame['a']

store
store.keys()

# why does he have us do both?

store['obj1_col']

# can store as fixed or table.  Table is slower but allows querries with convenient syntax.

store.put('obj2', frame, format='table')

store.select('obj2', where=['index >= 10 and index <= 15'])

store.close()

# pandas has tools to shortcut these operations

frame.to_hdf('mydata.h5', 'obj3', format='table')
# built in to frame methods

pd.read_hdf('mydata.h5', 'obj3', where=['index < 5'])

### reading excel files

xlsx = pd.ExcelFile('examples/ex1.xlsx')

xlsx

# then parse it

pd.read_excel(xlsx, 'Sheet1')

# or use read_excel directly:

pd.read_excel("examples/ex1.xlsx", "Sheet1")

# to write, first create a writer

writer = pd.ExcelWriter('examples/ex2.xlsx')

# then write to it

frame.to_excel(writer, "Sheet1")

writer.save()

# or maybe writer is not needed?

frame.to_excel("examples.ex2a.xlsx")

# so why create a writer??

## 6.3 Web APIs

import requests

url = 'https://api.github.com/repos/pandas-dev/pandas/issues'

resp = requests.get(url)

data = resp.json() # the contents of resp parsed as json

data[0]['title']

issues = pd.DataFrame(data, columns=['number', 'title', 'labels', 'state'])

issues

## 6.4.  Interacting with databases

#note John says we should use mysql
# import mysql.connector

import sqlite3

query = "CREATE TABLE test (a VARCHAR(20), b VARCHAR(20), c REAL, d INTEGER);"

con = sqlite3.connect('mydata.sqlite')

con.execute(query)

con.commit()

data = [('Atlanta', 'Georgia', 1.25, 6),
    ('Tallahassee', 'Florida', 2.6, 3),
    ('Sacramento', 'California', 1.7, 5)]

stmt = "INSERT INTO test VALUES(?, ?, ?, ?)"

con.executemany(stmt, data)

con.commit()

cursor = con.execute('select * from test')

cursor

cursor.rowcount

cursor.lastrowid

cursor.description

rows = cursor.fetchall()

rows
pd.DataFrame(rows, columns=[x[0] for x in cursor.description])

import sqlalchemy as sqla

db = sqla.create_engine('sqlite:///mydata.sqlite')

pd.read_sql('select * from test', db)
