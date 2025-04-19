
from collections import deque
from typing import List


def maxSubArray( nums: List[int]) -> int:
    total = nums[0]
    maxSum = float('-inf')
    for i in range(1, len(nums)):
        total = max(total + nums[i], nums[i])
        maxSum = max(maxSum, total)
    return maxSum


# print(maxSubArray([-2,1,-3,4,-1,2,1,-5,4]))



def canJump(nums: List[int]) -> bool:
    end = len(nums) - 1
    for i in range(end - 1, -1, -1):
        if i + nums[i] >= end:
            end = i
    return end == 0
   

# print(canJump([2,3,1,1,4]))
        
from typing import List

def jump(nums: List[int]) -> int:
    if len(nums) <= 1:
        return 0

    max_reach = nums[0]  # The farthest index you can reach with current jumps.
    steps = nums[0]      # Number of steps left to reach max_reach.
    jumps = 1           # Initial jump from the first position.

    for i in range(1, len(nums)):
        if i == len(nums) - 1:
            return jumps
        
        max_reach = max(max_reach, i + nums[i])
        steps -= 1
        
        if steps == 0:
            jumps += 1
            steps = max_reach - i

    return jumps

# Example usage:
nums = [2, 3, 1, 1, 4]
result = jump(nums)
# print(result)  # This should print 2


def jump2(nums: List[int]) -> int:
    furthest, curr, jumps = 0, 0, 0
    for i in range(len(nums) - 1):
        furthest = max(nums[i] + i, furthest)
        if i == curr:
            curr = furthest
            jumps += 1
    return jumps


# Example usage:
# nums2 = [2, 3, 1, 1, 4]
# result2 = jump2(nums)
# print(result2)  # This should print 2

    

def canCompleteCircuit(gas: List[int], cost: List[int]) -> int:
    Q = deque()
    for i in range(len(gas)):
        if gas[i] >= cost[i]:
            Q.append(i)

    for _ in range(len(Q)):
        index = Q.popleft()
        goal = index
        total = 0
        while total >= 0:
            total += gas[index] 
            total -= cost[index]
            if total < 0:
                break
            index += 1
            if index == len(gas):
                index = 0
            if index == goal:
                return goal
    return -1


print(canCompleteCircuit([2,3,4],[3,4,3]))

'''
Free code camp algos on YT
'''

# min

def bulbs(self, A):
    cost = 0

    for b in A:
        if cost % 2 == 0: b = b
        else: b = not b

        if b % 2 == 1: continue
        else: cost += 1

    return cost