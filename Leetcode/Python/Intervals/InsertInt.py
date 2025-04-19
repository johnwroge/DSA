from typing import List


class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        res = []
        for i in range(len(intervals)):
            if newInterval[1] < intervals[i][0]:
                print('first block')
                res.append(newInterval)
                return res + intervals[i:]
            elif newInterval[0] > intervals[i][1]:
                print('second')
                res.append(intervals[i])
            else:
                print('third')
                newInterval = [
                    min(newInterval[0], intervals[i][0]),
                    max(newInterval[1], intervals[i][1])
                ]
        res.append(newInterval)
        return res

# solution = Solution()    
# print(solution.insert([[1,3],[6,9]], [2,5]))

class Solution1:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort(key = lambda x: x[0])
        res = []
        current = intervals[0]
        for i in range(len(intervals)):
            if current[1] < intervals[i][0]:
                res.append(current)
                current = intervals[i]
            else:
                current = [
                    min(intervals[i][0], current[0]),
                    max(intervals[i][1], current[1])
                ]
        res.append(current)
        return res

solution1 = Solution1()
intervals = [[1,3],[2,6],[8,10],[15,18]]
# print(solution1.merge(intervals))

def eraseOverlapIntervals( intervals: List[List[int]]) -> int:
    intervals.sort(key=lambda x: x[1])
    
    prev, count = 0, 1
    # for i in range(1, len(intervals)):
    #     if intervals[prev][1] <= intervals[i][0]:
    #         prev = i 
    #         count += 1
    # return len(intervals) - count

# print(eraseOverlapIntervals([[1,2],[2,3],[3,4],[1,3]]))


def merge(intervals: List[List[int]]) -> List[List[int]]:
    intervals.sort(key=lambda x: x[0])
    res = []
    prev = intervals[0]
    for i in range(1, len(intervals)):
        print(prev[1], intervals[i][0])
        if prev[1] < intervals[i][0]:
            res.append(prev)
            prev = intervals[i]
        else:
            prev = [
                min(intervals[i][0], prev[0]),
                max(intervals[i][1], prev[1])
            ]
    res.append(prev)
    return res
print(merge([[1,3],[2,6],[8,10],[15,18]]))
