'''
Longest Collatz Sequence

The following iterative sequence is defined for the set of positive integers:

n -> n/2 (n is even)
n -> 3n + 1 (n is odd)

Using the above rule and starting with 13 we generate the following sequence

13 -> 40 -> 20 -> 10 -> 5 -> 16 -> 8 -> 4 -> 2 -> 1

It can be seen that this sequence (starting at 13 and finishing at 1) contains 10 terms.
Although it has not been proved yet (Collatz Problem), it is thought that all starting numbers finish at 1.

Which starting number, under one million, produces the longest chain?

NOTE: Once the chain starts the terms are allowed to go above one million.

'''

'''
solution: use memoization to keep track of precomputed values. iterating from 1 to 1,000,000
keep track of the length of sequences to get to 1 from the current number and store it in a cache.
If we reach a precomputed value from the current number, then add that cached length to the current length.

''' 

solutions = {}
key = 0
max_length = 0

for i in range(1,1000000):
    length = 0
    current = i
    while current != 1:
        length += 1
        if current in solutions:
            length += solutions.get(current)
            break
        elif current % 2 == 0:
            current //= 2
        else:
            current = 3 * current + 1
    solutions[i] = length
    if length > max_length:
        max_length = length
        key = i

print('Longest chain number is', key, 'with a max length of', max_length)

