class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        # create an adjacency list for each item in prerequisites, values in prerequisites will be from (0 -> numCourses - 1)
        prereq = { c:[] for c in range(numCourses) }
        # iterate over prerequisites and assign each 1st value in adjlist to second value
        for crs, pre in prerequisites:
            prereq[crs].append(pre)
        # create an empty list
        output = []
        # create two sets
        visit, cycle = set(), set()
        # create dfs helper function
        def dfs(crs):
            
            if crs in cycle:
                return False
            if crs in visit:
                return True

            cycle.add(crs)
            for pre in prereq[crs]:
                if dfs(pre) == False:
                    return False
            cycle.remove(crs)
            visit.add(crs)
            output.append(crs)
            return True
        for c in range(numCourses):
            if dfs(c) == False:
                return []
        return output