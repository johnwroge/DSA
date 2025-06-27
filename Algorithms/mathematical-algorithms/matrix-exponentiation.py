from typing import List

# =============================================================================
# MATRIX EXPONENTIATION ALGORITHM TEMPLATE
# =============================================================================

"""
LeetCode Problems that can be solved with this technique:
- 509. Fibonacci Number
- 70. Climbing Stairs
- 1137. N-th Tribonacci Number
- 552. Student Attendance Record II
- 790. Domino and Tromino Tiling
- 935. Knight Dialer
- 1220. Count Vowels Permutation
- 1416. Restore The Array
- 1547. Minimum Cost to Cut a Stick
"""

def matrix_multiply(A: List[List[int]], B: List[List[int]], mod: int = None) -> List[List[int]]:
    """
    Multiply two matrices with optional modular arithmetic
    Time Complexity: O(n^3) where n is matrix dimension
    """
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

def matrix_power(matrix: List[List[int]], n: int, mod: int = None) -> List[List[int]]:
    """
    Calculate matrix^n using fast exponentiation
    Time Complexity: O(k^3 * log n) where k is matrix dimension
    """
    if n == 0:
        # Return identity matrix
        size = len(matrix)
        identity = [[0] * size for _ in range(size)]
        for i in range(size):
            identity[i][i] = 1
        return identity
    
    if n == 1:
        return [row[:] for row in matrix]  # Deep copy
    
    result = None
    base = [row[:] for row in matrix]  # Deep copy
    
    while n > 0:
        if n & 1:
            if result is None:
                result = [row[:] for row in base]
            else:
                result = matrix_multiply(result, base, mod)
        
        n >>= 1
        if n > 0:
            base = matrix_multiply(base, base, mod)
    
    return result

def fibonacci_matrix(n: int) -> int:
    """
    LeetCode 509: Calculate nth Fibonacci number using matrix exponentiation
    [F(n+1)]   [1 1]^n   [F(1)]   [1 1]^n   [1]
    [F(n)  ] = [1 0]   * [F(0)] = [1 0]   * [0]
    """
    if n <= 1:
        return n
    
    # Transformation matrix for Fibonacci
    fib_matrix = [[1, 1], [1, 0]]
    
    result_matrix = matrix_power(fib_matrix, n)
    
    # F(n) = result_matrix[0][1] * F(1) + result_matrix[1][1] * F(0)
    return result_matrix[0][1]

def climbing_stairs_matrix(n: int) -> int:
    """
    LeetCode 70: Climbing stairs using matrix exponentiation
    Same recurrence as Fibonacci: f(n) = f(n-1) + f(n-2)
    """
    if n <= 2:
        return n
    
    # Transform matrix [f(n), f(n-1)] = [f(n-1), f(n-2)] * [[1, 1], [1, 0]]
    stairs_matrix = [[1, 1], [1, 0]]
    
    result_matrix = matrix_power(stairs_matrix, n - 1)
    
    # f(n) = result_matrix[0][0] * f(1) + result_matrix[0][1] * f(0)
    # where f(1) = 1, f(0) = 1 (base cases for stairs)
    return result_matrix[0][0] * 1 + result_matrix[0][1] * 1

def tribonacci_matrix(n: int) -> int:
    """
    LeetCode 1137: N-th Tribonacci Number using matrix exponentiation
    T(n) = T(n-1) + T(n-2) + T(n-3)
    """
    if n == 0:
        return 0
    if n <= 2:
        return 1
    
    # Transformation matrix for Tribonacci
    # [T(n), T(n-1), T(n-2)] = [T(n-1), T(n-2), T(n-3)] * transformation_matrix
    trib_matrix = [
        [1, 1, 1],
        [1, 0, 0],
        [0, 1, 0]
    ]
    
    result_matrix = matrix_power(trib_matrix, n - 2)
    
    # T(n) = result_matrix[0][0] * T(2) + result_matrix[0][1] * T(1) + result_matrix[0][2] * T(0)
    return result_matrix[0][0] * 1 + result_matrix[0][1] * 1 + result_matrix[0][2] * 0

def count_attendance_records(n: int) -> int:
    """
    LeetCode 552: Student Attendance Record II
    Count valid attendance records of length n
    States: (A_count, consecutive_L_count) where A_count <= 1, consecutive_L_count <= 2
    """
    MOD = 10**9 + 7
    
    if n == 1:
        return 3  # P, A, L
    
    # States: [A0L0, A0L1, A0L2, A1L0, A1L1, A1L2]
    # A0L0: 0 A's, 0 consecutive L's at end
    # A0L1: 0 A's, 1 consecutive L at end
    # A0L2: 0 A's, 2 consecutive L's at end
    # A1L0: 1 A, 0 consecutive L's at end
    # A1L1: 1 A, 1 consecutive L at end
    # A1L2: 1 A, 2 consecutive L's at end
    
    # Transition matrix
    transition = [
        # From A0L0: +P->A0L0, +L->A0L1, +A->A1L0
        [1, 1, 0, 1, 0, 0],
        # From A0L1: +P->A0L0, +L->A0L2, +A->A1L0
        [1, 0, 1, 1, 0, 0],
        # From A0L2: +P->A0L0, +A->A1L0 (can't add L)
        [1, 0, 0, 1, 0, 0],
        # From A1L0: +P->A1L0, +L->A1L1 (can't add A)
        [0, 0, 0, 1, 1, 0],
        # From A1L1: +P->A1L0, +L->A1L2 (can't add A)
        [0, 0, 0, 1, 0, 1],
        # From A1L2: +P->A1L0 (can't add A or L)
        [0, 0, 0, 1, 0, 0]
    ]
    
    result_matrix = matrix_power(transition, n - 1, MOD)
    
    # Start from A0L0 state (empty record)
    # Sum all final states
    total = 0
    for i in range(6):
        total = (total + result_matrix[i][0]) % MOD
    
    return total

def num_tilings(n: int) -> int:
    """
    LeetCode 790: Domino and Tromino Tiling
    Count ways to tile 2 x n board
    """
    MOD = 10**9 + 7
    
    if n <= 2:
        return n
    
    # States based on the rightmost column configuration
    # State 0: Both cells filled
    # State 1: Top cell filled, bottom empty (from previous L-tromino)
    # State 2: Top empty, bottom filled (from previous L-tromino)
    
    # Transition matrix
    # From state 0: can place vertical domino (->0), or two L-trominoes (->1,2)
    # From state 1: can place L-tromino (->0), or horizontal domino (->2)
    # From state 2: can place L-tromino (->0), or horizontal domino (->1)
    transition = [
        [1, 1, 1],  # State 0 transitions
        [1, 0, 1],  # State 1 transitions
        [1, 1, 0]   # State 2 transitions
    ]
    
    result_matrix = matrix_power(transition, n - 1, MOD)
    
    # Start from state 0 (empty board)
    return result_matrix[0][0]

def knight_dialer(n: int) -> int:
    """
    LeetCode 935: Knight Dialer
    Count distinct phone numbers of length n that can be dialed by knight moves
    """
    MOD = 10**9 + 7
    
    if n == 1:
        return 10
    
    # Adjacency for knight moves on phone keypad
    # 0: can go to 4, 6
    # 1: can go to 6, 8
    # 2: can go to 7, 9
    # 3: can go to 4, 8
    # 4: can go to 0, 3, 9
    # 5: nowhere (isolated)
    # 6: can go to 0, 1, 7
    # 7: can go to 2, 6
    # 8: can go to 1, 3
    # 9: can go to 2, 4
    
    # Transition matrix (10x10)
    transition = [[0] * 10 for _ in range(10)]
    
    # Define valid moves
    moves = {
        0: [4, 6],
        1: [6, 8],
        2: [7, 9],
        3: [4, 8],
        4: [0, 3, 9],
        5: [],  # No valid moves
        6: [0, 1, 7],
        7: [2, 6],
        8: [1, 3],
        9: [2, 4]
    }
    
    for digit in range(10):
        for next_digit in moves[digit]:
            transition[next_digit][digit] = 1
    
    result_matrix = matrix_power(transition, n - 1, MOD)
    
    # Sum all possible endings starting from each digit
    total = 0
    for i in range(10):
        for j in range(10):
            total = (total + result_matrix[i][j]) % MOD
    
    return total

def count_vowel_permutation(n: int) -> int:
    """
    LeetCode 1220: Count Vowels Permutation
    Count strings of length n with vowels following specific rules
    """
    MOD = 10**9 + 7
    
    if n == 1:
        return 5
    
    # Vowels: a=0, e=1, i=2, o=3, u=4
    # Rules:
    # a can only be followed by e
    # e can only be followed by a or i
    # i can only be followed by a, e, o, or u
    # o can only be followed by i or u
    # u can only be followed by a
    
    # Transition matrix
    transition = [
        [0, 1, 0, 0, 0],  # a -> e
        [1, 0, 1, 0, 0],  # e -> a, i
        [1, 1, 0, 1, 1],  # i -> a, e, o, u
        [0, 0, 1, 0, 1],  # o -> i, u
        [1, 0, 0, 0, 0]   # u -> a
    ]
    
    result_matrix = matrix_power(transition, n - 1, MOD)
    
    # Sum all possibilities starting from each vowel
    total = 0
    for i in range(5):
        for j in range(5):
            total = (total + result_matrix[i][j]) % MOD
    
    return total

def linear_recurrence_solver(coefficients: List[int], initial_values: List[int], n: int, mod: int = None) -> int:
    """
    Generic solver for linear recurrence relations
    f(n) = c0*f(n-1) + c1*f(n-2) + ... + ck*f(n-k-1)
    """
    k = len(coefficients)
    
    if n < k:
        return initial_values[n] if n < len(initial_values) else 0
    
    # Build transformation matrix
    transformation = [[0] * k for _ in range(k)]
    
    # First row contains coefficients
    for i in range(k):
        transformation[0][i] = coefficients[i]
    
    # Other rows shift the state
    for i in range(1, k):
        transformation[i][i-1] = 1
    
    result_matrix = matrix_power(transformation, n - k + 1, mod)
    
    # Calculate result
    result = 0
    for i in range(k):
        if i < len(initial_values):
            result += result_matrix[0][k-1-i] * initial_values[k-1-i]
            if mod:
                result %= mod
    
    return result

# =============================================================================
# USAGE EXAMPLES
# =============================================================================

if __name__ == "__main__":
    # Test Fibonacci
    print(f"10th Fibonacci number: {fibonacci_matrix(10)}")
    
    # Test climbing stairs
    print(f"Ways to climb 5 stairs: {climbing_stairs_matrix(5)}")
    
    # Test Tribonacci
    print(f"10th Tribonacci number: {tribonacci_matrix(10)}")
    
    # Test attendance records
    print(f"Valid attendance records of length 3: {count_attendance_records(3)}")
    
    # Test domino tiling
    print(f"Ways to tile 2x3 board: {num_tilings(3)}")
    
    # Test knight dialer
    print(f"Knight dialer numbers of length 2: {knight_dialer(2)}")
    
    # Test vowel permutation
    print(f"Vowel permutations of length 2: {count_vowel_permutation(2)}")
    
    # Test generic linear recurrence (Fibonacci as example)
    fib_result = linear_recurrence_solver([1, 1], [0, 1], 10)
    print(f"10th Fibonacci via generic solver: {fib_result}")