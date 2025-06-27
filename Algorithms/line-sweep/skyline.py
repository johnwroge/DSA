from typing import List, Tuple
import heapq
from collections import defaultdict

# =============================================================================
# SKYLINE LINE SWEEP TEMPLATE
# =============================================================================

"""
LeetCode Problems that can be solved with this technique:
- 218. The Skyline Problem
- 699. Falling Squares
- 715. Range Module
- 732. My Calendar III
- 1109. Corporate Flight Bookings
- 1589. Maximum Sum of All Subarrays
- 2158. Amount of New Area Painted Each Day
- 2276. Count Integers in Intervals
"""

def get_skyline(buildings: List[List[int]]) -> List[List[int]]:
    """
    Generate skyline from building coordinates
    Each building: [left, right, height]
    """
    # Create events: (x, height, type) where type: 0=start, 1=end
    events = []
    for left, right, height in buildings:
        events.append((left, height, 0))   # Building starts
        events.append((right, height, 1)) # Building ends
    
    # Sort events: by x, then by type (start before end), then by height
    events.sort(key=lambda x: (x[0], x[2], -x[1] if x[2] == 0 else x[1]))
    
    result = []
    # Use max heap (negate heights for max heap behavior)
    active_heights = [0]  # Ground level
    
    i = 0
    while i < len(events):
        curr_x = events[i][0]
        
        # Process all events at current x coordinate
        while i < len(events) and events[i][0] == curr_x:
            x, height, event_type = events[i]
            
            if event_type == 0:  # Building starts
                active_heights.append(height)
            else:  # Building ends
                active_heights.remove(height)
            
            i += 1
        
        # Find current max height
        max_height = max(active_heights)
        
        # Add key point if height changed
        if not result or result[-1][1] != max_height:
            result.append([curr_x, max_height])
    
    return result

def get_skyline_optimized(buildings: List[List[int]]) -> List[List[int]]:
    """
    Optimized skyline using multiset simulation with counter
    """
    from collections import Counter
    
    events = []
    for left, right, height in buildings:
        events.append((left, height, 0))   # Start
        events.append((right, height, 1)) # End
    
    # Sort: x coordinate, then end before start, then height desc for start
    events.sort(key=lambda x: (x[0], x[2], -x[1] if x[2] == 0 else x[1]))
    
    result = []
    height_count = Counter([0])  # Ground level
    
    i = 0
    while i < len(events):
        curr_x = events[i][0]
        
        while i < len(events) and events[i][0] == curr_x:
            x, height, event_type = events[i]
            
            if event_type == 0:  # Building starts
                height_count[height] += 1
            else:  # Building ends
                height_count[height] -= 1
                if height_count[height] == 0:
                    del height_count[height]
            
            i += 1
        
        max_height = max(height_count.keys())
        
        if not result or result[-1][1] != max_height:
            result.append([curr_x, max_height])
    
    return result

def falling_squares(positions: List[List[int]]) -> List[int]:
    """
    Calculate height after each square falls and settles
    """
    intervals = []  # (left, right, height)
    result = []
    
    for left, side_length in positions:
        right = left + side_length
        base_height = 0
        
        # Find maximum height this square will land on
        for l, r, h in intervals:
            if left < r and right > l:  # Overlap check
                base_height = max(base_height, h)
        
        # New height of this square
        new_height = base_height + side_length
        
        # Remove intervals completely covered by new square
        intervals = [(l, r, h) for l, r, h in intervals 
                    if not (left <= l and r <= right)]
        
        # Add new square
        intervals.append((left, right, new_height))
        
        # Current maximum height
        result.append(max(h for _, _, h in intervals))
    
    return result

class RangeModule:
    """
    Track ranges and support range operations
    """
    
    def __init__(self):
        self.ranges = []  # List of [start, end) intervals
    
    def addRange(self, left: int, right: int) -> None:
        """Add range [left, right)"""
        new_ranges = []
        inserted = False
        
        for start, end in self.ranges:
            if end < left or start > right:
                # No overlap
                new_ranges.append([start, end])
            else:
                # Overlap - merge
                left = min(left, start)
                right = max(right, end)
        
        new_ranges.append([left, right])
        
        # Sort and merge adjacent ranges
        new_ranges.sort()
        merged = []
        
        for start, end in new_ranges:
            if merged and merged[-1][1] >= start:
                merged[-1][1] = max(merged[-1][1], end)
            else:
                merged.append([start, end])
        
        self.ranges = merged
    
    def queryRange(self, left: int, right: int) -> bool:
        """Check if range [left, right) is tracked"""
        for start, end in self.ranges:
            if start <= left and right <= end:
                return True
        return False
    
    def removeRange(self, left: int, right: int) -> None:
        """Remove range [left, right)"""
        new_ranges = []
        
        for start, end in self.ranges:
            if end <= left or start >= right:
                # No overlap
                new_ranges.append([start, end])
            else:
                # Overlap - split if necessary
                if start < left:
                    new_ranges.append([start, left])
                if right < end:
                    new_ranges.append([right, end])
        
        self.ranges = new_ranges

class CountIntervals:
    """
    Count integers covered by intervals
    """
    
    def __init__(self):
        self.intervals = []
        self.count = 0
    
    def add(self, left: int, right: int) -> None:
        """Add interval [left, right]"""
        new_intervals = []
        new_left, new_right = left, right
        
        for start, end in self.intervals:
            if end < left or start > right:
                # No overlap
                new_intervals.append((start, end))
            else:
                # Overlap - merge and subtract old count
                self.count -= end - start + 1
                new_left = min(new_left, start)
                new_right = max(new_right, end)
        
        new_intervals.append((new_left, new_right))
        self.count += new_right - new_left + 1
        self.intervals = new_intervals
    
    def count_intervals(self) -> int:
        """Return total count of covered integers"""
        return self.count

def corporate_flight_bookings(bookings: List[List[int]], n: int) -> List[int]:
    """
    Calculate total seats booked for each flight using difference array
    """
    diff = [0] * (n + 2)  # 1-indexed with buffer
    
    for first, last, seats in bookings:
        diff[first] += seats
        diff[last + 1] -= seats
    
    # Convert difference array to actual values
    result = []
    current = 0
    
    for i in range(1, n + 1):
        current += diff[i]
        result.append(current)
    
    return result

def amount_painted_each_day(paint: List[List[int]]) -> List[int]:
    """
    Calculate new area painted each day
    """
    painted_ranges = []
    result = []
    
    for start, end in paint:
        # Calculate how much of [start, end) is not already painted
        new_area = end - start
        
        for p_start, p_end in painted_ranges:
            # Calculate overlap with existing painted range
            overlap_start = max(start, p_start)
            overlap_end = min(end, p_end)
            
            if overlap_start < overlap_end:
                new_area -= overlap_end - overlap_start
        
        result.append(new_area)
        
        # Merge new range with existing ranges
        merged_ranges = []
        new_start, new_end = start, end
        
        for p_start, p_end in painted_ranges:
            if p_end < start or p_start > end:
                # No overlap
                merged_ranges.append((p_start, p_end))
            else:
                # Overlap - merge
                new_start = min(new_start, p_start)
                new_end = max(new_end, p_end)
        
        merged_ranges.append((new_start, new_end))
        painted_ranges = merged_ranges
    
    return result

def maximum_height_skyline(buildings: List[List[int]]) -> int:
    """
    Find maximum height in skyline
    """
    if not buildings:
        return 0
    
    skyline = get_skyline(buildings)
    return max(height for x, height in skyline)

def skyline_area(buildings: List[List[int]]) -> int:
    """
    Calculate total area under skyline
    """
    skyline = get_skyline(buildings)
    
    total_area = 0
    for i in range(len(skyline) - 1):
        x1, h1 = skyline[i]
        x2, h2 = skyline[i + 1]
        total_area += h1 * (x2 - x1)
    
    return total_area

# =============================================================================
# USAGE EXAMPLES
# =============================================================================

if __name__ == "__main__":
    # Test skyline
    buildings = [[2, 9, 10], [3, 7, 15], [5, 12, 12], [15, 20, 10], [19, 24, 8]]
    skyline = get_skyline(buildings)
    print(f"Skyline: {skyline}")
    
    # Test falling squares
    positions = [[1, 2], [2, 3], [6, 1]]
    heights = falling_squares(positions)
    print(f"Falling squares heights: {heights}")
    
    # Test range module
    rm = RangeModule()
    rm.addRange(10, 20)
    rm.removeRange(14, 16)
    print(f"Query [10, 14): {rm.queryRange(10, 14)}")
    print(f"Query [13, 15): {rm.queryRange(13, 15)}")
    
    # Test corporate flight bookings
    bookings = [[1, 2, 10], [2, 3, 20], [2, 5, 25]]
    n = 5
    seats = corporate_flight_bookings(bookings, n)
    print(f"Flight bookings: {seats}")
    
    # Test painted area
    paint_jobs = [[1, 4], [4, 7], [5, 8]]
    painted = amount_painted_each_day(paint_jobs)
    print(f"Area painted each day: {painted}")