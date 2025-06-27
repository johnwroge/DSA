from typing import List

# =============================================================================
# FAST POWER ALGORITHM TEMPLATE
# =============================================================================

"""
LeetCode Problems that can be solved with this technique:
- 50. Pow(x, n)
- 372. Super Pow
- 1922. Count Good Numbers
- 1812. Determine Color of a Chessboard Square
- 1969. Minimum Non-Zero Product of the Array Elements
- 1498. Number of Subsequences That Satisfy the Given Sum Condition
- 1352. Product of the Last K Numbers
- 1590. Make Sum Divisible by P
"""

def fast_power(base: int, exp: int, mod: int = None) -> int:
    """
    Calculate base^exp efficiently using binary exponentiation
    Time Complexity: O(log exp)
    Space Complexity: O(1)
    """
    if exp == 0:
        return 1
    
    result = 1
    base = base % mod if mod else base
    
    while exp > 0:
        # If exp is odd, multiply result with current base
        if exp & 1:
            result = (result * base) % mod if mod else result * base
        
        # Square the base and halve the exponent
        exp >>= 1
        base = (base * base) % mod if mod else base * base
    
    return result

def fast_power_recursive(base: int, exp: int, mod: int = None) -> int:
    """
    Recursive implementation of fast power
    """
    if exp == 0:
        return 1
    if exp == 1:
        return base % mod if mod else base
    
    if exp & 1:  # Odd exponent
        half_power = fast_power_recursive(base, exp // 2, mod)
        result = (half_power * half_power * base)
        return result % mod if mod else result
    else:  # Even exponent
        half_power = fast_power_recursive(base, exp // 2, mod)
        result = half_power * half_power
        return result % mod if mod else result

def pow_x_n(x: float, n: int) -> float:
    """
    LeetCode 50: Implement pow(x, n)
    Handle negative exponents and edge cases
    """
    if n == 0:
        return 1.0
    
    if n < 0:
        x = 1 / x
        n = -n
    
    result = 1.0
    current_power = x
    
    while n > 0:
        if n & 1:
            result *= current_power
        current_power *= current_power
        n >>= 1
    
    return result

def super_pow(a: int, b: List[int]) -> int:
    """
    LeetCode 372: Calculate a^b where b is represented as array of digits
    Use property: a^1234 = (a^123)^10 * a^4
    """
    MOD = 1337
    
    def pow_mod(base: int, exp: int) -> int:
        return fast_power(base, exp, MOD)
    
    if not b:
        return 1
    
    last_digit = b.pop()
    return pow_mod(super_pow(a, b), 10) * pow_mod(a, last_digit) % MOD

def count_good_numbers(n: int) -> int:
    """
    LeetCode 1922: Count good numbers of length n
    Even positions: 5 choices (0,2,4,6,8)
    Odd positions: 4 choices (2,3,5,7)
    """
    MOD = 10**9 + 7
    
    even_positions = (n + 1) // 2  # Ceiling division
    odd_positions = n // 2
    
    even_contribution = fast_power(5, even_positions, MOD)
    odd_contribution = fast_power(4, odd_positions, MOD)
    
    return (even_contribution * odd_contribution) % MOD

def minimum_non_zero_product(p: int) -> int:
    """
    LeetCode 1969: Find minimum non-zero product of array elements
    Array contains all integers from 1 to 2^p - 1
    Strategy: pair numbers to minimize product
    """
    MOD = 10**9 + 7
    
    max_num = (1 << p) - 1  # 2^p - 1
    pairs = (max_num - 1) // 2
    
    # Each pair contributes max_num - 1 to the product
    # Plus the middle element if odd number of elements
    if max_num == 1:
        return 1
    
    result = fast_power(max_num - 1, pairs, MOD)
    result = (result * max_num) % MOD
    
    return result

def chessboard_square_color(coordinates: str) -> bool:
    """
    LeetCode 1812: Determine if chessboard square is white
    Use mathematical property: (row + col) % 2 determines color
    """
    col = ord(coordinates[0]) - ord('a') + 1
    row = int(coordinates[1])
    
    # If sum is even, square is black; if odd, square is white
    return (col + row) % 2 == 1

def num_subsequences(nums: List[int], target: int) -> int:
    """
    LeetCode 1498: Number of subsequences with sum <= target
    Use two pointers and fast power for counting subsequences
    """
    MOD = 10**9 + 7
    nums.sort()
    
    left, right = 0, len(nums) - 1
    result = 0
    
    # Precompute powers of 2
    powers = [1] * len(nums)
    for i in range(1, len(nums)):
        powers[i] = (powers[i-1] * 2) % MOD
    
    while left <= right:
        if nums[left] + nums[right] <= target:
            # All subsequences starting with nums[left] are valid
            result = (result + powers[right - left]) % MOD
            left += 1
        else:
            right -= 1
    
    return result

def matrix_power(matrix: List[List[int]], n: int, mod: int = None) -> List[List[int]]:
    """
    Calculate matrix^n using fast exponentiation
    Useful for solving linear recurrence relations
    """
    def matrix_multiply(A: List[List[int]], B: List[List[int]]) -> List[List[int]]:
        rows_A, cols_A = len(A), len(A[0])
        rows_B, cols_B = len(B), len(B[0])
        
        if cols_A != rows_B:
            raise ValueError("Matrix dimensions incompatible for multiplication")
        
        result = [[0] * cols_B for _ in range(rows_A)]
        
        for i in range(rows_A):
            for j in range(cols_B):
                for k in range(cols_A):
                    result[i][j] += A[i][k] * B[k][j]
                    if mod:
                        result[i][j] %= mod
        
        return result
    
    if n == 0:
        # Return identity matrix
        size = len(matrix)
        identity = [[0] * size for _ in range(size)]
        for i in range(size):
            identity[i][i] = 1
        return identity
    
    result = None
    base = [row[:] for row in matrix]  # Deep copy
    
    while n > 0:
        if n & 1:
            if result is None:
                result = [row[:] for row in base]
            else:
                result = matrix_multiply(result, base)
        
        n >>= 1
        if n > 0:
            base = matrix_multiply(base, base)
    
    return result

def fibonacci_fast(n: int) -> int:
    """
    Calculate nth Fibonacci number using matrix exponentiation
    F(n) = [[1,1],[1,0]]^n * [[1],[0]]
    """
    if n <= 1:
        return n
    
    # Transformation matrix for Fibonacci
    fib_matrix = [[1, 1], [1, 0]]
    
    result_matrix = matrix_power(fib_matrix, n - 1)
    
    # F(n) = result_matrix[0][0] * F(1) + result_matrix[0][1] * F(0)
    return result_matrix[0][0] * 1 + result_matrix[0][1] * 0

# =============================================================================
# USAGE EXAMPLES
# =============================================================================

if __name__ == "__main__":
    # Test fast power
    print(f"2^10 = {fast_power(2, 10)}")
    print(f"3^5 mod 7 = {fast_power(3, 5, 7)}")
    
    # Test pow(x, n)
    print(f"2.0^10 = {pow_x_n(2.0, 10)}")
    print(f"2.0^-2 = {pow_x_n(2.0, -2)}")
    
    # Test super pow
    print(f"2^[1,0] mod 1337 = {super_pow(2, [1, 0])}")
    
    # Test good numbers
    print(f"Good numbers of length 4: {count_good_numbers(4)}")
    
    # Test chessboard
    print(f"'a1' is white: {chessboard_square_color('a1')}")
    print(f"'h3' is white: {chessboard_square_color('h3')}")
    
    # Test Fibonacci
    print(f"10th Fibonacci number: {fibonacci_fast(10)}")
    
    # Test subsequences
    nums = [3, 5, 6, 7]
    target = 9
    print(f"Valid subsequences: {num_subsequences(nums, target)}")