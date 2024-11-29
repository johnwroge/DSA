'''
You are given a m x n matrix grid consisting of non-negative integers where grid[row][col]
represents the minimum time required to be able to visit the cell (row, col), which means
you can visit the cell (row, col) only when the time you visit it is greater than or
equal to grid[row][col].

You are standing in the top-left cell of the matrix in the 0th second, and you must move
to any adjacent cell in the four directions: up, down, left, and right. Each move you make takes 1 second.

Return the minimum time required in which you can visit the bottom-right cell of the matrix.
If you cannot visit the bottom-right cell, then return -1.


'''

import heapq
from typing import List


def minimumTime(grid: List[List[int]]) -> int:
    # If both initial moves require more than 1 second, impossible to proceed
    if grid[0][1] > 1 and grid[1][0] > 1:
        return -1

    rows, cols = len(grid), len(grid[0])
    # Possible movements: down, up, right, left
    directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
    visited = set()

    # Priority queue stores (time, row, col)
    # Ordered by minimum time to reach each cell
    pq = [(grid[0][0], 0, 0)]

    while pq:
        time, row, col = heapq.heappop(pq)

        # Check if reached target
        if (row, col) == (rows - 1, cols - 1):
            return time

        # Skip if cell already visited
        if (row, col) in visited:
            continue
        visited.add((row, col))

        # Try all four directions
        for dx, dy in directions:
            next_row, next_col = row + dx, col + dy

            if not _is_valid(visited, next_row, next_col, rows, cols):
                continue

            # Calculate the wait time needed to move to next cell
            wait_time = (
                1 if (grid[next_row][next_col] - time) % 2 == 0 else 0
            )
            next_time = max(grid[next_row][next_col] + wait_time, time + 1)
            heapq.heappush(pq, (next_time, next_row, next_col))

    return -1

# Checks if given cell coordinates are valid and unvisited
def _is_valid(visited, row, col, rows, cols):
    return 0 <= row < rows and 0 <= col < cols and (row, col) not in visited


grid = [[0,1,3,2],[5,1,2,5],[4,3,8,6]]
print(minimumTime(grid))