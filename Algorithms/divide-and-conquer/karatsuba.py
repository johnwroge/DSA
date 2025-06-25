"""
Karatsuba Multiplication - Divide and Conquer

LeetCode #43: Multiply Strings
LeetCode #2266: Count Number of Texts

Core pattern: Recursively multiply large numbers by breaking them into smaller parts.
"""

def karatsuba_multiply(x, y):
    # Base case for recursion
    if x < 10 or y < 10:
        return x * y
    
    # Calculate size of numbers
    str_x, str_y = str(x), str(y)
    n = max(len(str_x), len(str_y))
    m = n // 2
    
    # Split numbers into high and low parts
    power = 10 ** m
    a, b = x // power, x % power
    c, d = y // power, y % power
    
    # Three recursive multiplications (instead of four)
    ac = karatsuba_multiply(a, c)
    bd = karatsuba_multiply(b, d)
    abcd = karatsuba_multiply(a + b, c + d) - ac - bd
    
    # Combine results
    return ac * (10 ** (2 * m)) + abcd * (10 ** m) + bd

# Example usage
if __name__ == "__main__":
    x, y = 1234, 5678
    print(karatsuba_multiply(x, y))  # Output: 7006652