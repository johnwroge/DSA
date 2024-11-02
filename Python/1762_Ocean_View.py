'''
1762. Buildings With an Ocean View
Level
Medium

Description
There are n buildings in a line. You are given an integer array heights of size n that represents
the heights of the buildings in the line.

The ocean is to the right of the buildings. A building has an ocean view if the building can see the
ocean without obstructions. Formally, a building has an ocean view if all the buildings to its right
have a smaller height.

Return a list of indices (0-indexed) of buildings that have an ocean view, sorted in increasing order.

Example 1:

Input: heights = [4,2,3,1]
Output: [0,2,3]

Explanation: Building 1 (0-indexed) does not have an ocean view because building 2 is taller.

Example 2:

Input: heights = [4,3,2,1]
Output: [0,1,2,3]

Explanation: All the buildings have an ocean view.

Example 3:

Input: heights = [1,3,2,4]
Output: [3]

Explanation: Only building 3 has an ocean view.

Example 4:

Input: heights = [2,2,2,2]
Output: [3]

Explanation: Buildings cannot see the ocean if there are buildings of the same height to its right.

Constraints:

1 <= heights.length <= 10^5
1 <= heights[i] <= 10^9
'''


'''
solution: keep track of tallest building on right, as long as height is 
less than this point, we can add it to the result array. 
'''
from typing import List
class Solution:
    def findBuildings(self, heights: List[int]) -> List[int]:
        result = [len(heights) - 1]
        last = heights[result[-1]]
        for i in range(len(heights) - 2, -1, -1):
            if heights[i] > last:
                result.append(i)
            last = max(last, heights[i])
        return result[::-1]

# solution = Solution()
# print(solution.findBuildings([2,2,2,2]), '[3]')
# print(solution.findBuildings([1,3,2,4]), '[3]') 
# print(solution.findBuildings([4,2,3,1]), '[0,2,3]') 
# print(solution.findBuildings([4,3,2,1]), '[0,1,2,3]') 

# 2nd 
class Solution2
    def findBuildings(self, heights: List[int]) -> List[int]:
        ans = []
        mx = 0
        for i in range(len(heights) - 1, -1, -1):
            if heights[i] > mx:
                ans.append(i)
                mx = heights[i]
        return ans[::-1]