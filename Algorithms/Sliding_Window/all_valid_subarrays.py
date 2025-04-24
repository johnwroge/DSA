"""
LeetCode 713: Subarray Product Less Than K
LeetCode 2461: Maximum Sum of Distinct Subarrays With Length K
LeetCode 1876: Substrings of Size Three with Distinct Characters
"""

def find_all_valid_subarrays(arr, k):
    left = 0
    result = []
    current_window = []
    
    for right in range(len(arr)):
        current_window.append(arr[right])
        
        # Adjust window size if needed
        while not is_valid_window(current_window, k):
            current_window.pop(0)
            left += 1
        
        # When we have a valid window, we can count subarrays
        if is_valid_window(current_window, k):
            # Store or count valid subarrays
            # For example, if any subarray ending at 'right' is valid:
            for start in range(left, right + 1):
                result.append(arr[start:right + 1])
    
    return result