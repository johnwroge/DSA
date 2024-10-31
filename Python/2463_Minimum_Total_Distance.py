'''
There are some robots and factories on the X-axis. You are given an integer array robot where robot[i]
 is the position of the ith robot. You are also given a 2D integer array factory where 
 factory[j] = [positionj, limitj] indicates that positionj is the position of the jth factory and that
   the jth factory can repair at most limitj robots.

The positions of each robot are unique. The positions of each factory are also unique. Note that a robot
 can be in the same position as a factory initially.

All the robots are initially broken; they keep moving in one direction. The direction could be the
 negative or the positive direction of the X-axis. When a robot reaches a factory that did not
   reach its limit, the factory repairs the robot, and it stops moving.

At any moment, you can set the initial direction of moving for some robot. Your target is to
 minimize the total distance traveled by all the robots.

Return the minimum total distance traveled by all the robots. 
The test cases are generated such that all the robots can be repaired.

Note that

All robots move at the same speed.
If two robots move in the same direction, they will never collide.
If two robots move in opposite directions and they meet at some point, they do not collide. They cross each other.
If a robot passes by a factory that reached its limits, it crosses it as if it does not exist.
If the robot moved from a position x to a position y, the distance it moved is |y - x|.
 

Example 1:


Input: robot = [0,4,6], factory = [[2,2],[6,2]]
Output: 4
Explanation: As shown in the figure:
- The first robot at position 0 moves in the positive direction. It will be repaired at the first factory.
- The second robot at position 4 moves in the negative direction. It will be repaired at the first factory.
- The third robot at position 6 will be repaired at the second factory. It does not need to move.
The limit of the first factory is 2, and it fixed 2 robots.
The limit of the second factory is 2, and it fixed 1 robot.
The total distance is |2 - 0| + |2 - 4| + |6 - 6| = 4. It can be shown that we cannot achieve a better total distance than 4.
Example 2:


Input: robot = [1,-1], factory = [[-2,1],[2,1]]
Output: 2
Explanation: As shown in the figure:
- The first robot at position 1 moves in the positive direction. It will be repaired at the second factory.
- The second robot at position -1 moves in the negative direction. It will be repaired at the first factory.
The limit of the first factory is 1, and it fixed 1 robot.
The limit of the second factory is 1, and it fixed 1 robot.
The total distance is |2 - 1| + |(-2) - (-1)| = 2. It can be shown that we cannot achieve a better total distance than 2.
 

Constraints:

1 <= robot.length, factory.length <= 100
factory[j].length == 2
-109 <= robot[i], positionj <= 109
0 <= limitj <= robot.length
The input will be generated such that it is always possible to repair every robot.
'''


'''
Solution


This is a dynamic programming problem because we have overlapping sub problems and we 
are looking for a globally optimal solution with multiple constraints. 

I tried a greedy approach at first, but this failed for this test case:
robot = [9,11,99,101]
factory = [[10,1],[7,1],[14,1],[100,1],[96,1],[103,1]]

In this test case, a greedy approach would initially assign the robots 9 and 11 to the nearest
factories at 10 and 7, respectively. However, this local optimization prevents the most efficient
placement of the robots at 99 and 101. The globally optimal solution requires leaving some closer
factories partially unused to enable a more efficient overall configuration for all robots.
By prematurely assigning the first two robots to their closest factories, a greedy algorithm
would likely increase the total distance for the remaining robots, missing the opportunity
to minimize the overall movement across all robots and factories.

From Claude:

The problem requires dynamic programming because a greedy approach fails to capture the
global optimization challenge. The complexity arises from simultaneous constraints: factor
y capacity limits, total distance minimization, and the requirement to place every robot. A
local, greedy strategy of assigning each robot to its nearest factory can catastrophically
suboptimal, as the placement of one robot dramatically impacts the potential placements
of subsequent robots. The interdependence of decisions, combined with the exponential
growth of possible configurations, means that the optimal solution cannot be determined
by making independent, locally optimal choices at each step. Essentially, the problem
demands a comprehensive exploration of all possible robot-to-factory assignments to
find the truly minimal total distance configuration.

'''


# recursive dp with memo 

class Solution:
    def minimumTotalDistance(self, robot: List[int], factory: List[List[int]]) -> int:
        # Sort robots and factories
        robot.sort()
        factory.sort()
        
        # Memoization to store computed results
        @cache
        def dp(i, j):
            # Base cases
            if i == len(robot):  # All robots placed
                return 0
            if j == len(factory):  # No more factories, but robots remain
                return float('inf')
            
            # Option 1: Skip this factory
            skip = dp(i, j + 1)
            
            # Option 2: Place robots in this factory
            take = 0
            count = 0
            for k in range(factory[j][1]):  # Respect factory capacity
                if i + k >= len(robot):
                    break
                
                # Calculate distance for this robot
                take += abs(robot[i + k] - factory[j][0])
                count += 1
                
                # Recursively place remaining robots
                sub = dp(i + k + 1, j + 1)
                
                # Update minimum total distance
                if sub != float('inf'):
                    skip = min(skip, take + sub)
            
            return skip
        
        # Return minimum total distance
        return dp(0, 0)
    
# optimal iterative bottom up DP

class Solution:
    def minimumTotalDistance(self, robot: List[int], factory: List[List[int]]) -> int:
        robot.sort()
        factory.sort()
        m, n = len(robot), len(factory)
        dp = [[0]*(n+1) for _ in range(m+1)] 
        for i in range(m): dp[i][-1] = inf 
        for j in range(n-1, -1, -1): 
            prefix = 0 
            qq = deque([(m, 0)])
            for i in range(m-1, -1, -1): 
                prefix += abs(robot[i] - factory[j][0])
                if qq[0][0] > i+factory[j][1]: qq.popleft()
                while qq and qq[-1][1] >= dp[i][j+1] - prefix: qq.pop()
                qq.append((i, dp[i][j+1] - prefix))
                dp[i][j] = qq[0][1] + prefix
        return dp[0][0]