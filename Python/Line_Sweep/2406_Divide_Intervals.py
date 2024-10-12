'''
You are given a 2D integer array intervals where intervals[i] = [lefti, righti] 
represents the inclusive interval [lefti, righti].

You have to divide the intervals into one or more groups such that each interval is 
in exactly one group, and no two intervals that are in the same group intersect each other.

Return the minimum number of groups you need to make.

Two intervals intersect if there is at least one common number between them. For
example, the intervals [1, 5] and [5, 8] intersect.

 

Example 1:

Input: intervals = [[5,10],[6,8],[1,5],[2,3],[1,10]]
Output: 3
Explanation: We can divide the intervals into the following groups:
- Group 1: [1, 5], [6, 8].
- Group 2: [2, 3], [5, 10].
- Group 3: [1, 10].
It can be proven that it is not possible to divide the intervals into fewer than 3 groups.
Example 2:

Input: intervals = [[1,3],[5,6],[8,10],[11,13]]
Output: 1
Explanation: None of the intervals overlap, so we can put all of them in one group.
 

Constraints:

1 <= intervals.length <= 105
intervals[i].length == 2
1 <= lefti <= righti <= 106


'''


class Solution:
    def minGroups(self, intervals: List[List[int]]) -> int:
        lines = {}
        for start, end in intervals:
            lines[start] = lines.get(start, 0) + 1
            lines[end + 1] = lines.get(end + 1, 0) - 1

        count = 0
        max_c = 0
        for k in sorted(lines.keys()):
            count += lines[k]
            max_c = max(count, max_c)
        return max_c
    

# LC Solutions

# Approach 1: Sorting or Priority Queue

class Solution:
    def minGroups(self, intervals: List[List[int]]) -> int:
        # Convert the intervals to two events
        # start as (start, 1) and end as (end + 1, -1)
        events = []

        for interval in intervals:
            events.append((interval[0], 1))  # Start event
            events.append((interval[1] + 1, -1))  # End event (interval[1] + 1)

        # Sort the events first by time, and then by type (1 for start, -1 for end).
        events.sort(key=lambda x: (x[0], x[1]))

        concurrent_intervals = 0
        max_concurrent_intervals = 0

        # Sweep through the events
        for event in events:
            concurrent_intervals += event[1]  # Track currently active intervals
            max_concurrent_intervals = max(
                max_concurrent_intervals, concurrent_intervals
            )  # Update max

        return max_concurrent_intervals



# Approach 2: Line Sweep Algorithm With Ordered Container

class Solution:
    def minGroups(self, intervals: List[List[int]]) -> int:
        # Use a dictionary to store the points and their counts
        point_to_count = defaultdict(int)

        # Mark the starting and ending points in the dictionary
        for interval in intervals:
            point_to_count[interval[0]] += 1  # Start of an interval
            point_to_count[
                interval[1] + 1
            ] -= 1  # End of an interval (interval[1] + 1)

        concurrent_intervals = 0
        max_concurrent_intervals = 0

        # Iterate over the sorted keys of the dictionary
        for point in sorted(point_to_count.keys()):
            concurrent_intervals += point_to_count[
                point
            ]  # Update currently active intervals
            max_concurrent_intervals = max(
                max_concurrent_intervals, concurrent_intervals
            )  # Update max intervals

        return max_concurrent_intervals

# Approach 3: Line Sweep Algorithm Without Ordered Container


class Solution:
    def minGroups(self, intervals: List[List[int]]) -> int:
        # Find the minimum and maximum value in the intervals
        range_start = float("inf")
        range_end = float("-inf")
        for interval in intervals:
            range_start = min(range_start, interval[0])
            range_end = max(range_end, interval[1])

        # Initialize the list with all zeroes
        point_to_count = [0] * (range_end + 2)
        for interval in intervals:
            point_to_count[
                interval[0]
            ] += 1  # Increment at the start of the interval
            point_to_count[
                interval[1] + 1
            ] -= 1  # Decrement right after the end of the interval

        concurrent_intervals = 0
        max_concurrent_intervals = 0
        for i in range(range_start, range_end + 1):
            # Update currently active intervals
            concurrent_intervals += point_to_count[i]
            max_concurrent_intervals = max(
                max_concurrent_intervals, concurrent_intervals
            )

        return max_concurrent_intervals