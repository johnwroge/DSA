from typing import List, Tuple
import bisect

# =============================================================================
# RECTANGLE OVERLAP LINE SWEEP TEMPLATE
# =============================================================================

"""
LeetCode Problems that can be solved with this technique:
- 223. Rectangle Area
- 836. Rectangle Overlap
- 850. Rectangle Area II
- 391. Perfect Rectangle
- 302. Smallest Rectangle Enclosing Black Pixels
- 1024. Video Stitching (interval version)
- 1094. Car Pooling (1D version)
- 1546. Maximum Number of Non-Overlapping Subarrays
"""

def compute_area(ax1: int, ay1: int, ax2: int, ay2: int, 
                 bx1: int, by1: int, bx2: int, by2: int) -> int:
    """Compute total area covered by two rectangles"""
    area_a = (ax2 - ax1) * (ay2 - ay1)
    area_b = (bx2 - bx1) * (by2 - by1)
    
    # Calculate overlap
    overlap_width = max(0, min(ax2, bx2) - max(ax1, bx1))
    overlap_height = max(0, min(ay2, by2) - max(ay1, by1))
    overlap_area = overlap_width * overlap_height
    
    return area_a + area_b - overlap_area

def is_rectangle_overlap(rec1: List[int], rec2: List[int]) -> bool:
    """Check if two rectangles overlap"""
    x1, y1, x2, y2 = rec1
    x3, y3, x4, y4 = rec2
    
    # Check if they don't overlap
    if x2 <= x3 or x4 <= x1 or y2 <= y3 or y4 <= y1:
        return False
    
    return True

def rectangle_area_union(rectangles: List[List[int]]) -> int:
    """Calculate total area covered by union of rectangles using coordinate compression"""
    if not rectangles:
        return 0
    
    # Extract all unique x and y coordinates
    x_coords = set()
    y_coords = set()
    
    for x1, y1, x2, y2 in rectangles:
        x_coords.add(x1)
        x_coords.add(x2)
        y_coords.add(y1)
        y_coords.add(y2)
    
    x_sorted = sorted(x_coords)
    y_sorted = sorted(y_coords)
    
    # Create coordinate compression mappings
    x_map = {x: i for i, x in enumerate(x_sorted)}
    y_map = {y: i for i, y in enumerate(y_sorted)}
    
    # Mark covered areas in 2D grid
    covered = [[False] * (len(y_sorted) - 1) for _ in range(len(x_sorted) - 1)]
    
    for x1, y1, x2, y2 in rectangles:
        x1_idx, x2_idx = x_map[x1], x_map[x2]
        y1_idx, y2_idx = y_map[y1], y_map[y2]
        
        for i in range(x1_idx, x2_idx):
            for j in range(y1_idx, y2_idx):
                covered[i][j] = True
    
    # Calculate total area
    total_area = 0
    for i in range(len(x_sorted) - 1):
        for j in range(len(y_sorted) - 1):
            if covered[i][j]:
                width = x_sorted[i + 1] - x_sorted[i]
                height = y_sorted[j + 1] - y_sorted[j]
                total_area += width * height
    
    return total_area % (10**9 + 7)

def rectangle_area_line_sweep(rectangles: List[List[int]]) -> int:
    """Calculate rectangle union area using line sweep algorithm"""
    if not rectangles:
        return 0
    
    # Create events for vertical edges
    events = []
    for x1, y1, x2, y2 in rectangles:
        events.append((x1, y1, y2, 1))   # Opening edge
        events.append((x2, y1, y2, -1))  # Closing edge
    
    events.sort()
    
    def merge_intervals(intervals):
        """Merge overlapping intervals and return total length"""
        if not intervals:
            return 0
        
        intervals.sort()
        total = 0
        start, end = intervals[0]
        
        for s, e in intervals[1:]:
            if s <= end:
                end = max(end, e)
            else:
                total += end - start
                start, end = s, e
        
        total += end - start
        return total
    
    total_area = 0
    active_intervals = []
    prev_x = 0
    
    i = 0
    while i < len(events):
        curr_x = events[i][0]
        
        # Add area from previous sweep line
        if active_intervals and curr_x > prev_x:
            height = merge_intervals(active_intervals[:])
            total_area += (curr_x - prev_x) * height
        
        # Process all events at current x coordinate
        while i < len(events) and events[i][0] == curr_x:
            x, y1, y2, delta = events[i]
            if delta == 1:
                active_intervals.append((y1, y2))
            else:
                active_intervals.remove((y1, y2))
            i += 1
        
        prev_x = curr_x
    
    return total_area % (10**9 + 7)

def is_perfect_rectangle(rectangles: List[List[int]]) -> bool:
    """Check if rectangles form a perfect rectangle without gaps or overlaps"""
    if not rectangles:
        return False
    
    # Calculate expected area and corner coordinates
    min_x = min(rect[0] for rect in rectangles)
    min_y = min(rect[1] for rect in rectangles)
    max_x = max(rect[2] for rect in rectangles)
    max_y = max(rect[3] for rect in rectangles)
    
    expected_area = (max_x - min_x) * (max_y - min_y)
    
    # Calculate actual area and track corner points
    actual_area = 0
    corner_count = {}
    
    for x1, y1, x2, y2 in rectangles:
        actual_area += (x2 - x1) * (y2 - y1)
        
        # Track corner points (each interior point should appear even times)
        corners = [(x1, y1), (x1, y2), (x2, y1), (x2, y2)]
        for corner in corners:
            corner_count[corner] = corner_count.get(corner, 0) + 1
    
    # Check area
    if actual_area != expected_area:
        return False
    
    # Check corner points
    expected_corners = {(min_x, min_y), (min_x, max_y), (max_x, min_y), (max_x, max_y)}
    
    for corner, count in corner_count.items():
        if corner in expected_corners:
            if count != 1:  # Outer corners should appear exactly once
                return False
        else:
            if count % 2 != 0:  # Interior corners should appear even times
                return False
    
    # Check that all expected corners are present
    for corner in expected_corners:
        if corner not in corner_count:
            return False
    
    return True

def smallest_rectangle_enclosing_black_pixels(image: List[List[str]], x: int, y: int) -> int:
    """Find smallest rectangle enclosing all black pixels connected to given black pixel"""
    if not image or not image[0]:
        return 0
    
    m, n = len(image), len(image[0])
    
    def binary_search_left(low, high, check_func):
        while low < high:
            mid = (low + high) // 2
            if check_func(mid):
                high = mid
            else:
                low = mid + 1
        return low
    
    def binary_search_right(low, high, check_func):
        while low < high:
            mid = (low + high + 1) // 2
            if check_func(mid):
                low = mid
            else:
                high = mid - 1
        return low
    
    def has_black_in_row(row):
        return '1' in image[row]
    
    def has_black_in_col(col):
        return any(image[row][col] == '1' for row in range(m))
    
    # Find boundaries using binary search
    top = binary_search_left(0, x, has_black_in_row)
    bottom = binary_search_right(x, m - 1, has_black_in_row)
    left = binary_search_left(0, y, has_black_in_col)
    right = binary_search_right(y, n - 1, has_black_in_col)
    
    return (bottom - top + 1) * (right - left + 1)

def car_pooling(trips: List[List[int]], capacity: int) -> bool:
    """Check if car can complete all trips within capacity (1D line sweep)"""
    events = []
    
    for passengers, start, end in trips:
        events.append((start, passengers))   # Pick up passengers
        events.append((end, -passengers))    # Drop off passengers
    
    events.sort()
    
    current_passengers = 0
    for time, delta in events:
        current_passengers += delta
        if current_passengers > capacity:
            return False
    
    return True

def video_stitching(clips: List[List[int]], time: int) -> int:
    """Find minimum number of clips to cover [0, time] interval"""
    if not clips:
        return -1
    
    clips.sort()
    
    count = 0
    current_end = 0
    next_end = 0
    i = 0
    
    while current_end < time:
        # Find the clip that extends furthest from current position
        while i < len(clips) and clips[i][0] <= current_end:
            next_end = max(next_end, clips[i][1])
            i += 1
        
        if next_end <= current_end:
            return -1  # Cannot extend further
        
        count += 1
        current_end = next_end
    
    return count

# =============================================================================
# USAGE EXAMPLES
# =============================================================================

if __name__ == "__main__":
    # Test rectangle area
    print(f"Rectangle area: {compute_area(-3, 0, 3, 4, 0, -1, 9, 2)}")
    
    # Test rectangle overlap
    rec1, rec2 = [0, 0, 2, 2], [1, 1, 3, 3]
    print(f"Rectangles overlap: {is_rectangle_overlap(rec1, rec2)}")
    
    # Test rectangle union area
    rectangles = [[0, 0, 2, 2], [1, 0, 2, 3], [1, 0, 3, 1]]
    print(f"Union area: {rectangle_area_union(rectangles)}")
    
    # Test perfect rectangle
    perfect_rects = [[1, 1, 3, 3], [3, 1, 4, 2], [3, 2, 4, 4], [1, 3, 2, 4], [2, 3, 3, 4]]
    print(f"Perfect rectangle: {is_perfect_rectangle(perfect_rects)}")
    
    # Test car pooling
    trips = [[2, 1, 5], [3, 3, 7]]
    print(f"Car pooling possible: {car_pooling(trips, 4)}")