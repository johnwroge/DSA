"""
Combination Sum - Backtracking

LeetCode #39: Combination Sum
LeetCode #40: Combination Sum II
LeetCode #216: Combination Sum III

Core pattern: Build combinations incrementally, backtracking when sum exceeds target.
"""

def combination_sum(candidates, target):
    def backtrack(start, target, path):
        if target == 0:
            result.append(path.copy())
            return
        if target < 0:
            return
        for i in range(start, len(candidates)):
            path.append(candidates[i])
            backtrack(i, target - candidates[i], path)
            path.pop()
    
    result = []
    backtrack(0, target, [])
    return result

# Example usage
if __name__ == "__main__":
    candidates = [2, 3, 6, 7]
    target = 7
    print(combination_sum(candidates, target))