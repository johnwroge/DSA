'''
145 is a curious number, as 1! + 4! + 5! = 1 + 24 + 120 = 145.

Find the sum of all numbers which are equal to the sum of the factorial of their digits.

Note: as 1! = 1 and 2! = 2 are not sums they are not included.
'''

import time
import math
from functools import lru_cache

def solution1():
    values = []
    @lru_cache(maxsize=None) 
    def myfact(x):
        return math.factorial(x)
    for i in range(3, 1000000):
        string = list(str(i))
        total = sum(map(myfact, [int(c) for c in string]))
        if total == i:
            values.append(total)
    return sum(values)

def fastest_solution():
    # Precompute factorials for 0-9 in a tuple (immutable, faster lookups)
    facts = (1, 1, 2, 6, 24, 120, 720, 5040, 40320, 362880)
    
    # Find upper limit: A number with d digits can't be larger than d * 9!
    # For any number > 7 digits, sum of factorials will be smaller than number itself
    # 7 * 9! = 2,540,160 is our theoretical upper bound
    upper = 2540160
    
    # We can further optimize by starting at 3 (since 1! and 2! aren't sums)
    result = 0
    
    # Main loop with optimizations
    for num in range(3, upper):
        total = 0
        n = num
        
        # Use modulo/division instead of string conversion
        # This is faster than string operations
        while n:
            total += facts[n % 10]
            if total > num:  # Early exit if sum exceeds number
                break
            n //= 10
            
        if total == num:
            result += num
            
    return result


# Time solution1
start = time.time()
result1 = solution1()
time1 = time.time() - start

# Time solution2
start = time.time()
result2 = fastest_solution()
time2 = time.time() - start

print(f"Solution 1: {time1:.4f} seconds")
print(f"Solution 2: {time2:.4f} seconds")



# only 4 exist: 1, 2, 145 & 40585 but we exclude 1 and 2. 