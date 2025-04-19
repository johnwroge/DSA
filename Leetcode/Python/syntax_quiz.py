'''
Quiz for syntax
'''

import collections
import heapq
import math
thing = [1,2,3]
list2 = [2,3,5,1,0,2,22]

# what is the difference between a tuple, list and object? 

# add an element to a specific index in an array

list2.insert(0,22)


# read from a file

with open('filename.txt', 'r') as file:
    lines = file.readlines()
    print(lines)

# append to a file

with open('filename.txt', 'a') as file:
    line = 'hi world'
    file.write(line)


# append item to list
list2.append(2)

# remove item from list

list2.remove(2)
# remove item at index
index = 2
list2.pop(index)


# find index of 1st occurence
list2.index(2)

# find count of number of times item appears
print(list2.count(3))

# sort a list
list2.sort()

# sort a list in reversed order
list2.sort(key=lambda x: x, reverse=True)

# reverse a list and return new list
new_list = list(reversed(list2))
# print(new_list)

# create a new list of list1 and list 2
list3 = list2 + list2

# modify list 1 to contain items from list2
list2.extend(list2)

# remove all elements from a list
list2.clear()

''' Are strings mutable in python? '''
# No, you need to create copies of strings to mutate,
# converting to a list is oftentimes easier

# reverse a string using a list***
s = 'abc'
t = ''.join(list(reversed(s)))

# reverse a string using slices***
t2 = s[::-1]

# change number to string
number = 100
str(number)

# change string to lowercase'
string = 'HELLO'
string.lower()

# change string to uppercase
string.upper()

'What about upper or lowercase for matching?'


# replace parts of string with new 

string.replace('something','newwords')

# split a string by a separator
s.split(' ')
# split a string in a list of characters
list(s)
# remove white space from string
thing = '  a  b  c'
thing2 = 'def'
# concatenate two string use literal syntax
f"{thing}{thing2}"
# concatenate two strings use operator
thing + thing2

# create an adjacency list using a library with both a list and a set 

adjList = collections.defaultdict(list)
adjList2 = collections.defaultdict(set)

'''what is the difference in time and space complexity for operations in a list and a set?'''

# create an adjacency list using dictionary comprehension
edges = [[1,3],[3,4],[5,6],[8,9]]

adjList = {x:[y] for x,y in edges}

# create a deque

deque = collections.deque()

# add a number to the left part of deque
deque.appendleft('thing')

# pop an element from the left part of deque
deque.popleft()

# create an object for counting items 

# create a counter of an object

# rotate a list by k 


# create new list of 2d array sorted by 1st element

# create new list of 2d array sorted by 1st element in reverse

# sort 2d array sorted by 1st element in place

# create a new list of tuples

# create a new dictionary from list of tuples

# What happens if you have a duplicate key?

# get dictionaries keys

# get dic values

# get dict view object

# remove item at particular key and return its value
new_obj = {1:2, 3:4, 5:6}
new_obj2 = {1: 3, 6:7, 8:9, 9:10}
# remove all items from dictionary

# get a particular value at a key

# change dictionary key value with one from another 

# remove a value

'''
Heaps
'''

# create a minimum heap from a list of numbers
list1 = [2,3,5,6]
heapq.heapify(list1)

# create a maximum heap from list of numbers

'''
Sets
'''

# create a set 

# convert a list of numbers to a set

# set operations:

# union |


# intersection & or intersection()

# difference - or difference()

# symmetric difference

# subset <= issubset()

# superset >= issuperset()



'''Map, Filter, Reduce'''

# Example list
numbers = [1, 2, 3, 4, 5, 6]

# Using filter to get even numbers
# filter() filters elements that satisfy a condition (lambda)
# filter(function, iterable)
even_numbers = list(filter(lambda x: x % 2 == 0, numbers))
# print(even_numbers)  # Output: [2, 4, 6]

# Using map to square each number
# map() applies a function to all elements of an iterable
# map(function, iterable)
squared_numbers = list(map(lambda x: x ** 2, numbers))
# print(squared_numbers)  # Output: [1, 4, 9, 16, 25, 36]

# Using reduce to sum all elements in the list
# reduce() applies a function cumulatively to the items, reducing them to a single value
from functools import reduce
# reduce(function, iterable)
total_sum = reduce(lambda x, y: x + y, numbers)
# print(total_sum)  # Output: 21

# Combining filter, map, and reduce
# Example: Find the sum of the squares of even numbers
even_squared_sum = reduce(lambda x, y: x + y, map(lambda x: x ** 2, filter(lambda x: x % 2 == 0, numbers)))
# print(even_squared_sum)  # Output: 56



# create new array of length n filled with 0


# convert string in binary to number (remember what to include?)
bin_string = '1010101010'
num = int(bin_string, 2)


# find the intersection of 2 sets

# set1.intersection(set2)


# Math 

n = 536870912

# take the logarithm of a number

# base e
math.log(x)
# base 10
math.log10(x, 10)
# base 2
math.log2(x)


# use built in log 2 function to find log2 of number

# check to see if number is an integer


# take the product of a list of numbers
arr = [1,2,3,4,5,6,7,8,9,10]
# import math
# p = math.prod(arr)


# rotate a 2d grid by 90degrees
# https://stackoverflow.com/questions/8421337/rotating-a-two-dimensional-array-in-python

rotated = list(zip(*original[::-1]))

# https://stackoverflow.com/questions/41290350/inplace-rotation-of-a-matrix

# what is the difference between a tuple, list and object? 

'''
tuple is immutable and read only, list and dict/object are mutable
'''

# iterate over key val pairs in dictionary and return a list of these



# create a list of tuples of the rows of a graph

# iterate over the columns of a graph using unpacking operator
grid = [[3,1,2,2],[1,4,4,5],[2,4,2,2],[2,4,2,2]]

for tpl in zip(*grid):
    print(tpl)

# use built in binary search to determine index position in iterable

import bisect 
nums5 = [1,3,5,7,9]

# print(bisect.bisect(nums5, 6))


# Bit

# Format a number to be a 32 bit integer with 0's

n = format(n, '032b')

