from typing import List, Tuple
import bisect

# =============================================================================
# POINT LOCATION LINE SWEEP TEMPLATE
# =============================================================================

"""
LeetCode Problems that can be solved with this technique:
- 252. Meeting Rooms
- 253. Meeting Rooms II
- 435. Non-overlapping Intervals
- 436. Find Right Interval
- 452. Minimum Number of Arrows to Burst Balloons
- 646. Maximum Length of Pair Chain
- 729. My Calendar I
- 731. My Calendar II
- 732. My Calendar III
- 1851. Minimum Interval to Include Each Query
- 2406. Divide Intervals Into Minimum Number of Groups
"""

def can_attend_meetings(intervals: List[List[int]]) -> bool:
    """Check if person can attend all meetings (no overlaps)"""
    if not intervals:
        return True
    
    # Sort by start time
    intervals.sort()
    
    for i in range(1, len(intervals)):
        if intervals[i][0] < intervals[i-1][1]:  # Current start < previous end
            return False
    
    return True

def min_meeting_rooms(intervals: List[List[int]]) -> int:
    """Find minimum number of meeting rooms needed using events approach"""
    if not intervals:
        return 0
    
    events = []
    for start, end in intervals:
        events.append((start, 1))    # Meeting starts (+1 room)
        events.append((end, -1))     # Meeting ends (-1 room)
    
    # Sort events: if same time, process end before start
    events.sort(key=lambda x: (x[0], x[1]))
    
    concurrent = 0
    max_rooms = 0
    
    for time, delta in events:
        concurrent += delta
        max_rooms = max(max_rooms, concurrent)
    
    return max_rooms

def min_meeting_rooms_heap(intervals: List[List[int]]) -> int:
    """Find minimum number of meeting rooms using heap approach"""
    import heapq
    
    if not intervals:
        return 0
    
    # Sort by start time
    intervals.sort()
    
    # Min heap to track end times of ongoing meetings
    heap = []
    
    for start, end in intervals:
        # Remove meetings that have ended
        while heap and heap[0] <= start:
            heapq.heappop(heap)
        
        # Add current meeting's end time
        heapq.heappush(heap, end)
    
    return len(heap)

def erase_overlap_intervals(intervals: List[List[int]]) -> int:
    """Find minimum number of intervals to remove to make non-overlapping"""
    if not intervals:
        return 0
    
    # Sort by end time (greedy: keep interval that ends earliest)
    intervals.sort(key=lambda x: x[1])
    
    count = 0
    end = intervals[0][1]
    
    for i in range(1, len(intervals)):
        if intervals[i][0] < end:  # Overlap found
            count += 1  # Remove current interval
        else:
            end = intervals[i][1]  # Update end time
    
    return count

def find_right_interval(intervals: List[List[int]]) -> List[int]:
    """Find right interval for each interval"""
    n = len(intervals)
    
    # Create list of (start_time, original_index)
    starts = [(intervals[i][0], i) for i in range(n)]
    starts.sort()
    
    result = [-1] * n
    
    for i, (start, end) in enumerate(intervals):
        # Binary search for first interval with start >= end
        left, right = 0, n
        while left < right:
            mid = (left + right) // 2
            if starts[mid][0] >= end:
                right = mid
            else:
                left = mid + 1
        
        if left < n:
            result[i] = starts[left][1]
    
    return result

class MyCalendar:
    """Calendar that prevents double booking"""
    
    def __init__(self):
        self.events = []
    
    def book(self, start: int, end: int) -> bool:
        # Check for overlap with existing events
        for s, e in self.events:
            if start < e and end > s:  # Overlap condition
                return False
        
        self.events.append((start, end))
        return True

class MyCalendarTwo:
    """Calendar that allows at most double booking"""
    
    def __init__(self):
        self.events = []
        self.overlaps = []
    
    def book(self, start: int, end: int) -> bool:
        # Check if this would create triple booking
        for s, e in self.overlaps:
            if start < e and end > s:
                return False
        
        # Add overlaps with existing events
        for s, e in self.events:
            if start < e and end > s:
                overlap_start = max(start, s)
                overlap_end = min(end, e)
                self.overlaps.append((overlap_start, overlap_end))
        
        self.events.append((start, end))
        return True

class MyCalendarThree:
    """Calendar that returns maximum k-booking"""
    
    def __init__(self):
        self.timeline = {}
    
    def book(self, start: int, end: int) -> int:
        # Add events to timeline
        self.timeline[start] = self.timeline.get(start, 0) + 1
        self.timeline[end] = self.timeline.get(end, 0) - 1
        
        # Calculate maximum concurrent bookings
        ongoing = 0
        max_bookings = 0
        
        for time in sorted(self.timeline.keys()):
            ongoing += self.timeline[time]
            max_bookings = max(max_bookings, ongoing)
        
        return max_bookings

def min_groups(intervals: List[List[int]]) -> int:
    """Divide intervals into minimum number of non-overlapping groups"""
    events = []
    
    for start, end in intervals:
        events.append((start, 1))    # Interval starts
        events.append((end + 1, -1)) # Interval ends (exclusive end)
    
    events.sort()
    
    concurrent = 0
    max_groups = 0
    
    for time, delta in events:
        concurrent += delta
        max_groups = max(max_groups, concurrent)
    
    return max_groups

def min_arrows(points: List[List[int]]) -> int:
    """Find minimum arrows to burst all balloons"""
    if not points:
        return 0
    
    # Sort by end position
    points.sort(key=lambda x: x[1])
    
    arrows = 1
    end = points[0][1]
    
    for i in range(1, len(points)):
        if points[i][0] > end:  # No overlap, need new arrow
            arrows += 1
            end = points[i][1]
    
    return arrows

def min_interval_to_include_queries(intervals: List[List[int]], queries: List[int]) -> List[int]:
    """Find minimum size interval that includes each query point"""
    import heapq
    
    # Sort intervals by start time
    intervals.sort()
    
    # Create query list with original indices
    indexed_queries = [(q, i) for i, q in enumerate(queries)]
    indexed_queries.sort()
    
    result = [-1] * len(queries)
    heap = []  # (size, end)
    interval_idx = 0
    
    for query, orig_idx in indexed_queries:
        # Add all intervals that start before or at query point
        while interval_idx < len(intervals) and intervals[interval_idx][0] <= query:
            start, end = intervals[interval_idx]
            heapq.heappush(heap, (end - start + 1, end))
            interval_idx += 1
        
        # Remove intervals that end before query point
        while heap and heap[0][1] < query:
            heapq.heappop(heap)
        
        # Get minimum size interval if exists
        if heap:
            result[orig_idx] = heap[0][0]
    
    return result

