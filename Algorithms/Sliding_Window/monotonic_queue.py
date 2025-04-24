"""
LeetCode 239: Sliding Window Maximum
LeetCode 1438: Longest Continuous Subarray With Absolute Diff Less Than or Equal to Limit
LeetCode 862: Shortest Subarray with Sum at Least K
"""


from collections import deque

def sliding_window_with_monotonic_queue(nums, k):
    n = len(nums)
    result = []
    dq = deque()  # Monotonic queue (decreasing)
    
    for i in range(n):
        # Remove elements outside the current window
        while dq and dq[0] < i - k + 1:
            dq.popleft()
        
        # Remove elements smaller than current element from the end
        while dq and nums[dq[-1]] < nums[i]:
            dq.pop()
        
        # Add current index
        dq.append(i)
        
        # Get result (max/min in current window)
        if i >= k - 1:
            result.append(nums[dq[0]])
    
    return result