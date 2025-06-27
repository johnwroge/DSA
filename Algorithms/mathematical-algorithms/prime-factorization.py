from typing import List, Dict
from collections import defaultdict, Counter
import math

# =============================================================================
# PRIME FACTORIZATION ALGORITHM TEMPLATE
# =============================================================================

"""
LeetCode Problems that can be solved with this technique:
- 650. 2 Keys Keyboard
- 952. Largest Component Size by Common Factor
- 1735. Count Ways to Make Array With Product
- 1808. Maximize Number of Nice Divisors
- 1819. Number of Different Subsequences GCDs
- 1632. Rank Transform of a Matrix
- 1998. GCD Sort of an Array
- 279. Perfect Squares
- 264. Ugly Number II
"""

def is_prime(n: int) -> bool:
    """
    Check if a number is prime
    Time Complexity: O(√n)
    """
    if n < 2:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False
    
    for i in range(3, int(math.sqrt(n)) + 1, 2):
        if n % i == 0:
            return False
    
    return True

def prime_factorize(n: int) -> Dict[int, int]:
    """
    Find prime factorization of n
    Returns dictionary {prime: count}
    Time Complexity: O(√n)
    """
    factors = {}
    d = 2
    
    while d * d <= n:
        while n % d == 0:
            factors[d] = factors.get(d, 0) + 1
            n //= d
        d += 1
    
    if n > 1:
        factors[n] = factors.get(n, 0) + 1
    
    return factors

def prime_factorize_optimized(n: int) -> Dict[int, int]:
    """
    Optimized prime factorization
    Handle 2 separately, then check only odd numbers
    """
    factors = {}
    
    # Handle factor 2
    while n % 2 == 0:
        factors[2] = factors.get(2, 0) + 1
        n //= 2
    
    # Check odd factors from 3 onwards
    d = 3
    while d * d <= n:
        while n % d == 0:
            factors[d] = factors.get(d, 0) + 1
            n //= d
        d += 2
    
    if n > 1:
        factors[n] = factors.get(n, 0) + 1
    
    return factors

def get_divisors(n: int) -> List[int]:
    """
    Get all divisors of n using prime factorization
    Time Complexity: O(√n + d(n)) where d(n) is number of divisors
    """
    if n <= 0:
        return []
    
    factors = prime_factorize(n)
    divisors = [1]
    
    for prime, count in factors.items():
        new_divisors = []
        power = 1
        for _ in range(count):
            power *= prime
            for div in divisors:
                new_divisors.append(div * power)
        divisors.extend(new_divisors)
    
    return sorted(divisors)

def count_divisors(n: int) -> int:
    """
    Count number of divisors using prime factorization
    If n = p1^a1 * p2^a2 * ... * pk^ak, then divisors = (a1+1)(a2+1)...(ak+1)
    """
    factors = prime_factorize(n)
    count = 1
    
    for exponent in factors.values():
        count *= (exponent + 1)
    
    return count

def sum_of_divisors(n: int) -> int:
    """
    Calculate sum of all divisors using prime factorization
    If n = p^k, then sum = (p^(k+1) - 1) / (p - 1)
    """
    factors = prime_factorize(n)
    total_sum = 1
    
    for prime, count in factors.items():
        prime_sum = (prime**(count + 1) - 1) // (prime - 1)
        total_sum *= prime_sum
    
    return total_sum

def min_steps_keyboard(n: int) -> int:
    """
    LeetCode 650: 2 Keys Keyboard
    Find minimum steps to get n 'A's using Copy All and Paste operations
    """
    if n == 1:
        return 0
    
    factors = prime_factorize(n)
    
    # Sum of all prime factors (with repetition)
    steps = 0
    for prime, count in factors.items():
        steps += prime * count
    
    return steps

def largest_component_size(nums: List[int]) -> int:
    """
    LeetCode 952: Largest Component Size by Common Factor
    Find size of largest connected component where nodes are connected if they share a common factor > 1
    """
    # Union-Find implementation
    class UnionFind:
        def __init__(self, n):
            self.parent = list(range(n))
            self.rank = [0] * n
            self.size = [1] * n
        
        def find(self, x):
            if self.parent[x] != x:
                self.parent[x] = self.find(self.parent[x])
            return self.parent[x]
        
        def union(self, x, y):
            px, py = self.find(x), self.find(y)
            if px == py:
                return
            
            if self.rank[px] < self.rank[py]:
                px, py = py, px
            
            self.parent[py] = px
            self.size[px] += self.size[py]
            if self.rank[px] == self.rank[py]:
                self.rank[px] += 1
        
        def get_max_size(self):
            return max(self.size[self.find(i)] for i in range(len(self.parent)))
    
    n = len(nums)
    uf = UnionFind(n)
    
    # Map each prime factor to the indices that have it
    factor_to_indices = defaultdict(list)
    
    for i, num in enumerate(nums):
        factors = prime_factorize(num)
        for prime in factors:
            factor_to_indices[prime].append(i)
    
    # Union indices that share a common prime factor
    for indices in factor_to_indices.values():
        for i in range(1, len(indices)):
            uf.union(indices[0], indices[i])
    
    return uf.get_max_size()

def gcd_sort(nums: List[int]) -> bool:
    """
    LeetCode 1998: GCD Sort of an Array
    Check if array can be sorted by swapping elements with GCD > 1
    """
    class UnionFind:
        def __init__(self, n):
            self.parent = list(range(n))
        
        def find(self, x):
            if self.parent[x] != x:
                self.parent[x] = self.find(self.parent[x])
            return self.parent[x]
        
        def union(self, x, y):
            px, py = self.find(x), self.find(y)
            if px != py:
                self.parent[py] = px
    
    n = len(nums)
    uf = UnionFind(n)
    
    # Group indices by prime factors
    factor_to_indices = defaultdict(list)
    
    for i, num in enumerate(nums):
        factors = prime_factorize(num)
        for prime in factors:
            factor_to_indices[prime].append(i)
    
    # Union indices sharing prime factors
    for indices in factor_to_indices.values():
        for i in range(1, len(indices)):
            uf.union(indices[0], indices[i])
    
    # Check if each element can reach its sorted position
    sorted_nums = sorted(nums)
    for i in range(n):
        # Find where nums[i] should be in sorted array
        target_pos = sorted_nums.index(nums[i])
        if uf.find(i) != uf.find(target_pos):
            return False
        # Remove this element to handle duplicates
        sorted_nums[target_pos] = -1
    
    return True

def count_nice_divisors(prime_factors: int) -> int:
    """
    LeetCode 1808: Maximize Number of Nice Divisors
    Distribute prime_factors among primes to maximize number of divisors
    """
    MOD = 10**9 + 7
    
    if prime_factors <= 4:
        return prime_factors
    
    # To maximize divisors, distribute factors as evenly as possible
    # Prefer 3s over 2s when possible
    if prime_factors % 3 == 0:
        return pow(3, prime_factors // 3, MOD)
    elif prime_factors % 3 == 1:
        # Replace one 3 with two 2s (3+1 = 2+2, but 2*2 > 3*1)
        return pow(3, prime_factors // 3 - 1, MOD) * 4 % MOD
    else:  # prime_factors % 3 == 2
        return pow(3, prime_factors // 3, MOD) * 2 % MOD

def perfect_squares_count(n: int) -> int:
    """
    LeetCode 279: Perfect Squares
    Find minimum number of perfect squares that sum to n
    Uses mathematical properties and prime factorization
    """
    # Legendre's three-square theorem:
    # A positive integer can be represented as sum of three squares
    # if and only if it's not of the form 4^a(8b+7)
    
    def is_perfect_square(x):
        root = int(math.sqrt(x))
        return root * root == x
    
    # Check if n is a perfect square (answer = 1)
    if is_perfect_square(n):
        return 1
    
    # Check if n can be written as sum of two squares (answer = 2)
    for i in range(1, int(math.sqrt(n)) + 1):
        if is_perfect_square(n - i * i):
            return 2
    
    # Check Legendre's theorem for answer = 4
    temp = n
    while temp % 4 == 0:
        temp //= 4
    
    if temp % 8 == 7:
        return 4
    
    # Otherwise answer = 3
    return 3

def ugly_number_ii(n: int) -> int:
    """
    LeetCode 264: Ugly Number II
    Find nth ugly number (numbers with only prime factors 2, 3, 5)
    """
    ugly = [1]
    i2 = i3 = i5 = 0
    
    for _ in range(1, n):
        next_2 = ugly[i2] * 2
        next_3 = ugly[i3] * 3
        next_5 = ugly[i5] * 5
        
        next_ugly = min(next_2, next_3, next_5)
        ugly.append(next_ugly)
        
        if next_ugly == next_2:
            i2 += 1
        if next_ugly == next_3:
            i3 += 1
        if next_ugly == next_5:
            i5 += 1
    
    return ugly[n - 1]

def pollard_rho_factorization(n: int) -> int:
    """
    Pollard's rho algorithm for integer factorization
    Finds a non-trivial factor of n
    """
    def gcd(a, b):
        while b:
            a, b = b, a % b
        return a
    
    def f(x, n, c):
        return (x * x + c) % n
    
    if n % 2 == 0:
        return 2
    
    x = 2
    y = 2
    c = 1
    d = 1
    
    while d == 1:
        x = f(x, n, c)
        y = f(f(y, n, c), n, c)
        d = gcd(abs(x - y), n)
        
        if d == n:
            c += 1
            x = y = 2
            d = 1
    
    return d

def trial_division(n: int) -> List[int]:
    """
    Trial division factorization
    Returns list of prime factors
    """
    factors = []
    d = 2
    
    while d * d <= n:
        while n % d == 0:
            factors.append(d)
            n //= d
        d += 1
    
    if n > 1:
        factors.append(n)
    
    return factors

def factorize_range(start: int, end: int) -> Dict[int, Dict[int, int]]:
    """
    Factorize all numbers in range [start, end]
    Returns {number: {prime: count}}
    """
    result = {}
    
    for num in range(start, end + 1):
        result[num] = prime_factorize(num)
    
    return result

# =============================================================================
# USAGE EXAMPLES
# =============================================================================

if __name__ == "__main__":
    # Test prime factorization
    n = 60
    factors = prime_factorize(n)
    print(f"Prime factorization of {n}: {factors}")
    
    # Test divisors
    divisors = get_divisors(n)
    print(f"Divisors of {n}: {divisors}")
    print(f"Number of divisors: {count_divisors(n)}")
    print(f"Sum of divisors: {sum_of_divisors(n)}")
    
    # Test keyboard problem
    print(f"Min steps for 9 A's: {min_steps_keyboard(9)}")
    
    # Test perfect squares
    print(f"Min perfect squares for 12: {perfect_squares_count(12)}")
    
    # Test ugly numbers
    print(f"10th ugly number: {ugly_number_ii(10)}")
    
    # Test trial division
    factors_list = trial_division(84)
    print(f"Prime factors of 84: {factors_list}")
    
    # Test primality
    print(f"Is 17 prime: {is_prime(17)}")
    print(f"Is 18 prime: {is_prime(18)}")
    
    # Test GCD sort
    nums = [7, 21, 3]
    print(f"Can GCD sort {nums}: {gcd_sort(nums)}")