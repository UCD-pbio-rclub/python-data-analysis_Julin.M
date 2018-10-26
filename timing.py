import time

a = 0  # will be used in my loop

t1 = time.process_time() # get the current time

for i in range(0,10000000):  # a statement to test
    a = a  + 1
    
elapsed = time.process_time() - t1 

print(' the process took {0:.3f} seconds'.format(elapsed))
# alternative, using timeit

import timeit 

# note timeit runs the statement 1,000,000 times by default, so 
# I use a shorter loop

stmt = """\
for i in range(0,100):  # a statement to test
    a = a  + 1
"""

timeit.timeit(stmt, setup='a = 0')

