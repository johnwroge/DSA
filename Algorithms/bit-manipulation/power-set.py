"""
Power Set - Bit Manipulation

LeetCode #78: Subsets
LeetCode #90: Subsets II
LeetCode #1986: Minimum Number of Work Sessions to Finish the Tasks

Core pattern: Generate all possible combinations using bit representation.
"""

def power_set(nums):
    n = len(nums)
    result = []
    
    # 2^n possible subsets
    for i in range(1 << n):
        subset = []
        for j in range(n):
            # Check if jth bit is set in i
            if (i & (1 << j)) != 0:
                subset.append(nums[j])
        result.append(subset)
    
    return result

# Example usage
if __name__ == "__main__":
    nums = [1, 2, 3]
    print(power_set(nums))