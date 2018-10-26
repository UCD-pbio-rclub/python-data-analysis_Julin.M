# Chapter 2.3 Python language basics

a = [1, 2, 3, 4]

a

b = a

b

b.append(10)

b

a

c = list(a)

c

c.append(20)

c

a

d = list(a)

a

b

d   

a is b

a is d 

a == b

a == d 

iter(5)

# wow!

def append_element(some_list, element):
    some_list.append(element)
    
data = [1, 2, 3]    

output = append_element(data, 4)

data

output

## but this seems to contradict the statement in the book "If you bing a new object to a variable inside a function that change will not be reflected in the parent scope"

a = 4.5

b = 2

print('a is {0}, b is {1}'.format(type(a), type(b)))

a / b

a = 5

isinstance(a, int)

a = 'foo'

#a.

def isiterable(obj):
    try:
        iter(obj)
        return True
    except TypeError: # not iterable
        return False
        
isiterable('a string')

isiterable([1, 2, 3])

isiterable(5)

import some_module
result = some_module.f(5)
pi = some_module.PI

result

a = [1, 2, 3]

b = a

c = list(a)

a is b 
a is c
a == c

b.append(4)

b is a

a_list = ['foo', 2, [4, 5]] 

a_list[2] = (3, 4) # what is the difference between square and rounded brackets?
                   # list vs tuple

a_list

a_tuple = (3, 5, (4, 5))

a_tuple[1] = 'four'

## scalar types

# scalars are types that handle single values of data

