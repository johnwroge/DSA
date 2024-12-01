'''
The number 197 is called a circular prime because all rotations of the digits:
197, 971, and 719, are themselves prime.

There are thirteen such primes below 100: 2, 3, 5, 7, 11, 13, 17, 31, 37, 71, 73, 79, and 97.

How many circular primes are there below one million?
'''


import time

def solution():
    results = []
    def is_prime(n):
        if n < 2:
            return False
        for i in range(2, int(n**0.5) + 1):
            if n % i == 0:
                return False
        return True
    prime_set = set()
    for i in range(2, 1000001):
        if is_prime(i):
            prime_set.add(i)
    for i in range(2, 1000001):
        if i != 2 and i % 2 == 0:
            continue
        num_string = str(i)
        num_rotations = []
        for i in range(len(num_string)):
            num_rotations.append(int(num_string[i:] + num_string[:i]))
        if all(num in prime_set for num in num_rotations):
            results.append(num_string)
    return len(results)

def optimized_solution():
    def is_prime(n):
        if n < 2:
            return False
        if n == 2:
            return True
        if n % 2 == 0:
            return False
        for i in range(3, int(n**0.5) + 1, 2):
            if n % i == 0:
                return False
        return True
    
    def get_rotations(n):
        s = str(n)
        # Single digit numbers don't need digit checking
        if len(s) > 1 and any(d in '024568' for d in s):
            return []
            
        rotations = []
        for i in range(len(s)):
            rotations.append(int(s[i:] + s[:i]))
        return rotations
    
    # Start with 2
    count = 1
    
    # Handle single digit numbers first (2,3,5,7)
    for n in [3,5,7]:
        if is_prime(n):
            count += 1
    
    # Then check larger numbers
    for n in range(11, 1000000, 2):
        if is_prime(n):
            rotations = get_rotations(n)
            if rotations and all(is_prime(r) for r in rotations):
                count += 1
                
    return count

start = time.time()
result1 = solution()
time1 = time.time() - start

# Time solution2
start = time.time()
result2 = optimized_solution()
time2 = time.time() - start

print(f"Solution 1: {time1:.4f} seconds")
print(f"Solution 2: {time2:.4f} seconds")
        
    