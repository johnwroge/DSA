
import math

'''
62. Unique Paths

There is a robot on an m x n grid. The robot is initially located at the top-left corner 
(i.e., grid[0][0]). The robot tries to move to the bottom-right corner (i.e., grid[m - 1][n - 1]).
 The robot can only move either down or right at any point in time.

Given the two integers m and n, return the number of possible unique paths that the robot can 
take to reach the bottom-right corner.

The test cases are generated so that the answer will be less than or equal to 2 * 109.
'''


def uniquePaths(m: int, n: int) -> int:
    row = [1] * n
    for i in range(m - 1):
        new_row = [1] * n
        for j in range(n - 2, -1, -1):
            new_row[j] = new_row[j + 1] + row[j]
        row = new_row
    return row[0]



def uniquePaths2(m, n):
    return math.comb(m + n - 2, m - 1)

print(uniquePaths2(3,2))