"""
Counting Bits - Bit Manipulation

LeetCode #338: Counting Bits
LeetCode #191: Number of 1 Bits
LeetCode #461: Hamming Distance

Core pattern: Count set bits (1s) in binary representation using bit manipulation tricks.
"""

def count_bits(n):
    # For each number from 0 to n, count the number of 1's in its binary representation
    result = [0] * (n + 1)
    
    for i in range(1, n + 1):
        # i & (i-1) removes the rightmost 1 bit
        # result[i] = result[i with the rightmost 1 bit removed] + 1
        result[i] = result[i & (i - 1)] + 1
    
    return result

def hamming_weight(n):
    # Count the number of 1 bits in an integer
    count = 0
    while n:
        n &= (n - 1)  # Remove the rightmost 1 bit
        count += 1
    return count

# Example usage
if __name__ == "__main__":
    n = 5
    print(count_bits(n))      # Output: [0, 1, 1, 2, 1, 2]
    print(hamming_weight(11)) # Output: 3 (11 is 1011 in binary)