"""
N-Queens - Backtracking

LeetCode #51: N-Queens
LeetCode #52: N-Queens II

Core pattern: Place queens one by one in different columns, checking for conflicts with previously placed queens.
"""

def solve_n_queens(n):
    def is_safe(row, col):
        for j in range(col):
            if board[row][j] == 'Q':
                return False
        for i, j in zip(range(row, -1, -1), range(col, -1, -1)):
            if board[i][j] == 'Q':
                return False
        for i, j in zip(range(row, n), range(col, -1, -1)):
            if board[i][j] == 'Q':
                return False
        return True
    
    def backtrack(col):
        if col == n:
            result.append([''.join(row) for row in board])
            return
        for row in range(n):
            if is_safe(row, col):
                board[row][col] = 'Q'
                backtrack(col + 1)
                board[row][col] = '.'
    
    result = []
    board = [['.' for _ in range(n)] for _ in range(n)]
    backtrack(0)
    return result

# Example usage
if __name__ == "__main__":
    n = 4
    solutions = solve_n_queens(n)
    print(f"Found {len(solutions)} solutions for {n}-Queens")