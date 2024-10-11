'''
The sum of the primes below 10
is 2 + 3 + 5 + 7 = 17


Find the sum of all the primes below two million.
'''
import math


def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True
n = 1
total = sum([n for n in range(2000000) if is_prime(n)])


