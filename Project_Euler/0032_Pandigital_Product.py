'''
We shall say that an n-digit number is pandigital if it makes use of all the digits 1 to n
exactly once; for example, the 5-digit number, 15234, is 1 through 5 pandigital.

The product 7254 is unusual, as the identity, 39 × 186 = 7254, containing multiplicand,
multiplier, and product is 1 through 9 pandigital.

Find the sum of all products whose multiplicand/multiplier/product identity can be written
as a 1 through 9 pandigital.

HINT: Some products can be obtained in more than one way so be sure to only include it once
in your sum.


'''

from collections import Counter

def find_sum_of_pandigitals():
    vals = Counter('123456789')
    pandigitals = set()
    for i in range(100):
        for j in range(i + 1, 10000):
            curr = i * j
            characters = str(i) + str(j) + str(curr)
            to_check = Counter(characters)
            if vals == to_check:
                pandigitals.add(curr)
    return sum(pandigitals)


# Optimized
# Only need to check multiplicands 1-99 and multipliers up to 9999
# Since 100 * 100 = 10000 which would be too many digits

def optimized_pandigital_sum():
    pandigitals = set()

    for i in range(1, 100):
        # j starts from 100//i to avoid duplicate products
        start = max(i + 1, 1000 // i)
        for j in range(start, 10000 // i + 1):
            prod = i * j
            digits = f"{i}{j}{prod}"
            if len(digits) == 9 and set(digits) == set('123456789'):
                pandigitals.add(prod)
    return sum(pandigitals)

print(optimized_pandigital_sum())