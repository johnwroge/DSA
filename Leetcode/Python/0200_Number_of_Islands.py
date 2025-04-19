from typing import List


'''
200. Number of Islands

Given an m x n 2D binary grid grid which represents a map of '1's (land) and '0's (water), 
return the number of islands.

An island is surrounded by water and is formed by connecting adjacent lands horizontally or vertically.
 You may assume all four edges of the grid are all surrounded by water.

 

Example 1:

Input: grid = [
  ["1","1","1","1","0"],
  ["1","1","0","1","0"],
  ["1","1","0","0","0"],
  ["0","0","0","0","0"]
]
Output: 1
Example 2:

Input: grid = [
  ["1","1","0","0","0"],
  ["1","1","0","0","0"],
  ["0","0","1","0","0"],
  ["0","0","0","1","1"]
]
Output: 3
 

Constraints:

m == grid.length
n == grid[i].length
1 <= m, n <= 300
grid[i][j] is '0' or '1'.
'''


# DFS Solution
class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        count = 0
        visited = [[False] * len(grid[0]) for _ in range(len(grid))]
        
        for x in range(len(grid)):
            for y in range(len(grid[0])):
                
                if grid[x][y] == "1" and not visited[x][y]:
                    self.dfs(grid, visited, x, y)
                    count += 1
                          
        return count
    

    def dfs(self, grid, visited, x, y):
        
        if x < 0 or y < 0 or x >= len(grid) or y >= len(grid[0]) or grid[x][y] == "0" or visited[x][y]: 
            return 0
        if grid[x][y] == "1":
            visited[x][y] = True

            self.dfs(grid, visited, x + 1, y)  
            self.dfs(grid, visited, x - 1, y) 
            self.dfs(grid, visited, x, y + 1) 
            self.dfs(grid, visited, x, y - 1)


         
# With Stack

def numIslandsDFS(grid):
    if not grid:
        return 0

    rows, cols = len(grid), len(grid[0])
    visited = set()
    islands = 0

    for r in range(rows):
        for c in range(cols):
            if grid[r][c] == '1' and (r, c) not in visited:
                islands += 1
                # Initialize a stack with the current cell
                stack = [(r, c)]
                while stack:
                    curr_r, curr_c = stack.pop()
                    # Mark the cell as visited
                    visited.add((curr_r, curr_c))
                    # Explore neighbors (up, down, left, right)
                    for dr, dc in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
                        new_r, new_c = curr_r + dr, curr_c + dc
                        if 0 <= new_r < rows and 0 <= new_c < cols and grid[new_r][new_c] == '1' and (new_r, new_c) not in visited:
                            stack.append((new_r, new_c))  # Add the neighbor to the stack

    return islands

# Example usage:
grid = [
    ["1", "1", "0", "0", "0"],
    ["1", "1", "0", "0", "0"],
    ["0", "0", "1", "0", "0"],
    ["0", "0", "0", "1", "1"]
]

print(numIslandsDFS(grid))  # Output: 3

        
# BFS With Queue

from collections import deque

def numIslandsBFS(grid):
    if not grid:
        return 0

    rows, cols = len(grid), len(grid[0])
    visited = set()
    islands = 0

    def bfs(r, c):
        queue = deque([(r, c)])
        visited.add((r, c))
        while queue:
            curr_r, curr_c = queue.popleft()
            # Explore neighbors (up, down, left, right)
            for dr, dc in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
                new_r, new_c = curr_r + dr, curr_c + dc
                if 0 <= new_r < rows and 0 <= new_c < cols and grid[new_r][new_c] == '1' and (new_r, new_c) not in visited:
                    visited.add((new_r, new_c))
                    queue.append((new_r, new_c))

    for r in range(rows):
        for c in range(cols):
            if grid[r][c] == '1' and (r, c) not in visited:
                islands += 1
                bfs(r, c)

    return islands

# Example usage:
grid = [
    ["1", "1", "0", "0", "0"],
    ["1", "1", "0", "0", "0"],
    ["0", "0", "1", "0", "0"],
    ["0", "0", "0", "1", "1"]
]

print(numIslandsBFS(grid))  # Output: 3

        
        
grid = [
  ["1","1","1","1","0"],
  ["1","1","0","1","0"],
  ["1","1","0","0","0"],
  ["0","0","0","0","0"]
]
solution = Solution()
print(solution.numIslands(grid))