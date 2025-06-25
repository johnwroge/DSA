"""
Permutations - Backtracking

LeetCode #46: Permutations
LeetCode #47: Permutations II

Core pattern: Generate all possible orderings by swapping elements and recursively permuting the rest.
"""

def permute(nums):
    def backtrack(start):
        if start == len(nums):
            result.append(nums.copy())
            return
        for i in range(start, len(nums)):
            nums[start], nums[i] = nums[i], nums[start]
            backtrack(start + 1)
            nums[start], nums[i] = nums[i], nums[start]
    
    result = []
    backtrack(0)
    return result

# Example usage
if __name__ == "__main__":
    nums = [1, 2, 3]
    print(permute(nums))