## 3.1

### Tuple.  A fixed-length, immutable sequence of Python objects.

tup = 4, 5, 6

tup

# a tuple of tuples

nested_tup = (4, 5, 6), (7, 8)

nested_tup

# can also use the tuple function to convert

tuple([4, 0 ,2])

tup = tuple('string')

tup

#use square brackets to accesss elements

tup[1]

# cannot change

tup[1] = 'a'

# ahh but if the tuple contains a mutable object that object can be changed

tup = tuple(['foo', [1, 2], True])

tup[1].append(3)

tup

# can concatenate with the '+' sign

tup + (4, 5, 6)

# can repeat with the * sign

tup * 5

# unpack: assigning to a tuple-like expression of variables, then python will
# unpack

tup = (4, 5, 6)

a, b, c = tup

a
b
c

# use this to swap variables

b, a = a, b

b
a

### can iterate over sequences....

seq = [(1, 2, 3), (4, 5, 6), (7, 8, 9)]

for a, b, c in seq:
   print('a={0}, b={1}, c={2}'.format(a, b, c))

values = 1, 2, 3, 4, 5

a, b, *rest = values

a, b

rest

a = (1, 2, 2, 2, 3, 4, 2)

a.count(1)

a.count(2)

a.index(2)

a.index(1)

a.index(3)


## LIST

# Lists are variable length and mutable
# Defined with square brackets, or using the list() function

a_list = [2, 3, 7, None]

tup = ('foo', 'bar', 'baz')

b_list = list(tup)

b_list

gen = range(10)

gen

list(gen)

# use append() to add to the end

b_list.append("dwarf")

b_list

# use insert() to insert a particular position.

b_list.insert(1, "red")

b_list

b_list.pop() # with no arguemnt, pops that last item in the list

b_list.pop(2) 

b_list

'foo' in b_list

'bar' not in b_list

# but this is slow relative to checking in dicts and sets

# extend , or use "+" to add items to the end of a list.  extend is faster.

b_list.extend(([4,5,6]))

b_list

# use sort() to sort in place

a = [7, 2, 5, 1, 3]

a.sort()

a

b = ['saw', 'small', 'He', 'foxes', 'six']

b.sort(key=len)

b

# if you have a sorted list, then you can insert things into the correct place with bisect

import bisect

bisect.bisect(a, 4)  # returns the position where 4 should go

bisect.insort(a, 4)  # actually places it

a

# slicing

seq = [7, 2, 3, 7, 5, 6, 0, 1]

seq[1:5]

# can assign to slice

seq[3:4] = [6,3]  # note" element at the start is included, but the element at the end is not

seq

seq[4:4] = [10,11]

seq

# negative indicies indicates index relative to end

seq[-2:]

seq[-4:-3]

# step after second colon

seq[::3]  # take every 3rd

## built-in sequence functions

# enumerate().  returns a sequence of index, value tuples from a list

some_list = ['foo', 'bar', 'baz']

mapping = {}

for i, v in enumerate(some_list):
   mapping[v] = i

mapping

# use sorted to returne a new sorted list from a sequence

sorted(some_list)

# zip zips up sequences by pairing them

seq1 = ['foo', 'bar', 'baz']
seq2 = ['one', 'two', 'three']
zipped = zip(seq1, seq2)

list(zipped)

# reversed reverses the list

list(reversed(some_list))

## dict.  perhaps the most important data structure
## it is a hash table, or a set of key: value pairs

d1 = {'a' : 'some value', 'b' : [1, 2, 3, 4]}

d1

d1['b']

d1[7] = 'an integer'

d1

7 in d1 # checking for key, not value

# use del or pop to delete an element, based on its key
d1[5] = 'some value'

d1['dummy'] = 'another value'

d1

del d1[5]

d1

list(d1.keys())

list(d1.values())

d1.update({'b' : 'foo', 'c' : 12, 'julin' : 13})
#pre-existing values overwritten
d1

#note that most immutable objects can be keys, so tuples can be keys(!)

## sets
# a set is like the key part of a dict.  It is an unordered collection of unique elements
# create with set() function or with curly brackets

set([2, 2, 2, 1, 3, 3])

{2, 2, 2, 1, 3, 3}

a = set(range(1,6))

a

b = set(range(3,9))

b

a.union(b)

b.union(a)

a | b 

a.intersection(b)

a & b

# plus many methods...

## comprehensions
# form a new list by filtering elements of a collection.

[x*x for x in b if x > 3]

## functions

# variables defined within the function are local to the function
# unless the global keyword is used (this is discouraged)
# functions can access and modify global variables.

# can return multiple values (they will be returned as a tuple)

# functions are objects, so you can create a list of them and iterate over them.

# lambda keyword defines autonomous functions


def apply_to_list(some_list, f):
    return [f(x) for x in some_list]


ints = [4, 0, 1, 5, 6]
apply_to_list(ints, lambda x: x * 2)

# generators: functions that create an iterable.  Use `yield` instead of `return` in a function
# or use a generator expression.  Like a comprehension, but used curved instead of square brackets

# itertools has useful functions

import itertools

first_letter = lambda x: x[0]

names = ['Alan', 'Adam', 'Wes', 'Will', 'Albert', 'Steven']


for letter, grouped_names in itertools.groupby(names, first_letter):
    print(letter, list(grouped_names)) # grouped_names is a generator

# note that A comes up twice, so need to sort?

for letter, grouped_names in itertools.groupby(sorted(names), first_letter):
    print(letter, list(grouped_names)) # names is a generator

a = list(range(0,3))

a    

#preserved order
list(itertools.combinations(a, 3))
list(itertools.combinations(a, 2))

list(itertools.permutations(a, 3))

list(itertools.product('abc',a))

## exceptions
# so much better than R!

def attempt_float(x):
    try:
        return float(x)
    except ValueError:
        return x

attempt_float('123')        

attempt_float('test')

attempt_float((1,2,3))

## files

path = 'examples/segismundo.txt'

f = open(path)

for line in f:
    print(line)

lines = [x.rstrip() for x in open(path)]    

lines

f.close()

