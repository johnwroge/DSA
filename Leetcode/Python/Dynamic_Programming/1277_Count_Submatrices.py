
'''

1277. Count Square Submatrices with All Ones
Solved
Medium
Topics
Companies
Hint
Given a m * n matrix of ones and zeros, return how many square submatrices have all ones.

 

Example 1:

Input: matrix =
[
  [0,1,1,1],
  [1,1,1,1],
  [0,1,1,1]
]
Output: 15
Explanation: 
There are 10 squares of side 1.
There are 4 squares of side 2.
There is  1 square of side 3.
Total number of squares = 10 + 4 + 1 = 15.
Example 2:

Input: matrix = 
[
  [1,0,1],
  [1,1,0],
  [1,1,0]
]
Output: 7
Explanation: 
There are 6 squares of side 1.  
There is 1 square of side 2. 
Total number of squares = 6 + 1 = 7.
 

Constraints:

1 <= arr.length <= 300
1 <= arr[0].length <= 300
0 <= arr[i][j] <= 1
'''


# Solution Dynamic Programming

# Top Down DP T: O(row * col), S: O(row * col)

class Solution:
    def solve(self, i, j, grid, dp):
        # If the cell lies outside the grid, return 0.
        if i >= len(grid) or j >= len(grid[0]):
            return 0
        if grid[i][j] == 0:
            return 0
        # If we have already visited this cell, return the memoized value.
        if dp[i][j] != -1:
            return dp[i][j]
        # Find the answer for the cell to the right of the current cell.
        right = self.solve(i, j + 1, grid, dp)
        # Find the answer for the cell to the diagonal of the current cell.
        diagonal = self.solve(i + 1, j + 1, grid, dp)
        # Find the answer for the cell below the current cell.
        below = self.solve(i + 1, j, grid, dp)
        dp[i][j] = 1 + min(right, diagonal, below)
        return dp[i][j]

    def countSquares(self, matrix: List[List[int]]) -> int:
        ans = 0
        dp = [[-1 for _ in range(len(matrix[0]))] for _ in range(len(matrix))]
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                ans += self.solve(i, j, matrix, dp)
        return ans


# Bottom Up DP - Optimized T: O(row * col), S: O(row * col)

class Solution:
    def countSquares(self, matrix: List[List[int]]) -> int:
        row, col = len(matrix), len(matrix[0])
        dp = [[0] * (col + 1) for _ in range(row + 1)]
        ans = 0
        for i in range(row):
            for j in range(col):
                if matrix[i][j]:
                    dp[i + 1][j + 1] = (
                        min(dp[i][j + 1], dp[i + 1][j], dp[i][j]) + 1
                    )
                    ans += dp[i + 1][j + 1]
        return ans
        