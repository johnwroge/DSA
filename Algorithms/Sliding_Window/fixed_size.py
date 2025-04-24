"""
LeetCode 643: Maximum Average Subarray I
LeetCode 1343: Number of Sub-arrays of Size K and Average Greater than or Equal to Threshold
LeetCode 567: Permutation in String
"""

def fixed_window(arr, k):
    # k is the window size
    n = len(arr)
    window_sum = sum(arr[:k])  # Initial window sum
    result = [window_sum]  # Store results
    
    # Slide the window
    for i in range(k, n):
        # Add new element and remove oldest element
        window_sum = window_sum + arr[i] - arr[i-k]
        result.append(window_sum)
    
    return result