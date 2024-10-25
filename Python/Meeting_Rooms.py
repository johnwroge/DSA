'''
Meeting Schedule II
Given an array of meeting time interval objects 
consisting of start and end times [[start_1,end_1],[start_2,end_2],...] 
(start_i < end_i), find the minimum number of days required to schedule all meetings without any conflicts.

Example 1:

Input: intervals = [(0,40),(5,10),(15,20)]

Output: 2
Explanation:
day1: (0,40)
day2: (5,10),(15,20)

Example 2:

Input: intervals = [(4,9)]

Output: 1
Note:

(0,8),(8,10) is not considered a conflict at 8
Constraints:

0 <= intervals.length <= 500
0 <= intervals[i].start < intervals[i].end <= 1,000,000


'''



# Line Sweep Algorithm

def minHalls(start, end) :
    # tasks_list = [[s,e] for s,e in zip(start, end)]
    prefix_sum = [0] * MAX
    n = len(start)

    for i in range(n) :
        prefix_sum[start[i]] += 1
        prefix_sum[end[i] + 1] -= 1
         
    ans = prefix_sum[0]

    for i in range(1, MAX) :
        prefix_sum[i] += prefix_sum[i - 1]
        ans = max(ans, prefix_sum[i])
    
    return ans; 


def minHalls2(lectures: List[List[int]], n: int) -> int:
    Time = []
    for i in range(n):
        Time.append((lectures[i][0], 1))
        Time.append((lectures[i][1], -1))
    Time.sort(key=lambda x: x[0])
    answer = 0
    sum = 0
    for i in range(len(Time)):
        sum += Time[i][1]
        answer = max(answer, sum)
    return answer


