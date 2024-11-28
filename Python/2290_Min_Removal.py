

from typing import List
from collections import deque


from typing import List
from heapq import heappush, heappop

def minimumObstacles(grid: List[List[int]]) -> int:
    rows, cols = len(grid), len(grid[0])
    directions = [(0, 1), (1, 0), (0, -1), (-1, 0)] 
    visited = set()
    pq = []  
    heappush(pq, (0, 0, 0))  

    while pq:
        rem, x, y = heappop(pq)

        if (x, y) in visited:
            continue
        visited.add((x, y))

        if x == rows - 1 and y == cols - 1:
            return rem

        for dx, dy in directions:
            nx, ny = x + dx, y + dy
            if 0 <= nx < rows and 0 <= ny < cols and (nx, ny) not in visited:
                heappush(pq, (rem + grid[nx][ny], nx, ny))

    return -1 

grid = [[0,1,1],[1,1,0],[1,1,0]]
print(minimumObstacles(grid))

        