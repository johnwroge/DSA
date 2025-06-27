"""
LeetCode Problems where Point Update Segment Tree can be applied:

307. Range Sum Query - Mutable
308. Range Sum Query 2D - Mutable
315. Count of Smaller Numbers After Self
327. Count of Range Sum
699. Falling Squares
715. Range Module
732. My Calendar III
1488. Avoid Flood in The City
1622. Fancy Sequence
2286. Booking Concert Tickets in Groups
"""

class SegmentTree:
    """
    Segment Tree with Point Updates and Range Queries
    
    Time Complexity:
    - Build: O(n)
    - Update: O(log n)
    - Query: O(log n)
    
    Space Complexity: O(n)
    """
    
    def __init__(self, arr, operation='sum'):
        """
        Initialize segment tree from array
        
        Args:
            arr: initial array
            operation: 'sum', 'min', 'max', 'gcd', 'xor'
        """
        self.n = len(arr)
        self.operation = operation
        self.tree = [0] * (4 * self.n)
        self.identity = self._get_identity()
        
        if arr:
            self._build(arr, 0, 0, self.n - 1)
    
    def _get_identity(self):
        """Get identity element for the operation"""
        if self.operation == 'sum':
            return 0
        elif self.operation == 'min':
            return float('inf')
        elif self.operation == 'max':
            return float('-inf')
        elif self.operation == 'gcd':
            return 0
        elif self.operation == 'xor':
            return 0
        return 0
    
    def _combine(self, a, b):
        """Combine two values based on operation"""
        if self.operation == 'sum':
            return a + b
        elif self.operation == 'min':
            return min(a, b)
        elif self.operation == 'max':
            return max(a, b)
        elif self.operation == 'gcd':
            import math
            return math.gcd(a, b)
        elif self.operation == 'xor':
            return a ^ b
        return a + b
    
    def _build(self, arr, node, start, end):
        """Build segment tree recursively"""
        if start == end:
            self.tree[node] = arr[start]
        else:
            mid = (start + end) // 2
            self._build(arr, 2 * node + 1, start, mid)
            self._build(arr, 2 * node + 2, mid + 1, end)
            self.tree[node] = self._combine(
                self.tree[2 * node + 1], 
                self.tree[2 * node + 2]
            )
    
    def update(self, idx, val):
        """Update element at index idx to val"""
        self._update(0, 0, self.n - 1, idx, val)
    
    def _update(self, node, start, end, idx, val):
        """Update helper function"""
        if start == end:
            self.tree[node] = val
        else:
            mid = (start + end) // 2
            if idx <= mid:
                self._update(2 * node + 1, start, mid, idx, val)
            else:
                self._update(2 * node + 2, mid + 1, end, idx, val)
            
            self.tree[node] = self._combine(
                self.tree[2 * node + 1], 
                self.tree[2 * node + 2]
            )
    
    def query(self, left, right):
        """Query range [left, right] inclusive"""
        return self._query(0, 0, self.n - 1, left, right)
    
    def _query(self, node, start, end, left, right):
        """Query helper function"""
        if right < start or end < left:
            return self.identity
        
        if left <= start and end <= right:
            return self.tree[node]
        
        mid = (start + end) // 2
        left_result = self._query(2 * node + 1, start, mid, left, right)
        right_result = self._query(2 * node + 2, mid + 1, end, left, right)
        
        return self._combine(left_result, right_result)

class NumArray:
    """
    LeetCode 307: Range Sum Query - Mutable
    Support both point updates and range sum queries
    """
    
    def __init__(self, nums):
        self.seg_tree = SegmentTree(nums, 'sum')
    
    def update(self, index, val):
        """Update element at index to val"""
        self.seg_tree.update(index, val)
    
    def sumRange(self, left, right):
        """Return sum of elements from left to right"""
        return self.seg_tree.query(left, right)

class RangeModule:
    """
    LeetCode 715: Range Module
    Track ranges of integers and support add/remove/query operations
    """
    
    def __init__(self):
        self.ranges = []
    
    def addRange(self, left, right):
        """Add range [left, right)"""
        new_ranges = []
        i = 0
        
        # Add all ranges that end before new range starts
        while i < len(self.ranges) and self.ranges[i][1] < left:
            new_ranges.append(self.ranges[i])
            i += 1
        
        # Merge overlapping ranges
        while i < len(self.ranges) and self.ranges[i][0] <= right:
            left = min(left, self.ranges[i][0])
            right = max(right, self.ranges[i][1])
            i += 1
        
        new_ranges.append([left, right])
        
        # Add remaining ranges
        while i < len(self.ranges):
            new_ranges.append(self.ranges[i])
            i += 1
        
        self.ranges = new_ranges
    
    def queryRange(self, left, right):
        """Check if range [left, right) is tracked"""
        for start, end in self.ranges:
            if start <= left and right <= end:
                return True
        return False
    
    def removeRange(self, left, right):
        """Remove range [left, right)"""
        new_ranges = []
        
        for start, end in self.ranges:
            if end <= left or start >= right:
                # No overlap
                new_ranges.append([start, end])
            else:
                # Handle overlap
                if start < left:
                    new_ranges.append([start, left])
                if right < end:
                    new_ranges.append([right, end])
        
        self.ranges = new_ranges

class FallingSquares:
    """
    LeetCode 699: Falling Squares
    Track maximum height as squares fall
    """
    
    def __init__(self):
        self.coordinates = []
        self.heights = []
    
    def fallingSquares(self, positions):
        """
        Calculate height after each square falls
        """
        result = []
        max_height = 0
        
        for left, size in positions:
            right = left + size
            
            # Find maximum height in range [left, right)
            current_max = 0
            for i in range(len(self.coordinates)):
                coord_left, coord_right = self.coordinates[i]
                if not (coord_right <= left or coord_left >= right):
                    # Overlapping
                    current_max = max(current_max, self.heights[i])
            
            new_height = current_max + size
            
            # Remove intervals that are completely covered
            new_coordinates = []
            new_heights = []
            
            for i in range(len(self.coordinates)):
                coord_left, coord_right = self.coordinates[i]
                if coord_left >= right or coord_right <= left:
                    # No overlap
                    new_coordinates.append(self.coordinates[i])
                    new_heights.append(self.heights[i])
                else:
                    # Handle partial overlap
                    if coord_left < left:
                        new_coordinates.append((coord_left, left))
                        new_heights.append(self.heights[i])
                    if coord_right > right:
                        new_coordinates.append((right, coord_right))
                        new_heights.append(self.heights[i])
            
            # Add new interval
            new_coordinates.append((left, right))
            new_heights.append(new_height)
            
            self.coordinates = new_coordinates
            self.heights = new_heights
            
            max_height = max(max_height, new_height)
            result.append(max_height)
        
        return result

class MyCalendarThree:
    """
    LeetCode 732: My Calendar III
    Count maximum number of overlapping events
    """
    
    def __init__(self):
        self.events = {}
    
    def book(self, start, end):
        """Add event and return maximum overlapping count"""
        self.events[start] = self.events.get(start, 0) + 1
        self.events[end] = self.events.get(end, 0) - 1
        
        # Calculate maximum overlap
        max_overlap = 0
        current_overlap = 0
        
        for time in sorted(self.events.keys()):
            current_overlap += self.events[time]
            max_overlap = max(max_overlap, current_overlap)
        
        return max_overlap

# Segment Tree for finding kth smallest/largest element
class OrderStatisticTree:
    """
    Segment Tree that supports order statistics (kth smallest element)
    """
    
    def __init__(self, max_val):
        self.max_val = max_val
        self.tree = [0] * (4 * max_val)
    
    def update(self, idx, delta):
        """Add delta to count of element idx"""
        self._update(0, 0, self.max_val - 1, idx, delta)
    
    def _update(self, node, start, end, idx, delta):
        if start == end:
            self.tree[node] += delta
        else:
            mid = (start + end) // 2
            if idx <= mid:
                self._update(2 * node + 1, start, mid, idx, delta)
            else:
                self._update(2 * node + 2, mid + 1, end, idx, delta)
            
            self.tree[node] = self.tree[2 * node + 1] + self.tree[2 * node + 2]
    
    def kth_smallest(self, k):
        """Find kth smallest element (1-indexed)"""
        return self._kth_smallest(0, 0, self.max_val - 1, k)
    
    def _kth_smallest(self, node, start, end, k):
        if start == end:
            return start
        
        mid = (start + end) // 2
        left_count = self.tree[2 * node + 1]
        
        if k <= left_count:
            return self._kth_smallest(2 * node + 1, start, mid, k)
        else:
            return self._kth_smallest(2 * node + 2, mid + 1, end, k - left_count)
    
    def count_less_equal(self, val):
        """Count elements <= val"""
        if val < 0:
            return 0
        if val >= self.max_val:
            return self.tree[0]
        return self._query(0, 0, self.max_val - 1, 0, val)
    
    def _query(self, node, start, end, left, right):
        if right < start or end < left:
            return 0
        if left <= start and end <= right:
            return self.tree[node]
        
        mid = (start + end) // 2
        return (self._query(2 * node + 1, start, mid, left, right) +
                self._query(2 * node + 2, mid + 1, end, left, right))

# Template for dynamic programming with segment trees
class DPSegmentTree:
    """
    Segment tree optimized for DP transitions
    Example: dp[i] = max(dp[j] + score) for all valid j < i
    """
    
    def __init__(self, size):
        self.size = size
        self.tree = [float('-inf')] * (4 * size)
    
    def update(self, idx, val):
        """Update dp[idx] = max(dp[idx], val)"""
        self._update(0, 0, self.size - 1, idx, val)
    
    def _update(self, node, start, end, idx, val):
        if start == end:
            self.tree[node] = max(self.tree[node], val)
        else:
            mid = (start + end) // 2
            if idx <= mid:
                self._update(2 * node + 1, start, mid, idx, val)
            else:
                self._update(2 * node + 2, mid + 1, end, idx, val)
            
            self.tree[node] = max(self.tree[2 * node + 1], self.tree[2 * node + 2])
    
    def query_max(self, left, right):
        """Get maximum value in range [left, right]"""
        return self._query(0, 0, self.size - 1, left, right)
    
    def _query(self, node, start, end, left, right):
        if right < start or end < left:
            return float('-inf')
        if left <= start and end <= right:
            return self.tree[node]
        
        mid = (start + end) // 2
        return max(
            self._query(2 * node + 1, start, mid, left, right),
            self._query(2 * node + 2, mid + 1, end, left, right)
        )