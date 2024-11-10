'''
Problem 23: Non-Abundant Sums

A perfect number is a number for which the sum of its proper divisors is exactly equal to the number. 
For example, the sum of the proper divisors of 28 would be 1 + 2 + 4 + 7 + 14 = 28, which means that 28 
is a perfect number.

A number n is called deficient if the sum of its proper divisors is less than n and it is called abundant
if this sum exceeds n.

As 12 is the smallest abundant number, 1 + 2 + 3 + 4 + 6 = 16, the smallest number that can be written as the sum of two abundant
numbers is 24. By mathematical analysis, it can be shown that all integers greater than 28123 can be written
as the sum of two abundant numbers. However, this upper limit cannot be reduced any further by analysis 
even though it is known that the greatest number that cannot be expressed as the sum of two abundant numbers
is less than this limit.

Find the sum of all the positive integers which cannot be written as the sum of two abundant numbers.
'''


'''
how to find numbers that cannot be written as the sum of two abundant numbers

A number n is called deficient if the sum of its proper divisors is less than n and it is called abundant
if this sum exceeds n.

numbers within 1 - 28123

brute force

for each number
    # find all numbers that divide evenly with it, 
    # add those together, 
    # check if they are greater than the number
        # if yes store in a set, this is a set of abundant numbers

find all possible sums between each pair of numbers, store in a hash or set

iterate from 1 to 28123
    if number is in set
        continue
    otherwise
        add to list
        
return the final list

'''


def sum_of_divisors(n):
    total = 0
    for i in range(1, (n // 2) + 1):
        if n % i == 0:
            total += i
    return total    

def find_all_abundant_numbers_in_range(start, stop):
    store = []
    for n in range(start, stop):
        if sum_of_divisors(n) > n:
            store.append(n)
    return store

def find_all_sums_of_abundant_numbers(abundant):
    all_abundant_sums = set()
    for i in range(len(abundant)):
        for j in range(i, len(abundant)):
            target = abundant[i] + abundant[j]
            if target < 28124:
                all_abundant_sums.add(target)
    return all_abundant_sums

def find_answer():
    store = find_all_abundant_numbers_in_range(1, 28123)
    all_sums = find_all_sums_of_abundant_numbers(store)
    answer = []
    for i in range(1, 28124):
        if i not in all_sums:
            answer.append(i)
    return sum(answer)


print(find_answer())








# find all possible sums between each pair of numbers, store in a hash or set

# iterate from 1 to 28123
#     if number is in set
#         continue
#     otherwise
#         add to list
        
# return the final list
