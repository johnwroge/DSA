'''

862. Shortest Subarray with Sum at Least K

Given an integer array nums and an integer k, return the length of the shortest non-empty
subarray of nums with a sum of at least k. If there is no such subarray, return -1.

A subarray is a contiguous part of an array.

 

Example 1:

Input: nums = [1], k = 1
Output: 1
Example 2:

Input: nums = [1,2], k = 4
Output: -1
Example 3:

Input: nums = [2,-1,2], k = 3
Output: 3
 

Constraints:

1 <= nums.length <= 105
-105 <= nums[i] <= 105
1 <= k <= 109
'''

class Solution:
    def decrypt(self, code: List[int], k: int) -> List[int]:
        n = len(code)  # O(1): Length of the list.
        
        if k == 0:
            return [0] * n  # O(n): Return a list of zeros if k is 0.

        result = [0] * n  # O(n): Initialize the result list.
        
        # Determine the direction of the sliding window.
        start, end, step = (1, k + 1, 1) if k > 0 else (k, 0, 1)
        window_sum = sum(code[i % n] for i in range(start, end))  # O(k): Initialize the first window sum.

        for i in range(n):  # O(n): Slide the window across all positions.
            result[i] = window_sum  # Store the current window sum in the result.
            # Slide the window: Remove the outgoing element and add the incoming one.
            window_sum -= code[(i + start) % n]  # O(1): Remove outgoing element.
            window_sum += code[(i + end) % n]    # O(1): Add incoming element.
        
        return result  # O(1): Return the result list.