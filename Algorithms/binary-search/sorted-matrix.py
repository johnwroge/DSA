"""
Binary Search on Sorted Matrix - Binary Search

LeetCode #74: Search a 2D Matrix
LeetCode #240: Search a 2D Matrix II

Core pattern: Convert 2D index to 1D or use row and column properties to eliminate search space.
"""

def search_matrix(matrix, target):
    if not matrix or not matrix[0]:
        return False
    
    rows, cols = len(matrix), len(matrix[0])
    left, right = 0, rows * cols - 1
    
    while left <= right:
        mid = left + (right - left) // 2
        
        # Convert 1D index to 2D coordinates
        row, col = divmod(mid, cols)
        mid_val = matrix[row][col]
        
        if mid_val == target:
            return True
        elif mid_val < target:
            left = mid + 1
        else:
            right = mid - 1
    
    return False

# Example usage
if __name__ == "__main__":
    matrix = [
        [1, 3, 5, 7],
        [10, 11, 16, 20],
        [23, 30, 34, 60]
    ]
    target = 3
    print(search_matrix(matrix, target))  # Output: True