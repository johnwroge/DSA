"""
Bit Masks - Bit Manipulation

LeetCode #78: Subsets
LeetCode #187: Repeated DNA Sequences
LeetCode #1178: Number of Valid Words for Each Puzzle

Core pattern: Use binary representation to represent sets or states.
"""

def generate_subsets(nums):
    n = len(nums)
    subsets = []
    
    # 2^n possible subsets (each element is either included or excluded)
    for mask in range(1 << n):
        subset = []
        for i in range(n):
            # Check if ith bit is set
            if mask & (1 << i):
                subset.append(nums[i])
        subsets.append(subset)
    
    return subsets

# Example usage
if __name__ == "__main__":
    nums = [1, 2, 3]
    print(generate_subsets(nums))