"""
Activity Selection Problem Templates
Applicable LeetCode Problems:
- 435. Non-overlapping Intervals
- 452. Minimum Number of Arrows to Burst Balloons
- 646. Maximum Length of Pair Chain
- 1024. Video Stitching
- 1235. Maximum Profit in Job Scheduling (variant)
- 1353. Maximum Number of Events That Can Be Attended
"""

def activity_selection_greedy(activities):
    """
    Classic activity selection: select maximum number of non-overlapping activities
    activities: list of (start, end) tuples
    Time: O(n log n), Space: O(1)
    
    Greedy choice: always pick activity with earliest end time
    """
    if not activities:
        return []
    
    # Sort by end time
    activities.sort(key=lambda x: x[1])
    
    selected = [activities[0]]
    last_end_time = activities[0][1]
    
    for start, end in activities[1:]:
        if start >= last_end_time:  # No overlap
            selected.append((start, end))
            last_end_time = end
    
    return selected

def activity_selection_count(activities):
    """
    Return just the count of maximum non-overlapping activities
    Time: O(n log n), Space: O(1)
    """
    if not activities:
        return 0
    
    activities.sort(key=lambda x: x[1])
    
    count = 1
    last_end_time = activities[0][1]
    
    for start, end in activities[1:]:
        if start >= last_end_time:
            count += 1
            last_end_time = end
    
    return count

def min_intervals_to_remove(intervals):
    """
    LeetCode 435: Non-overlapping Intervals
    Find minimum number of intervals to remove to make rest non-overlapping
    """
    if not intervals:
        return 0
    
    intervals.sort(key=lambda x: x[1])  # Sort by end time
    
    count = 0
    last_end = intervals[0][1]
    
    for start, end in intervals[1:]:
        if start < last_end:  # Overlapping
            count += 1  # Remove current interval
        else:
            last_end = end  # Update last end time
    
    return count

def find_min_arrows(points):
    """
    LeetCode 452: Minimum Number of Arrows to Burst Balloons
    Find minimum arrows needed to burst all balloons
    """
    if not points:
        return 0
    
    points.sort(key=lambda x: x[1])  # Sort by end position
    
    arrows = 1
    arrow_position = points[0][1]
    
    for start, end in points[1:]:
        if start > arrow_position:  # Need new arrow
            arrows += 1
            arrow_position = end
    
    return arrows

def find_longest_chain(pairs):
    """
    LeetCode 646: Maximum Length of Pair Chain
    Find longest chain where pairs[i][1] < pairs[j][0]
    """
    if not pairs:
        return 0
    
    pairs.sort(key=lambda x: x[1])  # Sort by second element
    
    chain_length = 1
    last_end = pairs[0][1]
    
    for start, end in pairs[1:]:
        if start > last_end:  # Can extend chain
            chain_length += 1
            last_end = end
    
    return chain_length

def video_stitching(clips, time):
    """
    LeetCode 1024: Video Stitching
    Minimum number of clips to cover [0, time]
    """
    clips.sort()  # Sort by start time
    
    clip_count = 0
    current_end = 0
    i = 0
    
    while current_end < time:
        farthest = current_end
        
        # Find clip that starts before/at current_end and extends farthest
        while i < len(clips) and clips[i][0] <= current_end:
            farthest = max(farthest, clips[i][1])
            i += 1
        
        if farthest == current_end:  # No progress possible
            return -1
        
        clip_count += 1
        current_end = farthest
    
    return clip_count

def max_events_attend(events):
    """
    LeetCode 1353: Maximum Number of Events That Can Be Attended
    Maximum events that can be attended (each event lasts 1 day)
    """
    import heapq
    
    events.sort()  # Sort by start day
    
    min_heap = []  # Store end days of available events
    day = 1
    event_idx = 0
    attended = 0
    
    while event_idx < len(events) or min_heap:
        # Add all events that start today
        while event_idx < len(events) and events[event_idx][0] <= day:
            heapq.heappush(min_heap, events[event_idx][1])
            event_idx += 1
        
        # Remove events that have already ended
        while min_heap and min_heap[0] < day:
            heapq.heappop(min_heap)
        
        # Attend event with earliest end day
        if min_heap:
            heapq.heappop(min_heap)
            attended += 1
        
        day += 1
    
    return attended

def weighted_activity_selection(activities):
    """
    Weighted activity selection using dynamic programming approach
    activities: list of (start, end, weight) tuples
    Returns maximum weight of non-overlapping activities
    """
    if not activities:
        return 0
    
    # Sort by end time
    activities.sort(key=lambda x: x[1])
    n = len(activities)
    
    # dp[i] = maximum weight using activities 0 to i
    dp = [0] * n
    dp[0] = activities[0][2]
    
    def find_latest_non_overlapping(i):
        """Find latest activity that doesn't overlap with activity i"""
        for j in range(i - 1, -1, -1):
            if activities[j][1] <= activities[i][0]:
                return j
        return -1
    
    for i in range(1, n):
        # Include current activity
        include_weight = activities[i][2]
        latest_non_overlap = find_latest_non_overlapping(i)
        if latest_non_overlap != -1:
            include_weight += dp[latest_non_overlap]
        
        # Don't include current activity
        exclude_weight = dp[i - 1]
        
        dp[i] = max(include_weight, exclude_weight)
    
    return dp[n - 1]

def merge_intervals_greedy(intervals):
    """
    Merge overlapping intervals using greedy approach
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

def interval_intersection(list1, list2):
    """
    Find intersection of two lists of intervals
    """
    if not list1 or not list2:
        return []
    
    i = j = 0
    result = []
    
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