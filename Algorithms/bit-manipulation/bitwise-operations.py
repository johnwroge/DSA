"""
Bitwise Operations - Bit Manipulation

LeetCode #136: Single Number
LeetCode #137: Single Number II
LeetCode #260: Single Number III

Core pattern: Use XOR, AND, OR, NOT to manipulate individual bits efficiently.
"""

def single_number(nums):
    # XOR of a number with itself is 0
    # XOR of a number with 0 is the number itself
    result = 0
    for num in nums:
        result ^= num
    return result

def count_set_bits(n):
    count = 0
    while n:
        # n & (n-1) removes the rightmost set bit
        n &= (n - 1)
        count += 1
    return count

def is_power_of_two(n):
    # Powers of 2 have only one bit set, so n & (n-1) = 0
    return n > 0 and (n & (n - 1)) == 0

# Example usage
if __name__ == "__main__":
    nums = [4, 1, 2, 1, 2]
    print(single_number(nums))  # Output: 4
    print(count_set_bits(7))    # Output: 3 (111 in binary)
    print(is_power_of_two(8))   # Output: True