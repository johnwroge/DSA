"""
LeetCode Problems where Largest Rectangle template can be applied:

84. Largest Rectangle in Histogram
85. Maximal Rectangle
1504. Count Submatrices With All Ones
1574. Shortest Subarray to be Removed to Make Array Sorted
1793. Maximum Score of a Good Subarray
907. Sum of Subarray Minimums (similar concept)
"""

def largestRectangleArea(heights):
    """
    Find the largest rectangle area in histogram using monotonic stack
    
    Time: O(n), Space: O(n)
    Key insight: For each bar, find the left and right boundaries where 
    the rectangle with this bar's height can extend
    """
    stack = []  # Store indices of heights in increasing order
    max_area = 0
    
    for i in range(len(heights)):
        # While current height is less than stack top height
        while stack and heights[i] < heights[stack[-1]]:
            # Pop the stack and calculate area with popped height as smallest
            h = heights[stack.pop()]
            # Width is from next smaller on left to next smaller on right
            w = i if not stack else i - stack[-1] - 1
            max_area = max(max_area, h * w)
        
        stack.append(i)
    
    # Process remaining bars in stack
    while stack:
        h = heights[stack.pop()]
        w = len(heights) if not stack else len(heights) - stack[-1] - 1
        max_area = max(max_area, h * w)
    
    return max_area

def largestRectangleArea_with_sentinels(heights):
    """
    Alternative approach using sentinel values to avoid edge cases
    """
    # Add sentinels: 0 at start and end
    heights = [0] + heights + [0]
    stack = []
    max_area = 0
    
    for i in range(len(heights)):
        while stack and heights[i] < heights[stack[-1]]:
            h = heights[stack.pop()]
            w = i - stack[-1] - 1
            max_area = max(max_area, h * w)
        stack.append(i)
    
    return max_area

def maximalRectangle(matrix):
    """
    LeetCode 85: Maximal Rectangle
    Convert 2D problem to multiple histogram problems
    """
    if not matrix or not matrix[0]:
        return 0
    
    rows, cols = len(matrix), len(matrix[0])
    heights = [0] * cols
    max_area = 0
    
    for row in matrix:
        # Update heights array
        for j in range(cols):
            if row[j] == '1':
                heights[j] += 1
            else:
                heights[j] = 0
        
        # Find largest rectangle in current histogram
        max_area = max(max_area, largestRectangleArea(heights))
    
    return max_area

def numSubmat(mat):
    """
    LeetCode 1504: Count Submatrices With All Ones
    Count all rectangles with all 1s
    """
    if not mat or not mat[0]:
        return 0
    
    rows, cols = len(mat), len(mat[0])
    heights = [0] * cols
    total = 0
    
    for row in mat:
        # Update heights
        for j in range(cols):
            if row[j] == 1:
                heights[j] += 1
            else:
                heights[j] = 0
        
        # Count rectangles in current histogram
        total += countRectanglesInHistogram(heights)
    
    return total

def countRectanglesInHistogram(heights):
    """
    Count all possible rectangles in histogram
    """
    stack = []
    total = 0
    
    for i in range(len(heights)):
        while stack and heights[i] < heights[stack[-1]]:
            h = heights[stack.pop()]
            w = i if not stack else i - stack[-1] - 1
            # Number of rectangles with height >= h
            total += h * w * (w + 1) // 2
        stack.append(i)
    
    while stack:
        h = heights[stack.pop()]
        w = len(heights) if not stack else len(heights) - stack[-1] - 1
        total += h * w * (w + 1) // 2
    
    return total

def maximumScore(nums, k):
    """
    LeetCode 1793: Maximum Score of a Good Subarray
    Find max score = min(subarray) * len(subarray) where subarray contains index k
    """
    n = len(nums)
    stack = []
    max_score = 0
    
    # Add sentinel
    nums.append(0)
    
    for i in range(n + 1):
        while stack and nums[i] < nums[stack[-1]]:
            h = nums[stack.pop()]
            w = i if not stack else i - stack[-1] - 1
            left = 0 if not stack else stack[-1] + 1
            right = i - 1
            
            # Check if subarray contains index k
            if left <= k <= right:
                max_score = max(max_score, h * w)
        
        stack.append(i)
    
    return max_score

# Template for any "find rectangle with property X" problem
def solve_rectangle_problem(heights, condition_func):
    """
    Generic template for rectangle problems with custom conditions
    
    Args:
        heights: list of heights
        condition_func: function that takes (height, width, left_idx, right_idx) 
                       and returns value to maximize
    """
    stack = []
    best_result = 0
    
    for i in range(len(heights)):
        while stack and heights[i] < heights[stack[-1]]:
            h = heights[stack.pop()]
            w = i if not stack else i - stack[-1] - 1
            left_idx = 0 if not stack else stack[-1] + 1
            right_idx = i - 1
            
            result = condition_func(h, w, left_idx, right_idx)
            best_result = max(best_result, result)
        
        stack.append(i)
    
    # Process remaining elements
    while stack:
        h = heights[stack.pop()]
        w = len(heights) if not stack else len(heights) - stack[-1] - 1
        left_idx = 0 if not stack else stack[-1] + 1
        right_idx = len(heights) - 1
        
        result = condition_func(h, w, left_idx, right_idx)
        best_result = max(best_result, result)
    
    return best_result