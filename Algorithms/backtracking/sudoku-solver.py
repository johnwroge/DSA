"""
Sudoku Solver - Backtracking

LeetCode #37: Sudoku Solver

Core pattern: Try placing digits 1-9 in empty cells, backtracking when no valid digit can be placed.
"""

def solve_sudoku(board):
    def is_valid(row, col, num):
        for x in range(9):
            if board[row][x] == num or board[x][col] == num:
                return False
        box_row, box_col = 3 * (row // 3), 3 * (col // 3)
        for i in range(box_row, box_row + 3):
            for j in range(box_col, box_col + 3):
                if board[i][j] == num:
                    return False
        return True
    
    def find_empty():
        for i in range(9):
            for j in range(9):
                if board[i][j] == '.':
                    return i, j
        return None
    
    def backtrack():
        empty_cell = find_empty()
        if not empty_cell:
            return True
        row, col = empty_cell
        for num in map(str, range(1, 10)):
            if is_valid(row, col, num):
                board[row][col] = num
                if backtrack():
                    return True
                board[row][col] = '.'
        return False
    
    return backtrack()

# Example usage
if __name__ == "__main__":
    sudoku_board = [
        ['5', '3', '.', '.', '7', '.', '.', '.', '.'],
        ['6', '.', '.', '1', '9', '5', '.', '.', '.'],
        ['.', '9', '8', '.', '.', '.', '.', '6', '.'],
        ['8', '.', '.', '.', '6', '.', '.', '.', '3'],
        ['4', '.', '.', '8', '.', '3', '.', '.', '1'],
        ['7', '.', '.', '.', '2', '.', '.', '.', '6'],
        ['.', '6', '.', '.', '.', '.', '2', '8', '.'],
        ['.', '.', '.', '4', '1', '9', '.', '.', '5'],
        ['.', '.', '.', '.', '8', '.', '.', '7', '9']
    ]
    print(solve_sudoku(sudoku_board))