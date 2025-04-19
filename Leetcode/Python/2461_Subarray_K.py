'''

2461. Maximum Sum of Distinct Subarrays With Length K

You are given an integer array nums and an integer k. Find the maximum subarray sum of all the subarrays of nums that meet the following conditions:

The length of the subarray is k, and
All the elements of the subarray are distinct.
Return the maximum subarray sum of all the subarrays that meet the conditions. If no subarray meets the conditions, return 0.

A subarray is a contiguous non-empty sequence of elements within an array.

 

Example 1:

Input: nums = [1,5,4,2,9,9,9], k = 3
Output: 15
Explanation: The subarrays of nums with length 3 are:
- [1,5,4] which meets the requirements and has a sum of 10.
- [5,4,2] which meets the requirements and has a sum of 11.
- [4,2,9] which meets the requirements and has a sum of 15.
- [2,9,9] which does not meet the requirements because the element 9 is repeated.
- [9,9,9] which does not meet the requirements because the element 9 is repeated.
We return 15 because it is the maximum subarray sum of all the subarrays that meet the conditions
Example 2:

Input: nums = [4,4,4], k = 3
Output: 0
Explanation: The subarrays of nums with length 3 are:
- [4,4,4] which does not meet the requirements because the element 4 is repeated.
We return 0 because no subarrays meet the conditions.
 

Constraints:

1 <= k <= nums.length <= 105
1 <= nums[i] <= 105
'''


class Solution:
    def maximumSubarraySum(self, nums: List[int], k: int) -> int:

        mSum = float("-inf")
        window = set()
        cSum = 0
        L = 0
        
        for R in range(len(nums)):
            if nums[R] not in window:
                cSum += nums[R]
                window.add(nums[R])
            else:
                # Move left pointer forward to remove duplicates
                while nums[L] != nums[R]:
                    cSum -= nums[L]
                    window.remove(nums[L])
                    L += 1
                L += 1  # Skip the duplicate element
            
            # If the window size is k, update the max sum and shrink the window
            if len(window) == k:
                mSum = max(mSum, cSum)
                # Remove the left element from the window and adjust the sum
                cSum -= nums[L]
                window.remove(nums[L])
                L += 1
        
        return 0 if mSum == float("-inf") else mSum

class Solution:
    def maximumSubarraySum(self, nums: List[int], k: int) -> int:
        n = len(nums)
        mp = defaultdict(int)
        ws = 0
        max_sum = 0

        for i in range(n):
            # Add the current element to the window
            mp[nums[i]] += 1
            ws += nums[i]

            # If the window size exceeds 'k', slide the window
            if i >= k:
                le = nums[i - k]
                mp[le] -= 1
                ws -= le
                if mp[le] == 0:
                    del mp[le]

            # Check if the window has exactly 'k' distinct elements
            if i >= k - 1 and len(mp) == k:
                max_sum = max(max_sum, ws)

        return max_sum

class Solution:
    def maximumSubarraySum(self, nums: List[int], k: int) -> int:
        s = sum(nums[:k])
        d = {n: i for i, n in enumerate(nums[:k])}
        ms = s if len(d) == k else 0
        for i in range(k, len(nums)):
            s += nums[i] - nums[i-k]
            d[nums[i]] = i
            if d[nums[i-k]] == i-k:
                del d[nums[i-k]]
            ms = max(s, ms) if len(d) == k else ms

        return ms