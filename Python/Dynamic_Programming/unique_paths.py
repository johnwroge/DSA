
import math


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