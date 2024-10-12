from typing import List


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


         
        
        
        
grid = [
  ["1","1","1","1","0"],
  ["1","1","0","1","0"],
  ["1","1","0","0","0"],
  ["0","0","0","0","0"]
]
solution = Solution()
print(solution.numIslands(grid))