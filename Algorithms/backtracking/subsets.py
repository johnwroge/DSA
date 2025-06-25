"""
Subsets - Backtracking

LeetCode #78: Subsets
LeetCode #90: Subsets II

Core pattern: Generate all possible combinations by including or excluding each element.
"""

def subsets(nums):
    def backtrack(start, path):
        result.append(path.copy())
        for i in range(start, len(nums)):
            path.append(nums[i])
            backtrack(i + 1, path)
            path.pop()
    
    result = []
    backtrack(0, [])
    return result

# Example usage
if __name__ == "__main__":
    nums = [1, 2, 3]
    print(subsets(nums))