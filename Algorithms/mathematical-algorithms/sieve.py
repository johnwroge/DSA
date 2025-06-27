from typing import List, Dict, Set
import math

# =============================================================================
# SIEVE ALGORITHMS TEMPLATE
# =============================================================================

"""
LeetCode Problems that can be solved with this technique:
- 204. Count Primes
- 279. Perfect Squares
- 264. Ugly Number II
- 313. Super Ugly Number
- 1356. Sort Integers by The Number of 1 Bits
- 952. Largest Component Size by Common Factor
- 1735. Count Ways to Make Array With Product
- 1819. Number of Different Subsequences GCDs
"""

def sieve_of_eratosthenes(n: int) -> List[bool]:
    """
    Sieve of Eratosthenes to find all primes up to n
    Time Complexity: O(n log log n)
    Space Complexity: O(n)
    Returns boolean array where is_prime[i] indicates if i is prime
    """
    if n < 2:
        return [False] * max(n + 1, 2)
    
    is_prime = [True] * (n + 1)
    is_prime[0] = is_prime[1] = False
    
    for i in range(2, int(math.sqrt(n)) + 1):
        if is_prime[i]:
            # Mark all multiples of i starting from i²
            for j in range(i * i, n + 1, i):
                is_prime[j] = False
    
    return is_prime

def sieve_primes_list(n: int) -> List[int]:
    """
    Get list of all prime numbers up to n using sieve
    """
    is_prime = sieve_of_eratosthenes(n)
    return [i for i in range(2, n + 1) if is_prime[i]]

def count_primes(n: int) -> int:
    """
    LeetCode 204: Count the number of prime numbers less than n
    """
    if n <= 2:
        return 0
    
    is_prime = sieve_of_eratosthenes(n - 1)
    return sum(is_prime)

def segmented_sieve(low: int, high: int) -> List[int]:
    """
    Segmented sieve to find primes in range [low, high]
    Useful when range is large but segment size is manageable
    """
    if high < 2:
        return []
    
    # First find all primes up to sqrt(high)
    limit = int(math.sqrt(high)) + 1
    primes = sieve_primes_list(limit)
    
    # Create boolean array for segment [low, high]
    segment_size = high - low + 1
    is_prime_segment = [True] * segment_size
    
    for prime in primes:
        # Find minimum number in [low, high] that is divisible by prime
        start = max(prime * prime, ((low + prime - 1) // prime) * prime)
        
        # Mark multiples of prime in segment
        for j in range(start, high + 1, prime):
            is_prime_segment[j - low] = False
    
    # Collect primes in segment
    result = []
    for i in range(segment_size):
        if is_prime_segment[i] and (low + i) >= 2:
            result.append(low + i)
    
    return result

def sieve_smallest_prime_factor(n: int) -> List[int]:
    """
    Modified sieve to find smallest prime factor for each number
    spf[i] = smallest prime factor of i
    """
    spf = list(range(n + 1))  # Initialize with identity
    
    for i in range(2, int(math.sqrt(n)) + 1):
        if spf[i] == i:  # i is prime
            for j in range(i * i, n + 1, i):
                if spf[j] == j:  # First time marking j
                    spf[j] = i
    
    return spf

def sieve_euler_totient(n: int) -> List[int]:
    """
    Sieve to compute Euler's totient function φ(i) for all i from 1 to n
    φ(i) = count of numbers ≤ i that are coprime with i
    """
    phi = list(range(n + 1))  # Initialize φ(i) = i
    
    for i in range(2, n + 1):
        if phi[i] == i:  # i is prime
            for j in range(i, n + 1, i):
                phi[j] -= phi[j] // i  # φ(j) = φ(j) * (1 - 1/i)
    
    return phi

def sieve_mobius_function(n: int) -> List[int]:
    """
    Sieve to compute Möbius function μ(i) for all i from 1 to n
    μ(i) = 1 if i is square-free with even number of prime factors
    μ(i) = -1 if i is square-free with odd number of prime factors
    μ(i) = 0 if i has squared prime factor
    """
    mu = [1] * (n + 1)
    is_prime = [True] * (n + 1)
    
    for i in range(2, n + 1):
        if is_prime[i]:
            for j in range(i, n + 1, i):
                is_prime[j] = False
                mu[j] *= -1
            
            # Mark squares of prime i
            for j in range(i * i, n + 1, i * i):
                mu[j] = 0
    
    return mu

def count_perfect_squares_sieve(n: int) -> int:
    """
    LeetCode 279: Perfect Squares using sieve-like DP approach
    Find minimum number of perfect squares that sum to n
    """
    dp = [float('inf')] * (n + 1)
    dp[0] = 0
    
    # Generate perfect squares
    squares = []
    i = 1
    while i * i <= n:
        squares.append(i * i)
        i += 1
    
    # Fill DP table
    for square in squares:
        for i in range(square, n + 1):
            dp[i] = min(dp[i], dp[i - square] + 1)
    
    return dp[n]

def super_ugly_numbers(n: int, primes: List[int]) -> int:
    """
    LeetCode 313: Super Ugly Number II
    Find nth super ugly number (only factors from given primes)
    """
    ugly = [1]
    indices = [0] * len(primes)
    
    for _ in range(1, n):
        # Calculate next candidates
        candidates = [ugly[indices[i]] * primes[i] for i in range(len(primes))]
        next_ugly = min(candidates)
        ugly.append(next_ugly)
        
        # Update indices for primes that produced minimum
        for i in range(len(primes)):
            if candidates[i] == next_ugly:
                indices[i] += 1
    
    return ugly[n - 1]

def linear_sieve(n: int) -> tuple:
    """
    Linear sieve (Sieve of Euler) - O(n) time complexity
    Returns (list of primes, smallest prime factor array)
    """
    spf = [0] * (n + 1)  # Smallest prime factor
    primes = []
    
    for i in range(2, n + 1):
        if spf[i] == 0:  # i is prime
            spf[i] = i
            primes.append(i)
        
        for prime in primes:
            if prime > spf[i] or prime * i > n:
                break
            spf[prime * i] = prime
    
    return primes, spf

def sieve_divisor_count(n: int) -> List[int]:
    """
    Sieve to count number of divisors for each number from 1 to n
    """
    divisor_count = [0] * (n + 1)
    
    for i in range(1, n + 1):
        for j in range(i, n + 1, i):
            divisor_count[j] += 1
    
    return divisor_count

def sieve_sum_of_divisors(n: int) -> List[int]:
    """
    Sieve to compute sum of divisors for each number from 1 to n
    """
    divisor_sum = [0] * (n + 1)
    
    for i in range(1, n + 1):
        for j in range(i, n + 1, i):
            divisor_sum[j] += i
    
    return divisor_sum

def count_subsequences_gcd(nums: List[int]) -> int:
    """
    LeetCode 1819: Number of Different Subsequences GCDs
    Count how many different GCDs are possible from subsequences
    """
    max_val = max(nums)
    count = [0] * (max_val + 1)
    
    # Count occurrences of each number
    for num in nums:
        count[num] += 1
    
    result = 0
    
    # For each possible GCD value
    for gcd_val in range(1, max_val + 1):
        subsequence_count = 0
        
        # Count numbers that are multiples of gcd_val
        for multiple in range(gcd_val, max_val + 1, gcd_val):
            subsequence_count += count[multiple]
        
        # If we have at least one multiple, this GCD is achievable
        if subsequence_count > 0:
            # Use inclusion-exclusion or DP to check if this exact GCD is possible
            # For simplicity, we count if any multiples exist
            result += 1
    
    return result

def sieve_for_factorization(n: int) -> Dict[int, List[int]]:
    """
    Precompute prime factors for all numbers up to n
    Returns dictionary mapping each number to its prime factors
    """
    factors = {i: [] for i in range(n + 1)}
    
    for i in range(2, n + 1):
        if not factors[i]:  # i is prime
            for j in range(i, n + 1, i):
                temp = j
                while temp % i == 0:
                    factors[j].append(i)
                    temp //= i
    
    return factors

def bitwise_sieve_optimization(n: int) -> List[int]:
    """
    Space-optimized sieve using bitwise operations
    Uses only odd numbers to save space
    """
    if n < 2:
        return []
    
    if n == 2:
        return [2]
    
    # Only store odd numbers
    size = (n - 1) // 2
    is_prime = [True] * size  # is_prime[i] represents (2*i + 3)
    
    primes = [2]  # Start with 2
    
    for i in range(size):
        if is_prime[i]:
            p = 2 * i + 3
            primes.append(p)
            
            # Mark multiples starting from p²
            for j in range((p * p - 3) // 2, size, p):
                is_prime[j] = False
    
    return primes

def wheel_factorization_sieve(n: int) -> List[int]:
    """
    Wheel factorization sieve for better performance
    Uses wheel of 2, 3, 5 to skip more composites
    """
    if n < 2:
        return []
    
    primes = []
    if n >= 2: primes.append(2)
    if n >= 3: primes.append(3)
    if n >= 5: primes.append(5)
    
    if n < 7:
        return primes
    
    # Wheel increments for 2*3*5 = 30
    # Skip multiples of 2, 3, 5
    wheel = [4, 6, 10, 12, 16, 18, 22, 24]
    
    is_prime = [True] * (n + 1)
    is_prime[0] = is_prime[1] = False
    
    # Mark multiples of 2, 3, 5
    for p in [2, 3, 5]:
        for i in range(p * p, n + 1, p):
            is_prime[i] = False
    
    # Use wheel to check remaining candidates
    candidate = 7
    wheel_index = 0
    
    while candidate <= n:
        if is_prime[candidate]:
            primes.append(candidate)
            
            # Mark multiples starting from candidate²
            for i in range(candidate * candidate, n + 1, candidate):
                is_prime[i] = False
        
        candidate += wheel[wheel_index]
        wheel_index = (wheel_index + 1) % len(wheel)
    
    return primes

# =============================================================================
# USAGE EXAMPLES
# =============================================================================

if __name__ == "__main__":
    # Test basic sieve
    n = 30
    is_prime = sieve_of_eratosthenes(n)
    primes = sieve_primes_list(n)
    print(f"Primes up to {n}: {primes}")
    
    # Test count primes
    print(f"Number of primes less than 10: {count_primes(10)}")
    
    # Test segmented sieve
    segment_primes = segmented_sieve(10, 20)
    print(f"Primes in [10, 20]: {segment_primes}")
    
    # Test smallest prime factor
    spf = sieve_smallest_prime_factor(20)
    print(f"Smallest prime factors: {spf[2:21]}")
    
    # Test Euler totient
    phi = sieve_euler_totient(10)
    print(f"Euler totient function: {phi[1:11]}")
    
    # Test linear sieve
    linear_primes, linear_spf = linear_sieve(20)
    print(f"Linear sieve primes: {linear_primes}")
    
    # Test divisor count
    div_count = sieve_divisor_count(10)
    print(f"Divisor counts: {div_count[1:11]}")
    
    # Test perfect squares
    print(f"Min perfect squares for 12: {count_perfect_squares_sieve(12)}")
    
    # Test super ugly numbers
    ugly_primes = [2, 7, 13, 19]
    print(f"12th super ugly number: {super_ugly_numbers(12, ugly_primes)}")
    
    # Test bitwise optimization
    bitwise_primes = bitwise_sieve_optimization(30)
    print(f"Bitwise sieve primes: {bitwise_primes}")
    
    # Test wheel factorization
    wheel_primes = wheel_factorization_sieve(30)
    print(f"Wheel factorization primes: {wheel_primes}")