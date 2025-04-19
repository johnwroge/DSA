'''
2684. Maximum Number of Moves in a Grid
Medium
Topics
Companies
Hint
You are given a 0-indexed m x n matrix grid consisting of positive integers.

You can start at any cell in the first column of the matrix, and traverse the grid in the following way:

From a cell (row, col), you can move to any of the cells: (row - 1, col + 1), (row, col + 1) and (row + 1, col + 1) such that the value of the cell you move to, should be strictly bigger than the value of the current cell.
Return the maximum number of moves that you can perform.

 

Example 1:


Input: grid = [[2,4,3,5],[5,4,9,3],[3,4,2,11],[10,9,13,15]]
Output: 3
Explanation: We can start at the cell (0, 0) and make the following moves:
- (0, 0) -> (0, 1).
- (0, 1) -> (1, 2).
- (1, 2) -> (2, 3).
It can be shown that it is the maximum number of moves that can be made.
Example 2:


Input: grid = [[3,2,4],[2,1,9],[1,1,7]]
Output: 0
Explanation: Starting from any cell in the first column we cannot perform any moves.
 

Constraints:

m == grid.length
n == grid[i].length
2 <= m, n <= 1000
4 <= m * n <= 105
1 <= grid[i][j] <= 106
'''

from typing import List

# dynamic programming solution

class Solution:
    def maxMoves(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        dp = [[0] * n for _ in range(m)]
        
        # Start from first column
        for i in range(m):
            dp[i][0] = 1  # Mark all starting positions as reachable
            
        # Process column by column
        for j in range(n-1):  # columns
            for i in range(m):  # rows
                if dp[i][j]:  # If we can reach this cell
                    # Try all three moves
                    for di in [-1, 0, 1]:
                        ni = i + di
                        nj = j + 1
                        if (0 <= ni < m and 
                            grid[ni][nj] > grid[i][j]):
                            dp[ni][nj] = 1
                            
        # Find rightmost reachable column
        for j in range(n-1, -1, -1):
            if any(dp[i][j] for i in range(m)):
                return j
        return 0

# Using BFS

class Solution:
    # The three possible directions for the next column.
    dirs = [-1, 0, 1]

    def maxMoves(self, grid):
        M, N = len(grid), len(grid[0])

        q = deque()
        vis = [[False] * N for _ in range(M)]

        # Enqueue the cells in the first column.
        for i in range(M):
            vis[i][0] = True
            q.append((i, 0, 0))

        max_moves = 0
        while q:
            sz = len(q)

            for _ in range(sz):
                row, col, count = q.popleft()

                # Update the maximum moves made so far.
                max_moves = max(max_moves, count)

                for dir in self.dirs:
                    # Next cell after the move.
                    new_row, new_col = row + dir, col + 1

                    # If the next cell isn't visited yet and is greater than
                    # the current cell value, add it to the queue with the
                    # incremented move count.
                    if (
                        0 <= new_row < M
                        and 0 <= new_col < N
                        and not vis[new_row][new_col]
                        and grid[row][col] < grid[new_row][new_col]
                    ):
                        vis[new_row][new_col] = True
                        q.append((new_row, new_col, count + 1))

        return max_moves


# Top down dynamic programming

class Solution:
    # The three possible directions for the next column.
    dirs = [-1, 0, 1]

    def DFS(self, row, col, grid, dp):
        M, N = len(grid), len(grid[0])

        # If we have already calculated the moves required for this cell, return the answer.
        if dp[row][col] != -1:
            return dp[row][col]

        max_moves = 0
        for dir in self.dirs:
            # Next cell after the move.
            new_row, new_col = row + dir, col + 1

            # If the next cell is valid and greater than the current cell value,
            # perform recursion to that cell with updated value of moves.
            if (
                0 <= new_row < M
                and 0 <= new_col < N
                and grid[row][col] < grid[new_row][new_col]
            ):
                max_moves = max(
                    max_moves, 1 + self.DFS(new_row, new_col, grid, dp)
                )

        dp[row][col] = max_moves
        return max_moves

    def maxMoves(self, grid):
        M, N = len(grid), len(grid[0])

        # Initialize the dp array with -1 indicating uncomputed cells.
        dp = [[-1] * N for _ in range(M)]

        max_moves = 0
        # Start DFS from each cell in the first column.
        for i in range(M):
            moves_required = self.DFS(i, 0, grid, dp)
            max_moves = max(max_moves, moves_required)

        return max_moves