'''
64 Minimum Path Sum

Given a m x n grid filled with non-negative numbers, 
find a path from top left to bottom right, which minimizes the sum of all numbers along its path.

Note: You can only move either down or right at any point in time.

Input: grid = [[1,3,1],[1,5,1],[4,2,1]]
Output: 7
Explanation: Because the path 1 → 3 → 1 → 1 → 1 minimizes the sum.
Example 2:

Input: grid = [[1,2,3],[4,5,6]]
Output: 12
'''

# unoptimized solution

class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        # iterate over bottom row and add 
        row = grid[len(grid) - 1]
        for i in range(len(row) - 2, -1, -1):
            row[i] += row[i + 1]
        
        #iterate right side and add
        for i in range(len(grid) - 2, -1, -1):
            for j in range(len(grid[i]) - 1, len(grid[i]) - 2, -1):
                grid[i][j] += grid[i + 1][j] 

        # determine the local min at 2nd last row and index     
        for i in range(len(grid) - 2, -1, -1):
            for j in range(len(grid[i]) - 2, -1, -1):
                grid[i][j] += min(grid[i][j + 1], grid[i + 1][j])
        
        
        return grid[0][0]

class Solution:
    def minPathSum2(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        prev = [float("inf")] * n
        prev[-1] = 0

        for row in range(m - 1, -1, -1):
            dp = [float("inf")] * n
            for col in range(n - 1, -1, -1):
                if col < n - 1:
                    dp[col] = min(dp[col], dp[col + 1])
                dp[col] = min(dp[col], prev[col]) + grid[row][col]
            prev = dp

        return prev[0]