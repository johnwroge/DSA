"""
LeetCode 11: Container With Most Water
LeetCode 42: Trapping Rain Water
LeetCode 845: Longest Mountain in Array
"""

def two_pointer_sliding_window(arr):
    n = len(arr)
    left = 0
    right = n - 1
    result = 0
    
    while left < right:
        # Calculate current value (like area, etc.)
        current = calculate_value(arr, left, right)
        result = max(result, current)
        
        # Move pointers based on strategy
        if arr[left] < arr[right]:
            left += 1
        else:
            right -= 1
    
    return result