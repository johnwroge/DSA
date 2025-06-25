"""
Interval Scheduling Problem Templates
Applicable LeetCode Problems:
- 56. Merge Intervals
- 57. Insert Interval
- 253. Meeting Rooms II
- 435. Non-overlapping Intervals
- 452. Minimum Number of Arrows to Burst Balloons
- 986. Interval List Intersections
- 1353. Maximum Number of Events That Can Be Attended
- 2402. Meeting Rooms III
"""

import heapq
from collections import defaultdict

def classic_interval_scheduling(intervals):
    """
    Classic interval scheduling: select maximum number of non-overlapping intervals
    Greedy choice: always pick interval with earliest end time
    Time: O(n log n), Space: O(1)
    """
    if not intervals:
        return []
    
    # Sort by end time (greedy choice)
    intervals.sort(key=lambda x: x[1])
    
    scheduled = [intervals[0]]
    last_end = intervals[0][1]
    
    for start, end in intervals[1:]:
        if start >= last_end:  # No overlap
            scheduled.append((start, end))
            last_end = end
    
    return scheduled

def weighted_interval_scheduling(intervals):
    """
    Weighted interval scheduling: maximize total weight of non-overlapping intervals
    intervals: list of (start, end, weight) tuples
    Time: O(n log n), Space: O(n)
    """
    if not intervals:
        return 0, []
    
    # Sort by end time
    intervals.sort(key=lambda x: x[1])
    n = len(intervals)
    
    # dp[i] = (max_weight, selected_intervals) ending at or before interval i
    dp = [(0, [])] * n
    dp[0] = (intervals[0][2], [intervals[0]])
    
    def latest_non_overlapping(i):
        """Binary search to find latest non-overlapping interval"""
        left, right = 0, i - 1
        result = -1
        
        while left <= right:
            mid = (left + right) // 2
            if intervals[mid][1] <= intervals[i][0]:
                result = mid
                left = mid + 1
            else:
                right = mid - 1
        
        return result
    
    for i in range(1, n):
        # Option 1: Don't include current interval
        exclude_weight, exclude_intervals = dp[i - 1]
        
        # Option 2: Include current interval
        include_weight = intervals[i][2]
        include_intervals = [intervals[i]]
        
        latest = latest_non_overlapping(i)
        if latest >= 0:
            include_weight += dp[latest][0]
            include_intervals = dp[latest][1] + include_intervals
        
        # Take the better option
        if include_weight > exclude_weight:
            dp[i] = (include_weight, include_intervals)
        else:
            dp[i] = (exclude_weight, exclude_intervals)
    
    return dp[n - 1]

def merge_intervals(intervals):
    """
    LeetCode 56: Merge Intervals
    Time: O(n log n), Space: O(1)
    """
    if not intervals:
        return []
    
    intervals.sort(key=lambda x: x[0])  # Sort by start time
    merged = [intervals[0]]
    
    for start, end in intervals[1:]:
        if start <= merged[-1][1]:  # Overlapping
            merged[-1] = (merged[-1][0], max(merged[-1][1], end))
        else:
            merged.append((start, end))
    
    return merged

def insert_interval(intervals, new_interval):
    """
    LeetCode 57: Insert Interval
    Time: O(n), Space: O(1)
    """
    result = []
    i = 0
    start, end = new_interval
    
    # Add all intervals ending before new interval starts
    while i < len(intervals) and intervals[i][1] < start:
        result.append(intervals[i])
        i += 1
    
    # Merge overlapping intervals
    while i < len(intervals) and intervals[i][0] <= end:
        start = min(start, intervals[i][0])
        end = max(end, intervals[i][1])
        i += 1
    
    result.append((start, end))
    
    # Add remaining intervals
    while i < len(intervals):
        result.append(intervals[i])
        i += 1
    
    return result

def min_meeting_rooms(intervals):
    """
    LeetCode 253: Meeting Rooms II
    Find minimum number of meeting rooms required
    Time: O(n log n), Space: O(n)
    """
    if not intervals:
        return 0
    
    # Separate start and end times
    starts = sorted([interval[0] for interval in intervals])
    ends = sorted([interval[1] for interval in intervals])
    
    rooms = 0
    max_rooms = 0
    start_ptr = end_ptr = 0
    
    while start_ptr < len(starts):
        if starts[start_ptr] < ends[end_ptr]:
            # Meeting starts, need a room
            rooms += 1
            max_rooms = max(max_rooms, rooms)
            start_ptr += 1
        else:
            # Meeting ends, free a room
            rooms -= 1
            end_ptr += 1
    
    return max_rooms

def min_meeting_rooms_heap(intervals):
    """
    Alternative solution using min heap
    Time: O(n log n), Space: O(n)
    """
    if not intervals:
        return 0
    
    intervals.sort(key=lambda x: x[0])  # Sort by start time
    heap = []  # Store end times of ongoing meetings
    
    for start, end in intervals:
        # Remove meetings that have ended
        while heap and heap[0] <= start:
            heapq.heappop(heap)
        
        # Add current meeting's end time
        heapq.heappush(heap, end)
    
    return len(heap)

def interval_intersections(list1, list2):
    """
    LeetCode 986: Interval List Intersections
    Time: O(m + n), Space: O(1)
    """
    result = []
    i = j = 0
    
    while i < len(list1) and j < len(list2):
        start1, end1 = list1[i]
        start2, end2 = list2[j]
        
        # Find intersection
        start = max(start1, start2)
        end = min(end1, end2)
        
        if start <= end:  # Valid intersection
            result.append((start, end))
        
        # Move pointer of interval that ends first
        if end1 < end2:
            i += 1
        else:
            j += 1
    
    return result

def can_attend_all_meetings(intervals):
    """
    Check if person can attend all meetings (no overlaps)
    Time: O(n log n), Space: O(1)
    """
    if not intervals:
        return True
    
    intervals.sort(key=lambda x: x[0])  # Sort by start time
    
    for i in range(1, len(intervals)):
        if intervals[i][0] < intervals[i-1][1]:  # Overlap
            return False
    
    return True

def max_events_one_day_each(events):
    """
    LeetCode 1353: Maximum Number of Events That Can Be Attended
    Each event can be attended on any day within its range
    Time: O(n log n), Space: O(n)
    """
    events.sort(key=lambda x: x[0])  # Sort by start day
    
    available_events = []  # Min heap of end days
    day = 1
    event_idx = 0
    attended = 0
    
    while event_idx < len(events) or available_events:
        # Add all events starting today or earlier
        while event_idx < len(events) and events[event_idx][0] <= day:
            heapq.heappush(available_events, events[event_idx][1])
            event_idx += 1
        
        # Remove expired events
        while available_events and available_events[0] < day:
            heapq.heappop(available_events)
        
        # Attend event with earliest end day
        if available_events:
            heapq.heappop(available_events)
            attended += 1
        
        day += 1
    
    return attended

def partition_labels(s):
    """
    LeetCode 763: Partition Labels (interval scheduling variant)
    Time: O(n), Space: O(1)
    """
    # Find last occurrence of each character
    last_occurrence = {char: i for i, char in enumerate(s)}
    
    partitions = []
    start = 0
    end = 0
    
    for i, char in enumerate(s):
        end = max(end, last_occurrence[char])
        
        if i == end:  # Reached end of current partition
            partitions.append(end - start + 1)
            start = i + 1
    
    return partitions

def scheduler_with_deadlines(tasks):
    """
    Schedule tasks with deadlines to minimize lateness
    tasks: list of (duration, deadline) tuples
    Greedy: sort by deadline (Earliest Deadline First)
    """
    if not tasks:
        return []
    
    # Sort by deadline
    indexed_tasks = [(tasks[i], i) for i in range(len(tasks))]
    indexed_tasks.sort(key=lambda x: x[0][1])
    
    schedule = []
    current_time = 0
    
    for (duration, deadline), original_idx in indexed_tasks:
        start_time = current_time
        finish_time = current_time + duration
        lateness = max(0, finish_time - deadline)
        
        schedule.append({
            'task_id': original_idx,
            'start': start_time,
            'finish': finish_time,
            'deadline': deadline,
            'lateness': lateness
        })
        
        current_time = finish_time
    
    return schedule

def resource_allocation_intervals(requests, resources):
    """
    Allocate resources to interval requests
    requests: list of (start, end, resource_type)
    resources: dict mapping resource_type to count
    """
    # Group requests by resource type
    by_resource = defaultdict(list)
    for start, end, resource_type in requests:
        by_resource[resource_type].append((start, end))
    
    allocated = []
    
    for resource_type, intervals in by_resource.items():
        if resource_type not in resources:
            continue
        
        # Sort intervals by end time for this resource
        intervals.sort(key=lambda x: x[1])
        
        # Greedy allocation
        available_resources = resources[resource_type]
        resource_end_times = [0] * available_resources
        
        for start, end in intervals:
            # Find earliest available resource
            earliest_idx = 0
            for i in range(1, available_resources):
                if resource_end_times[i] < resource_end_times[earliest_idx]:
                    earliest_idx = i
            
            # Check if resource is available
            if resource_end_times[earliest_idx] <= start:
                resource_end_times[earliest_idx] = end
                allocated.append((start, end, resource_type, earliest_idx))
    
    return allocated