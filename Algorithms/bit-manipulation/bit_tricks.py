"""
Bit Manipulation Tricks - Bit Manipulation

LeetCode #201: Bitwise AND of Numbers Range
LeetCode #371: Sum of Two Integers
LeetCode #477: Total Hamming Distance

Core pattern: Use bit properties for specific operations without using arithmetic operators.
"""

def get_sum(a, b):
    # Add two integers without using arithmetic operators
    while b != 0:
        carry = a & b  # Bits that generate a carry
        a = a ^ b      # Sum without considering carries
        b = carry << 1 # Carry shifted to the left
    return a

def range_bitwise_and(m, n):
    # Find bitwise AND of all numbers in range [m, n]
    # This is essentially finding the common prefix of m and n in binary
    shift = 0
    while m < n:
        m >>= 1
        n >>= 1
        shift += 1
    return m << shift

def swap_bits(x, i, j):
    # Swap ith and jth bits in x
    # Only swap if the bits are different
    if ((x >> i) & 1) != ((x >> j) & 1):
        # Create a mask with 1s at positions i and j
        mask = (1 << i) | (1 << j)
        # Flip those bits using XOR
        x ^= mask
    return x

# Example usage
if __name__ == "__main__":
    print(get_sum(2, 3))         # Output: 5
    print(range_bitwise_and(5, 7)) # Output: 4
    print(swap_bits(10, 1, 3))    # Output: 14 (1010 -> 1110)