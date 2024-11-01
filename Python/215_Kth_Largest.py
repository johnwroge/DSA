'''
215. Kth Largest Element in an Array
Solved
Medium
Topics
Companies
Given an integer array nums and an integer k, return the kth largest element
 in the array.

Note that it is the kth largest element in the sorted order,
 not the kth distinct element.

Can you solve it without sorting?

 

Example 1:

Input: nums = [3,2,1,5,6,4], k = 2
Output: 5
Example 2:

Input: nums = [3,2,3,1,2,4,5,5,6], k = 4
Output: 4
 

Constraints:

1 <= k <= nums.length <= 105
-104 <= nums[i] <= 104

'''

# general solution with sorting

class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        nums.sort()
        curr = None
        for i in range(k):
            curr = nums.pop()
        return curr
import heapq
# with a heap
class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        nums = [-n for n in nums]
        heapq.heapify(nums)
        curr = None
        for i in range(k):
            curr = -1 * heapq.heappop(nums)
        return curr
        
        