'''
There is a party where n friends numbered from 0 to n - 1 are attending. There is an infinite number
 of chairs in this party that are numbered from 0 to infinity. When a friend arrives at the party, 
 they sit on the unoccupied chair with the smallest number.

For example, if chairs 0, 1, and 5 are occupied when a friend comes, they will sit on chair number 2.
When a friend leaves the party, their chair becomes unoccupied at the moment they leave. If another 
friend arrives at that same moment, they can sit in that chair.

You are given a 0-indexed 2D integer array times where times[i] = [arrivali, leavingi], indicating
 the arrival and leaving times of the ith friend respectively, and an integer targetFriend.
   All arrival times are distinct.

Return the chair number that the friend numbered targetFriend will sit on.

Input: times = [[1,4],[2,3],[4,6]], targetFriend = 1
Output: 1


Input: times = [[3,10],[1,5],[2,6]], targetFriend = 0
Output: 2

'''

from heapq import heappop,heappush
# Brute Force.

'''
Brute force approach is modeling the way this would occur in real life. The key is
to keep a list of occupied chairs initialized to 0 and comparing the arrival time 
to that chair list. IF the chair time is less than or equal to the arrival time, it's available.
we then just need to find the closest available seat in the chairs list. 
'''

def smallestChair(self, times: List[List[int]], targetFriend: int) -> int:
    target_time = times[targetFriend]
    times.sort()

    n = len(times)
    chair_time = [0] * n

    for time in times:
        for i in range(n):
            if chair_time[i] <= time[0]:
                chair_time[i] = time[1]
                if time == target_time:
                    return i
                break
    return 0


# Optimized with 2 Heaps

'''
Solution works by maintaining two min heaps. 1 Heap - `available` stores all of the available seats. 
We will pop from this heap to ensure we have the lowest seat number. The other heap `leaves times` stores
the latest departure time with the most recently available seat. If we find an arrival time that matches the target
time arrival we just return the soonest available. 

'''

def smallestChair(self, times: List[List[int]], target: int) -> int:
    # maintain to heaps 
    available, leave_times = list(range(len(times))), []
    # iterate over times in sorted order
    for arrival, leaving in sorted(times):
        # while the current leave time is less than the current arrival time
        # we push into the available seats the latest departure time
        while leave_times and leave_times[0][0] <= arrival:
            heappush(available, heappop(leave_times)[1])
        # if the current arrival is the target, we return the soonest available seat
        if arrival == times[target][0]: return available[0]
        # otherwise we push into leave times a tuple containing the current departure time and smallest
        # available seat
        heappush(leave_times, (leaving, heappop(available)))