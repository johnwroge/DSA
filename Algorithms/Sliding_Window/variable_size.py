"""
LeetCode 209: Minimum Size Subarray Sum
LeetCode 76: Minimum Window Substring
LeetCode 1004: Max Consecutive Ones III
"""

def min_size_subarray_sum(arr, target):
    n = len(arr)
    left = 0
    current_sum = 0
    min_length = float('inf')
    
    for right in range(n):
        current_sum += arr[right]
        
        # Shrink window when condition is met
        while current_sum >= target:
            min_length = min(min_length, right - left + 1)
            current_sum -= arr[left]
            left += 1
    
    return min_length if min_length != float('inf') else 0