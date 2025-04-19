'''
207. Course Schedule

There are a total of numCourses courses you have to take, labeled from 0 to numCourses - 1.
 You are given an array prerequisites where prerequisites[i] = [ai, bi] indicates that you must 
 take course bi first if you want to take course ai.

For example, the pair [0, 1], indicates that to take course 0 you have to first take course 1.
Return true if you can finish all courses. Otherwise, return false.

 

Example 1:

Input: numCourses = 2, prerequisites = [[1,0]]
Output: true
Explanation: There are a total of 2 courses to take. 
To take course 1 you should have finished course 0. So it is possible.
Example 2:

Input: numCourses = 2, prerequisites = [[1,0],[0,1]]
Output: false
Explanation: There are a total of 2 courses to take. 
To take course 1 you should have finished course 0, and to take course 0 you 
should also have finished course 1. So it is impossible.
 

Constraints:

1 <= numCourses <= 2000
0 <= prerequisites.length <= 5000
prerequisites[i].length == 2
0 <= ai, bi < numCourses
All the pairs prerequisites[i] are unique.

'''

# Topological Sort Using Khan's Algorithm
from collections import defaultdict

class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        if not prerequisites:
            return True
        graph = defaultdict(list)
        downstream = [0] * numCourses
        courses = 0
        Q = []

        for second, first  in prerequisites:
            graph[first].append(second)
            graph[second].append(first)
            downstream[second] += 1
        
        for i in range(len(downstream)):
            if downstream[i] == 0:
                courses += 1
                Q.append(i)     
        
        while Q:
            val = Q.pop(0)
            graph[val]
            for ne in graph[val]:
                downstream[ne] -= 1
                if downstream[ne] == 0:
                    courses += 1
                    Q.append(ne)

        return numCourses == courses