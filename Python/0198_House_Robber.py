
'''

Code
Testcase
Test Result
Test Result
198. House Robber
Solved
Medium
Topics
Companies
You are a professional robber planning to rob houses along a street.
 Each house has a certain amount of money stashed, the only constraint 
 stopping you from robbing each of them is that adjacent houses have security
   systems connected and it will automatically contact the police if two adjacent 
   houses were broken into on the same night.

Given an integer array nums representing the amount of money of each house, return 
the maximum amount of money you can rob tonight without alerting the police.

 

Example 1:

Input: nums = [1,2,3,1]
Output: 4
Explanation: Rob house 1 (money = 1) and then rob house 3 (money = 3).
Total amount you can rob = 1 + 3 = 4.
Example 2:

Input: nums = [2,7,9,3,1]
Output: 12
Explanation: Rob house 1 (money = 2), rob house 3 (money = 9) and rob house 5 (money = 1).
Total amount you can rob = 2 + 9 + 1 = 12.
 

Constraints:

1 <= nums.length <= 100
0 <= nums[i] <= 400

'''
class Solution:
    # recursive top down without memo
    def rob(self, nums: List[int]) -> int:
        def helper(nums, i):
            if i < 0:
                return 0       
            return max(helper(nums, i - 2) + nums[i], helper(nums, i - 1))
        return helper(nums, len(nums) - 1)

    # recursive top down with memo
    def rob(self, nums: List[int]) -> int:
        memo = [-1] * len(nums)
        def helper(nums, i):
            if i < 0:
                return 0     
            if memo[i] >= 0:
                return memo[i]  
            result = max(helper(nums, i - 2) + nums[i], helper(nums, i - 1))
            memo[i] = result
            return result
        return helper(nums, len(nums) - 1)

    # iterative memo bottom up
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 0:
            return 0
        memo = [0] * (len(nums) + 1)
        memo[0] = 0
        memo[1] = nums[0]
        for i in range(1,len(nums)):
            val = nums[i]
            memo[i + 1] = max(memo[i], memo[i - 1] + val)
        return memo[len(nums)]

    # iterative plus two variables
    def rob(self, nums: List[int]) -> int:
        prev1 = 0
        prev2 = 0
        for num in nums:
            temp = max(num + prev1, prev2)
            prev1 = prev2
            prev2 = temp
        return prev2


   
# def find_max_sum(nums):
#     n = len(nums)
#     dp = [0] * (n + 2)  # Initialize dp array with 0s
#     for i in range(n - 1, -1, -1):
#         dp[i] = max(dp[i + 2] + nums[i], dp[i + 1])
#     return dp[0]

# # Example usage
# nums = [5, 1, 1, 5]
# result = find_max_sum(nums)
# print(result)  # Output: 10



# def find_max_sum(nums):
#     n = len(nums)
#     if n == 0:
#         return 0
#     if n == 1:
#         return nums[0]

#     dp = [0] * n
#     dp[0] = nums[0]
#     dp[1] = max(nums[0], nums[1])

#     for i in range(2, n):
#         dp[i] = max(dp[i - 1], dp[i - 2] + nums[i])

#     return dp[n - 1]

# print(find_max_sum([5, 1, 1, 5]))

# def find_max_sum(nums):
#     n = len(nums)
#     if n == 0:
#         return 0
#     if n == 1:
#         return nums[0]

#     incl = nums[0]
#     excl = 0
#     for i in range(1, n):
#         new_excl = max(incl, excl)
#         incl = excl + nums[i]
#         excl = new_excl

#     return max(incl, excl)
