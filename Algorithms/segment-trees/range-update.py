"""
LeetCode Problems where Range Update Segment Tree with Lazy Propagation can be applied:

307. Range Sum Query - Mutable
308. Range Sum Query 2D - Mutable
370. Range Addition
598. Range Addition II
699. Falling Squares
715. Range Module
732. My Calendar III
1094. Car Pooling
1109. Corporate Flight Bookings
1589. Maximum Sum Obtained of Any Permutation
1674. Minimum Moves to Make Array Complementary
2179. Count Good Triplets in an Array
2407. Longest Increasing Subsequence II
"""

class LazySegmentTree:
    """
    Segment Tree with Lazy Propagation for efficient range updates
    
    Supports:
    - Range addition/assignment
    - Range sum/min/max queries
    - Lazy propagation for O(log n) range updates
    
    Time Complexity:
    - Build: O(n)
    - Range Update: O(log n)
    - Range Query: O(log n)
    
    Space Complexity: O(n)
    """
    
    def __init__(self, arr, operation='sum', update_type='add'):
        """
        Initialize lazy segment tree
        
        Args:
            arr: initial array
            operation: 'sum', 'min', 'max' for range queries
            update_type: 'add' for range addition, 'set' for range assignment
        """
        self.n = len(arr)
        self.operation = operation
        self.update_type = update_type
        
        # Tree arrays
        self.tree = [0] * (4 * self.n)
        self.lazy = [0] * (4 * self.n)
        self.has_lazy = [False] * (4 * self.n)
        
        # Identity values
        self.identity = self._get_identity()
        
        self._build(arr, 0, 0, self.n - 1)
    
    def _get_identity(self):
        """Get identity element for the operation"""
        if self.operation == 'sum':
            return 0
        elif self.operation == 'min':
            return float('inf')
        elif self.operation == 'max':
            return float('-inf')
        return 0
    
    def _combine(self, a, b):
        """Combine two values based on operation"""
        if self.operation == 'sum':
            return a + b
        elif self.operation == 'min':
            return min(a, b)
        elif self.operation == 'max':
            return max(a, b)
        return a + b
    
    def _apply_lazy(self, node, start, end, lazy_val):
        """Apply lazy update to a node"""
        if self.update_type == 'add':
            if self.operation == 'sum':
                self.tree[node] += lazy_val * (end - start + 1)
            else:  # min/max
                self.tree[node] += lazy_val
        elif self.update_type == 'set':
            if self.operation == 'sum':
                self.tree[node] = lazy_val * (end - start + 1)
            else:  # min/max
                self.tree[node] = lazy_val
    
    def _combine_lazy(self, old_lazy, new_lazy):
        """Combine two lazy values"""
        if self.update_type == 'add':
            return old_lazy + new_lazy
        elif self.update_type == 'set':
            return new_lazy  # Set operation overwrites
        return old_lazy + new_lazy
    
    def _push(self, node, start, end):
        """Push lazy updates down to children"""
        if not self.has_lazy[node]:
            return
        
        # Apply lazy update to current node
        self._apply_lazy(node, start, end, self.lazy[node])
        
        # Push to children if not leaf
        if start != end:
            # Left child
            if self.has_lazy[2 * node + 1]:
                self.lazy[2 * node + 1] = self._combine_lazy(
                    self.lazy[2 * node + 1], self.lazy[node]
                )
            else:
                self.lazy[2 * node + 1] = self.lazy[node]
                self.has_lazy[2 * node + 1] = True
            
            # Right child
            if self.has_lazy[2 * node + 2]:
                self.lazy[2 * node + 2] = self._combine_lazy(
                    self.lazy[2 * node + 2], self.lazy[node]
                )
            else:
                self.lazy[2 * node + 2] = self.lazy[node]
                self.has_lazy[2 * node + 2] = True
        
        # Clear current node's lazy value
        self.lazy[node] = 0
        self.has_lazy[node] = False
    
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
    
    def range_update(self, left, right, val):
        """Update range [left, right] with val"""
        self._range_update(0, 0, self.n - 1, left, right, val)
    
    def _range_update(self, node, start, end, left, right, val):
        """Range update helper function"""
        # Push any pending updates
        self._push(node, start, end)
        
        # No overlap
        if start > right or end < left:
            return
        
        # Complete overlap
        if start >= left and end <= right:
            self.lazy[node] = val
            self.has_lazy[node] = True
            self._push(node, start, end)
            return
        
        # Partial overlap
        mid = (start + end) // 2
        self._range_update(2 * node + 1, start, mid, left, right, val)
        self._range_update(2 * node + 2, mid + 1, end, left, right, val)
        
        # Update current node after children are updated
        self._push(2 * node + 1, start, mid)
        self._push(2 * node + 2, mid + 1, end)
        
        self.tree[node] = self._combine(
            self.tree[2 * node + 1], 
            self.tree[2 * node + 2]
        )
    
    def range_query(self, left, right):
        """Query range [left, right] inclusive"""
        return self._range_query(0, 0, self.n - 1, left, right)
    
    def _range_query(self, node, start, end, left, right):
        """Range query helper function"""
        # No overlap
        if start > right or end < left:
            return self.identity
        
        # Push any pending updates
        self._push(node, start, end)
        
        # Complete overlap
        if start >= left and end <= right:
            return self.tree[node]
        
        # Partial overlap
        mid = (start + end) // 2
        left_result = self._range_query(2 * node + 1, start, mid, left, right)
        right_result = self._range_query(2 * node + 2, mid + 1, end, left, right)
        
        return self._combine(left_result, right_result)

class RangeAddition:
    """
    LeetCode 370: Range Addition
    Apply multiple range updates and return final array
    """
    
    def getModifiedArray(self, length, updates):
        """
        Apply range updates efficiently using lazy segment tree
        """
        # Initialize with zeros
        arr = [0] * length
        seg_tree = LazySegmentTree(arr, 'sum', 'add')
        
        # Apply all updates
        for start, end, inc in updates:
            seg_tree.range_update(start, end, inc)
        
        # Extract final array
        result = []
        for i in range(length):
            result.append(seg_tree.range_query(i, i))
        
        return result

class RangeAdditionII:
    """
    LeetCode 598: Range Addition II
    Find maximum value after range updates
    """
    
    def maxCount(self, m, n, ops):
        """
        Find count of maximum elements after operations
        """
        if not ops:
            return m * n
        
        # The maximum value will be at the intersection of all operations
        min_row = min(op[0] for op in ops)
        min_col = min(op[1] for op in ops)
        
        return min_row * min_col

class CarPooling:
    """
    LeetCode 1094: Car Pooling
    Check if car can handle all passengers with given capacity
    """
    
    def carPooling(self, trips, capacity):
        """
        Use range updates to track passenger count at each location
        """
        # Find maximum location
        max_location = max(trip[2] for trip in trips)
        
        # Initialize difference array
        diff = [0] * (max_location + 2)
        
        # Apply range updates using difference array
        for passengers, start, end in trips:
            diff[start] += passengers
            diff[end] -= passengers
        
        # Check if capacity is ever exceeded
        current_passengers = 0
        for change in diff:
            current_passengers += change
            if current_passengers > capacity:
                return False
        
        return True

class CorporateFlightBookings:
    """
    LeetCode 1109: Corporate Flight Bookings
    Sum of bookings for each flight
    """
    
    def corpFlightBookings(self, bookings, n):
        """
        Use range addition to calculate total seats for each flight
        """
        result = [0] * n
        
        # Use difference array for efficient range updates
        diff = [0] * (n + 1)
        
        for first, last, seats in bookings:
            diff[first - 1] += seats  # Convert to 0-indexed
            diff[last] -= seats
        
        # Build final array from difference array
        current_sum = 0
        for i in range(n):
            current_sum += diff[i]
            result[i] = current_sum
        
        return result

class DynamicRangeSum:
    """
    Advanced lazy segment tree with both range updates and point queries
    """
    
    def __init__(self, n):
        self.lazy_tree = LazySegmentTree([0] * n, 'sum', 'add')
    
    def range_add(self, left, right, val):
        """Add val to all elements in range [left, right]"""
        self.lazy_tree.range_update(left, right, val)
    
    def point_query(self, idx):
        """Get value at specific index"""
        return self.lazy_tree.range_query(idx, idx)
    
    def range_sum(self, left, right):
        """Get sum of range [left, right]"""
        return self.lazy_tree.range_query(left, right)

class AdvancedLazySegmentTree:
    """
    More advanced lazy segment tree supporting multiple operations:
    - Range addition
    - Range assignment
    - Range min/max/sum queries
    """
    
    def __init__(self, arr):
        self.n = len(arr)
        self.tree_sum = [0] * (4 * self.n)
        self.tree_min = [0] * (4 * self.n)
        self.tree_max = [0] * (4 * self.n)
        
        # Lazy propagation arrays
        self.lazy_add = [0] * (4 * self.n)
        self.lazy_set = [None] * (4 * self.n)  # None means no set operation
        
        self._build(arr, 0, 0, self.n - 1)
    
    def _build(self, arr, node, start, end):
        if start == end:
            val = arr[start]
            self.tree_sum[node] = val
            self.tree_min[node] = val
            self.tree_max[node] = val
        else:
            mid = (start + end) // 2
            self._build(arr, 2 * node + 1, start, mid)
            self._build(arr, 2 * node + 2, mid + 1, end)
            
            self.tree_sum[node] = self.tree_sum[2 * node + 1] + self.tree_sum[2 * node + 2]
            self.tree_min[node] = min(self.tree_min[2 * node + 1], self.tree_min[2 * node + 2])
            self.tree_max[node] = max(self.tree_max[2 * node + 1], self.tree_max[2 * node + 2])
    
    def _push(self, node, start, end):
        """Push lazy updates to current node and children"""
        # Apply set operation first (if exists)
        if self.lazy_set[node] is not None:
            val = self.lazy_set[node]
            self.tree_sum[node] = val * (end - start + 1)
            self.tree_min[node] = val
            self.tree_max[node] = val
            
            if start != end:  # Not a leaf
                self.lazy_set[2 * node + 1] = val
                self.lazy_set[2 * node + 2] = val
                self.lazy_add[2 * node + 1] = 0
                self.lazy_add[2 * node + 2] = 0
            
            self.lazy_set[node] = None
            self.lazy_add[node] = 0
        
        # Apply add operation
        if self.lazy_add[node] != 0:
            val = self.lazy_add[node]
            self.tree_sum[node] += val * (end - start + 1)
            self.tree_min[node] += val
            self.tree_max[node] += val
            
            if start != end:  # Not a leaf
                if self.lazy_set[2 * node + 1] is not None:
                    self.lazy_set[2 * node + 1] += val
                else:
                    self.lazy_add[2 * node + 1] += val
                
                if self.lazy_set[2 * node + 2] is not None:
                    self.lazy_set[2 * node + 2] += val
                else:
                    self.lazy_add[2 * node + 2] += val
            
            self.lazy_add[node] = 0
    
    def range_add(self, left, right, val):
        """Add val to all elements in range [left, right]"""
        self._range_add(0, 0, self.n - 1, left, right, val)
    
    def _range_add(self, node, start, end, left, right, val):
        self._push(node, start, end)
        
        if start > right or end < left:
            return
        
        if start >= left and end <= right:
            self.lazy_add[node] += val
            self._push(node, start, end)
            return
        
        mid = (start + end) // 2
        self._range_add(2 * node + 1, start, mid, left, right, val)
        self._range_add(2 * node + 2, mid + 1, end, left, right, val)
        
        self._push(2 * node + 1, start, mid)
        self._push(2 * node + 2, mid + 1, end)
        
        self.tree_sum[node] = self.tree_sum[2 * node + 1] + self.tree_sum[2 * node + 2]
        self.tree_min[node] = min(self.tree_min[2 * node + 1], self.tree_min[2 * node + 2])
        self.tree_max[node] = max(self.tree_max[2 * node + 1], self.tree_max[2 * node + 2])
    
    def range_set(self, left, right, val):
        """Set all elements in range [left, right] to val"""
        self._range_set(0, 0, self.n - 1, left, right, val)
    
    def _range_set(self, node, start, end, left, right, val):
        self._push(node, start, end)
        
        if start > right or end < left:
            return
        
        if start >= left and end <= right:
            self.lazy_set[node] = val
            self.lazy_add[node] = 0
            self._push(node, start, end)
            return
        
        mid = (start + end) // 2
        self._range_set(2 * node + 1, start, mid, left, right, val)
        self._range_set(2 * node + 2, mid + 1, end, left, right, val)
        
        self._push(2 * node + 1, start, mid)
        self._push(2 * node + 2, mid + 1, end)
        
        self.tree_sum[node] = self.tree_sum[2 * node + 1] + self.tree_sum[2 * node + 2]
        self.tree_min[node] = min(self.tree_min[2 * node + 1], self.tree_min[2 * node + 2])
        self.tree_max[node] = max(self.tree_max[2 * node + 1], self.tree_max[2 * node + 2])
    
    def range_sum(self, left, right):
        """Get sum of range [left, right]"""
        return self._range_query(0, 0, self.n - 1, left, right, 'sum')
    
    def range_min(self, left, right):
        """Get minimum of range [left, right]"""
        return self._range_query(0, 0, self.n - 1, left, right, 'min')
    
    def range_max(self, left, right):
        """Get maximum of range [left, right]"""
        return self._range_query(0, 0, self.n - 1, left, right, 'max')
    
    def _range_query(self, node, start, end, left, right, query_type):
        if start > right or end < left:
            if query_type == 'sum':
                return 0
            elif query_type == 'min':
                return float('inf')
            elif query_type == 'max':
                return float('-inf')
        
        self._push(node, start, end)
        
        if start >= left and end <= right:
            if query_type == 'sum':
                return self.tree_sum[node]
            elif query_type == 'min':
                return self.tree_min[node]
            elif query_type == 'max':
                return self.tree_max[node]
        
        mid = (start + end) // 2
        left_result = self._range_query(2 * node + 1, start, mid, left, right, query_type)
        right_result = self._range_query(2 * node + 2, mid + 1, end, left, right, query_type)
        
        if query_type == 'sum':
            return left_result + right_result
        elif query_type == 'min':
            return min(left_result, right_result)
        elif query_type == 'max':
            return max(left_result, right_result)