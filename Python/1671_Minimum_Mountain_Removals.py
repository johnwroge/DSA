'''
1671. Minimum Number of Removals to Make Mountain Array
Hard
Topics
Companies
Hint
You may recall that an array arr is a mountain array if and only if:

arr.length >= 3
There exists some index i (0-indexed) with 0 < i < arr.length - 1 such that:
arr[0] < arr[1] < ... < arr[i - 1] < arr[i]
arr[i] > arr[i + 1] > ... > arr[arr.length - 1]
Given an integer array nums​​​, return the minimum number of elements to remove to
 make nums​​​ a mountain array.

 

Example 1:

Input: nums = [1,3,1]
Output: 0
Explanation: The array itself is a mountain array so we do not need to remove any
 elements.
Example 2:

Input: nums = [2,1,1,5,6,2,3,1]
Output: 3
Explanation: One solution is to remove the elements at indices 0, 1, and 5, making
 the array nums = [1,5,6,3,1].
 

Constraints:

3 <= nums.length <= 1000
1 <= nums[i] <= 109
It is guaranteed that you can make a mountain array out of nums.

To calculate the number of elements to remove:

On the left side of the peak, there are i + 1 elements from nums[0] to nums[i]. Therefore, the number of elements to remove on the left side is i + 1 - L1.
On the right side, there are N - i elements from nums[i] to nums[N - 1]. The number of elements to remove on the right side is N - i - L2.
Thus, the total number of elements to remove for a given peak at index i is:

removals=(i + 1 − L1) + (N − i − L2) = N + 1 − L1 − L2
'''

'''
Solution

Changing the question to instead find difference between the length of the 
array and the largest mountain length helps. 

One solution is to use dynamic programming performing two passes to compute the longest
increasing subsequence and longest decreasing subsequence. From these we can find max mountain length
and by adding them together at each index and subtracting 1. 


'''
class Solution:
    def minimumMountainRemovals(self, nums: List[int]) -> int:
        n = len(nums)
        LIS = [1] * n
        LDS = [1] * n

        # Compute LIS for each index
        for i in range(n):
            for j in range(i):
                if nums[i] > nums[j]:
                    LIS[i] = max(LIS[i], LIS[j] + 1)

        # Compute LDS from each index
        for i in range(n - 1, -1, -1):
            for j in range(n - 1, i, -1):
                if nums[i] > nums[j]:
                    LDS[i] = max(LDS[i], LDS[j] + 1)

        maxMountainLength = 0

        # Find the maximum mountain length
        for i in range(1, n - 1):
            if LIS[i] > 1 and LDS[i] > 1:  # Valid peak
                maxMountainLength = max(maxMountainLength, LIS[i] + LDS[i] - 1)

        return n - maxMountainLength








# solutions from leetcode

from typing import List
class Solution:
    def minimumMountainRemovals(self, nums: List[int]) -> int:
        N = len(nums)

        lis_length = [1] * N
        lds_length = [1] * N

        # Stores the length of longest increasing subsequence that ends at i.
        for i in range(N):
            for j in range(i):
                if nums[i] > nums[j]:
                    lis_length[i] = max(lis_length[i], lis_length[j] + 1)

        # Stores the length of longest decreasing subsequence that starts at i.
        for i in range(N - 1, -1, -1):
            for j in range(i + 1, N):
                if nums[i] > nums[j]:
                    lds_length[i] = max(lds_length[i], lds_length[j] + 1)

        min_removals = float("inf")
        for i in range(N):
            if lis_length[i] > 1 and lds_length[i] > 1:
                min_removals = min(
                    min_removals, N - lis_length[i] - lds_length[i] + 1
                )

        return min_removals

# Optimized Solution using Binary Search. 

class Solution:
    def getLongestIncreasingSubsequenceLength(self, v: List[int]) -> List[int]:
        lis_len = [1] * len(v)
        lis = [v[0]]

        for i in range(1, len(v)):
            index = self.lowerBound(lis, v[i])

            # Add to the list if v[i] is greater than the last element
            if index == len(lis):
                lis.append(v[i])
            else:
                # Replace the element at index with v[i]
                lis[index] = v[i]

            lis_len[i] = len(lis)

        return lis_len

    # Returns the index of the first element which is equal to or greater than target.
    def lowerBound(self, lis: List[int], target: int) -> int:
        left, right = 0, len(lis)
        while left < right:
            mid = left + (right - left) // 2
            if lis[mid] < target:
                left = mid + 1
            else:
                right = mid
        return left

    def minimumMountainRemovals(self, nums: List[int]) -> int:
        N = len(nums)

        lis_length = self.getLongestIncreasingSubsequenceLength(nums)

        nums.reverse()
        lds_length = self.getLongestIncreasingSubsequenceLength(nums)
        # Reverse the length array to correctly depict the length of longest decreasing subsequence for each index.
        lds_length.reverse()

        min_removals = float("inf")
        for i in range(N):
            if lis_length[i] > 1 and lds_length[i] > 1:
                min_removals = min(
                    min_removals, N - lis_length[i] - lds_length[i] + 1
                )

        return min_removals