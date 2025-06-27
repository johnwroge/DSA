from typing import List
import math

# =============================================================================
# GCD AND LCM ALGORITHM TEMPLATE
# =============================================================================

"""
LeetCode Problems that can be solved with this technique:
- 1071. Greatest Common Divisor of Strings
- 914. X of a Kind in a Deck of Cards
- 1979. Find Greatest Common Divisor of Array
- 2413. Smallest Even Multiple
- 1342. Number of Steps to Reduce a Number to Zero
- 1952. Three Divisors
- 1486. XOR Operation in an Array
- 365. Water and Jug Problem
- 780. Reaching Points
"""

def gcd(a: int, b: int) -> int:
    """
    Calculate Greatest Common Divisor using Euclidean algorithm
    Time Complexity: O(log(min(a, b)))
    Space Complexity: O(1)
    """
    while b:
        a, b = b, a % b
    return a

def gcd_recursive(a: int, b: int) -> int:
    """
    Recursive implementation of GCD
    """
    if b == 0:
        return a
    return gcd_recursive(b, a % b)

def extended_gcd(a: int, b: int) -> tuple:
    """
    Extended Euclidean Algorithm
    Returns (gcd, x, y) such that ax + by = gcd(a, b)
    """
    if b == 0:
        return a, 1, 0
    
    gcd_val, x1, y1 = extended_gcd(b, a % b)
    x = y1
    y = x1 - (a // b) * y1
    
    return gcd_val, x, y

def lcm(a: int, b: int) -> int:
    """
    Calculate Least Common Multiple
    LCM(a, b) = (a * b) / GCD(a, b)
    """
    return abs(a * b) // gcd(a, b)

def gcd_array(arr: List[int]) -> int:
    """
    Calculate GCD of entire array
    """
    if not arr:
        return 0
    
    result = arr[0]
    for i in range(1, len(arr)):
        result = gcd(result, arr[i])
        if result == 1:  # Early termination
            break
    
    return result

def lcm_array(arr: List[int]) -> int:
    """
    Calculate LCM of entire array
    """
    if not arr:
        return 0
    
    result = arr[0]
    for i in range(1, len(arr)):
        result = lcm(result, arr[i])
    
    return result

def gcd_string(str1: str, str2: str) -> str:
    """
    LeetCode 1071: Greatest Common Divisor of Strings
    Find largest string that divides both input strings
    """
    # Check if concatenations are equal
    if str1 + str2 != str2 + str1:
        return ""
    
    # GCD of lengths gives us the answer
    gcd_length = gcd(len(str1), len(str2))
    return str1[:gcd_length]

def has_groups_size_x(deck: List[int]) -> bool:
    """
    LeetCode 914: X of a Kind in a Deck of Cards
    Check if deck can be divided into groups of same size >= 2
    """
    from collections import Counter
    
    counts = Counter(deck)
    gcd_val = 0
    
    for count in counts.values():
        gcd_val = gcd(gcd_val, count)
    
    return gcd_val >= 2

def find_gcd_array(nums: List[int]) -> int:
    """
    LeetCode 1979: Find Greatest Common Divisor of Array
    Return GCD of smallest and largest element
    """
    return gcd(min(nums), max(nums))

def smallest_even_multiple(n: int) -> int:
    """
    LeetCode 2413: Smallest Even Multiple
    Find smallest positive integer that is multiple of both 2 and n
    """
    return lcm(2, n)

def can_measure_water(jug1_capacity: int, jug2_capacity: int, target_capacity: int) -> bool:
    """
    LeetCode 365: Water and Jug Problem
    Check if we can measure target_capacity using two jugs
    Uses Bezout's identity: ax + by = c has solution iff gcd(a,b) divides c
    """
    if target_capacity > jug1_capacity + jug2_capacity:
        return False
    
    if target_capacity == 0:
        return True
    
    return target_capacity % gcd(jug1_capacity, jug2_capacity) == 0

def reaching_points(sx: int, sy: int, tx: int, ty: int) -> bool:
    """
    LeetCode 780: Reaching Points
    Check if we can reach (tx, ty) from (sx, sy) using operations:
    (x, y) -> (x + y, y) or (x, y + x)
    """
    while tx >= sx and ty >= sy:
        if tx == sx and ty == sy:
            return True
        
        if tx > ty:
            # If ty == sy, we can only reduce tx by subtracting ty
            if ty == sy:
                return (tx - sx) % ty == 0
            tx %= ty
        else:
            # If tx == sx, we can only reduce ty by subtracting tx
            if tx == sx:
                return (ty - sy) % tx == 0
            ty %= tx
    
    return False

def count_pairs_with_gcd(nums: List[int], target_gcd: int) -> int:
    """
    Count pairs (i, j) where gcd(nums[i], nums[j]) == target_gcd
    """
    count = 0
    n = len(nums)
    
    for i in range(n):
        for j in range(i + 1, n):
            if gcd(nums[i], nums[j]) == target_gcd:
                count += 1
    
    return count

def coprime_numbers(n: int) -> List[int]:
    """
    Find all numbers less than n that are coprime with n
    Two numbers are coprime if gcd(a, b) = 1
    """
    result = []
    for i in range(1, n):
        if gcd(i, n) == 1:
            result.append(i)
    return result

def euler_totient(n: int) -> int:
    """
    Calculate Euler's totient function φ(n)
    Count of numbers less than n that are coprime with n
    """
    result = n
    p = 2
    
    while p * p <= n:
        if n % p == 0:
            # Remove multiples of p
            while n % p == 0:
                n //= p
            result -= result // p
        p += 1
    
    if n > 1:
        result -= result // n
    
    return result

def is_coprime(a: int, b: int) -> bool:
    """
    Check if two numbers are coprime (gcd = 1)
    """
    return gcd(a, b) == 1

def modular_inverse(a: int, m: int) -> int:
    """
    Find modular inverse of a modulo m using extended GCD
    Returns x such that (a * x) % m = 1
    Only exists if gcd(a, m) = 1
    """
    gcd_val, x, y = extended_gcd(a, m)
    
    if gcd_val != 1:
        return -1  # Modular inverse doesn't exist
    
    return (x % m + m) % m

def chinese_remainder_theorem(remainders: List[int], moduli: List[int]) -> int:
    """
    Solve system of congruences using Chinese Remainder Theorem
    x ≡ remainders[i] (mod moduli[i]) for all i
    Assumes all moduli are pairwise coprime
    """
    if len(remainders) != len(moduli):
        return -1
    
    # Check if moduli are pairwise coprime
    n = len(moduli)
    for i in range(n):
        for j in range(i + 1, n):
            if gcd(moduli[i], moduli[j]) != 1:
                return -1  # Not pairwise coprime
    
    total_mod = 1
    for mod in moduli:
        total_mod *= mod
    
    result = 0
    for i in range(n):
        Mi = total_mod // moduli[i]
        yi = modular_inverse(Mi, moduli[i])
        result += remainders[i] * Mi * yi
    
    return result % total_mod

def reduce_fraction(numerator: int, denominator: int) -> tuple:
    """
    Reduce fraction to lowest terms using GCD
    """
    if denominator == 0:
        raise ValueError("Denominator cannot be zero")
    
    common_divisor = gcd(abs(numerator), abs(denominator))
    
    reduced_num = numerator // common_divisor
    reduced_den = denominator // common_divisor
    
    # Ensure denominator is positive
    if reduced_den < 0:
        reduced_num = -reduced_num
        reduced_den = -reduced_den
    
    return reduced_num, reduced_den

def gcd_polynomial_evaluation(coefficients: List[int], x_values: List[int]) -> int:
    """
    Find GCD of polynomial evaluations at different x values
    """
    if not coefficients or not x_values:
        return 0
    
    def evaluate_polynomial(coeffs: List[int], x: int) -> int:
        result = 0
        power = 1
        for coeff in coeffs:
            result += coeff * power
            power *= x
        return result
    
    evaluations = [evaluate_polynomial(coefficients, x) for x in x_values]
    return gcd_array(evaluations)

# =============================================================================
# USAGE EXAMPLES
# =============================================================================

if __name__ == "__main__":
    # Test basic GCD and LCM
    print(f"GCD(48, 18) = {gcd(48, 18)}")
    print(f"LCM(12, 8) = {lcm(12, 8)}")
    
    # Test extended GCD
    gcd_val, x, y = extended_gcd(30, 18)
    print(f"Extended GCD(30, 18): gcd={gcd_val}, x={x}, y={y}")
    print(f"Verification: 30*{x} + 18*{y} = {30*x + 18*y}")
    
    # Test string GCD
    print(f"GCD('ABCABC', 'ABC') = '{gcd_string('ABCABC', 'ABC')}'")
    
    # Test array GCD/LCM
    arr = [12, 18, 24]
    print(f"GCD of {arr} = {gcd_array(arr)}")
    print(f"LCM of {arr} = {lcm_array(arr)}")
    
    # Test water jug problem
    print(f"Can measure 4L with 3L and 5L jugs: {can_measure_water(3, 5, 4)}")
    
    # Test coprime check
    print(f"Are 15 and 28 coprime: {is_coprime(15, 28)}")
    
    # Test Euler's totient
    print(f"φ(12) = {euler_totient(12)}")
    
    # Test modular inverse
    inv = modular_inverse(3, 7)
    print(f"Modular inverse of 3 mod 7 = {inv}")
    if inv != -1:
        print(f"Verification: (3 * {inv}) mod 7 = {(3 * inv) % 7}")
    
    # Test fraction reduction
    num, den = reduce_fraction(24, 36)
    print(f"24/36 reduced = {num}/{den}")