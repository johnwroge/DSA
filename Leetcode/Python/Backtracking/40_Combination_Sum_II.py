'''
40. Combination Sum II

Given a collection of candidate numbers (candidates) and a target number (target),
find all unique combinations in candidates where the candidate numbers sum to target.

Each number in candidates may only be used once in the combination.

Note: The solution set must not contain duplicate combinations.

 

Example 1:

Input: candidates = [10,1,2,7,6,1,5], target = 8
Output: 
[
[1,1,6],
[1,2,5],
[1,7],
[2,6]
]
Example 2:

Input: candidates = [2,5,2,1,2], target = 5
Output: 
[
[1,2,2],
[5]
]
 

Constraints:

1 <= candidates.length <= 100
1 <= candidates[i] <= 50
1 <= target <= 30
'''


class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []
        curr = []
        candidates.sort()
        def backtrack(index, total):
            if total == 0:
                res.append(curr.copy()) if curr not in res else None
                return
            if total < 0 or index >= len(candidates):
                return
            
            for i in range(index, len(candidates)):
                if candidates[i] > target:
                    continue
                if i > index and candidates[i] == candidates[i - 1]:
                    continue
                curr.append(candidates[i])
                backtrack(i + 1, total - candidates[i])
                curr.pop()
                
        
        backtrack(0,target)
        return res
        