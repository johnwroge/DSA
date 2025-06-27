"""
LeetCode Problems where Range Query Segment Tree can be applied:

307. Range Sum Query - Mutable
308. Range Sum Query 2D - Mutable
315. Count of Smaller Numbers After Self
327. Count of Range Sum
406. Queue Reconstruction by Height
493. Reverse Pairs
673. Number of Longest Increasing Subsequence
699. Falling Squares
715. Range Module
732. My Calendar III
1649. Create Sorted Array through Instructions
2213. Longest Substring of One Repeating Character
"""

class RangeQuerySegmentTree:
    """
    Generic Segment Tree for various range query operations
    
    Supports: sum, min, max, gcd, xor, and custom operations
    """
    
    def __init__(self, arr=None, size=None, operation='sum', default_value=None):
        """
        Initialize segment tree
        
        Args:
            arr: initial array (optional)
            size: size if creating empty tree
            operation: 'sum', 'min', 'max', 'gcd', 'xor', or custom function
            default_value: default value for empty ranges
        """
        if arr:
            self.n = len(arr)
        elif size:
            self.n = size
            arr = [0] * size
        else:
            raise ValueError("Must provide either arr or size")
        
        self.operation = operation
        self.tree = [0] * (4 * self.n)
        self.default_value = default_value or self._get_default_value()
        
        if arr:
            self._build(arr, 0, 0, self.n - 1)
    
    def _get_default_value(self):
        """Get default value for the operation"""
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
        if callable(self.operation):
            return self.operation(a, b)
        elif self.operation == 'sum':
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
        if left > right:
            return self.default_value
        return self._query(0, 0, self.n - 1, left, right)
    
    def _query(self, node, start, end, left, right):
        """Query helper function"""
        if right < start or end < left:
            return self.default_value
        
        if left <= start and end <= right:
            return self.tree[node]
        
        mid = (start + end) // 2
        left_result = self._query(2 * node + 1, start, mid, left, right)
        right_result = self._query(2 * node + 2, mid + 1, end, left, right)
        
        return self._combine(left_result, right_result)

class MultiOperationSegmentTree:
    """
    Segment Tree that maintains multiple values per node
    Example: (sum, min, max, count) for each range
    """
    
    def __init__(self, arr):
        self.n = len(arr)
        # Each node stores (sum, min, max, count)
        self.tree = [(0, float('inf'), float('-inf'), 0)] * (4 * self.n)
        
        if arr:
            self._build(arr, 0, 0, self.n - 1)
    
    def _combine(self, left_node, right_node):
        """Combine two nodes"""
        left_sum, left_min, left_max, left_count = left_node
        right_sum, right_min, right_max, right_count = right_node
        
        return (
            left_sum + right_sum,
            min(left_min, right_min),
            max(left_max, right_max),
            left_count + right_count
        )
    
    def _build(self, arr, node, start, end):
        """Build segment tree"""
        if start == end:
            val = arr[start]
            self.tree[node] = (val, val, val, 1)
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
        if start == end:
            self.tree[node] = (val, val, val, 1)
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
        """Query range [left, right] and return (sum, min, max, count)"""
        return self._query(0, 0, self.n - 1, left, right)
    
    def _query(self, node, start, end, left, right):
        if right < start or end < left:
            return (0, float('inf'), float('-inf'), 0)
        
        if left <= start and end <= right:
            return self.tree[node]
        
        mid = (start + end) // 2
        left_result = self._query(2 * node + 1, start, mid, left, right)
        right_result = self._query(2 * node + 2, mid + 1, end, left, right)
        
        return self._combine(left_result, right_result)

def longestRepeatingSubstring(s, queryCharacters, queryIndices):
    """
    LeetCode 2213: Longest Substring of One Repeating Character
    Handle character updates and find longest repeating substring
    """
    n = len(s)
    s = list(s)
    
    # Segment tree to track maximum length of repeating substring
    class RepeatingSegTree:
        def __init__(self, s):
            self.n = len(s)
            # Each node stores (left_char, left_len, right_char, right_len, max_len)
            self.tree = [('', 0, '', 0, 0)] * (4 * self.n)
            self.s = s
            self._build(0, 0, self.n - 1)
        
        def _combine(self, left_node, right_node):
            if left_node[4] == 0:  # Empty left
                return right_node
            if right_node[4] == 0:  # Empty right
                return left_node
            
            left_char, left_len, _, _, left_max = left_node
            _, _, right_char, right_len, right_max = right_node
            
            # Calculate new values
            new_left_char = left_char
            new_left_len = left_len
            new_right_char = right_char
            new_right_len = right_len
            new_max = max(left_max, right_max)
            
            # Check if middle characters match
            if left_node[2] == right_node[0]:  # right char of left == left char of right
                middle_len = left_node[3] + right_node[1]
                new_max = max(new_max, middle_len)
                
                # Update left length if entire left segment is same character
                if left_len == left_max and left_char == right_node[0]:
                    new_left_len = middle_len
                
                # Update right length if entire right segment is same character
                if right_len == right_max and right_char == left_node[2]:
                    new_right_len = middle_len
            
            return (new_left_char, new_left_len, new_right_char, new_right_len, new_max)
        
        def _build(self, node, start, end):
            if start == end:
                char = self.s[start]
                self.tree[node] = (char, 1, char, 1, 1)
            else:
                mid = (start + end) // 2
                self._build(2 * node + 1, start, mid)
                self._build(2 * node + 2, mid + 1, end)
                self.tree[node] = self._combine(
                    self.tree[2 * node + 1], 
                    self.tree[2 * node + 2]
                )
        
        def update(self, idx, char):
            self.s[idx] = char
            self._update(0, 0, self.n - 1, idx, char)
        
        def _update(self, node, start, end, idx, char):
            if start == end:
                self.tree[node] = (char, 1, char, 1, 1)
            else:
                mid = (start + end) // 2
                if idx <= mid:
                    self._update(2 * node + 1, start, mid, idx, char)
                else:
                    self._update(2 * node + 2, mid + 1, end, idx, char)
                
                self.tree[node] = self._combine(
                    self.tree[2 * node + 1], 
                    self.tree[2 * node + 2]
                )
        
        def query_max(self):
            return self.tree[0][4]
    
    seg_tree = RepeatingSegTree(s)
    result = []
    
    for i, char in enumerate(queryCharacters):
        idx = queryIndices[i]
        seg_tree.update(idx, char)
        result.append(seg_tree.query_max())
    
    return result

class RangeModeQuery:
    """
    Segment tree for range mode queries (most frequent element in range)
    """
    
    def __init__(self, arr):
        self.n = len(arr)
        self.arr = arr
        # Coordinate compression
        self.unique_vals = sorted(set(arr))
        self.val_to_idx = {v: i for i, v in enumerate(self.unique_vals)}
        
        # Each node stores frequency count for each unique value
        self.tree = [[0] * len(self.unique_vals) for _ in range(4 * self.n)]
        self._build(0, 0, self.n - 1)
    
    def _build(self, node, start, end):
        if start == end:
            val_idx = self.val_to_idx[self.arr[start]]
            self.tree[node][val_idx] = 1
        else:
            mid = (start + end) // 2
            self._build(2 * node + 1, start, mid)
            self._build(2 * node + 2, mid + 1, end)
            
            # Combine frequency counts
            for i in range(len(self.unique_vals)):
                self.tree[node][i] = (self.tree[2 * node + 1][i] + 
                                    self.tree[2 * node + 2][i])
    
    def query_mode(self, left, right):
        """Find mode (most frequent element) in range [left, right]"""
        freq = self._query(0, 0, self.n - 1, left, right)
        
        max_freq = max(freq)
        mode_idx = freq.index(max_freq)
        return self.unique_vals[mode_idx], max_freq
    
    def _query(self, node, start, end, left, right):
        if right < start or end < left:
            return [0] * len(self.unique_vals)
        
        if left <= start and end <= right:
            return self.tree[node][:]
        
        mid = (start + end) // 2
        left_freq = self._query(2 * node + 1, start, mid, left, right)
        right_freq = self._query(2 * node + 2, mid + 1, end, left, right)
        
        # Combine frequencies
        result = []
        for i in range(len(self.unique_vals)):
            result.append(left_freq[i] + right_freq[i])
        
        return result

# Template for coordinate compression with segment tree
def solve_with_coordinate_compression(arr, queries):
    """
    Template for problems requiring coordinate compression
    
    Args:
        arr: input array with potentially large values
        queries: list of queries
    """
    # Step 1: Coordinate compression
    all_values = set(arr)
    for query in queries:
        # Add query values to compression set
        pass
    
    sorted_values = sorted(all_values)
    compress = {v: i for i, v in enumerate(sorted_values)}
    
    # Step 2: Create segment tree with compressed coordinates
    compressed_arr = [compress[x] for x in arr]
    seg_tree = RangeQuerySegmentTree(compressed_arr)
    
    # Step 3: Process queries
    results = []
    for query in queries:
        # Process each query
        pass
    
    return results

# Persistent Segment Tree (for historical queries)
class PersistentSegmentTree:
    """
    Persistent Segment Tree - keeps all historical versions
    """
    
    def __init__(self, arr):
        self.n = len(arr)
        self.versions = []
        
        # Build initial version
        root = self._build(arr, 0, self.n - 1)
        self.versions.append(root)
    
    def _build(self, arr, start, end):
        node = {'start': start, 'end': end, 'sum': 0, 'left': None, 'right': None}
        
        if start == end:
            node['sum'] = arr[start]
        else:
            mid = (start + end) // 2
            node['left'] = self._build(arr, start, mid)
            node['right'] = self._build(arr, mid + 1, end)
            node['sum'] = node['left']['sum'] + node['right']['sum']
        
        return node
    
    def update(self, version, idx, val):
        """Create new version with updated value"""
        old_root = self.versions[version]
        new_root = self._update(old_root, idx, val)
        self.versions.append(new_root)
        return len(self.versions) - 1
    
    def _update(self, old_node, idx, val):
        start, end = old_node['start'], old_node['end']
        new_node = {'start': start, 'end': end, 'sum': 0, 'left': None, 'right': None}
        
        if start == end:
            new_node['sum'] = val
        else:
            mid = (start + end) // 2
            if idx <= mid:
                new_node['left'] = self._update(old_node['left'], idx, val)
                new_node['right'] = old_node['right']  # Reuse old right subtree
            else:
                new_node['left'] = old_node['left']  # Reuse old left subtree
                new_node['right'] = self._update(old_node['right'], idx, val)
            
            new_node['sum'] = new_node['left']['sum'] + new_node['right']['sum']
        
        return new_node
    
    def query(self, version, left, right):
        """Query range sum in specific version"""
        root = self.versions[version]
        return self._query(root, left, right)
    
    def _query(self, node, left, right):
        if right < node['start'] or node['end'] < left:
            return 0
        
        if left <= node['start'] and node['end'] <= right:
            return node['sum']
        
        return (self._query(node['left'], left, right) + 
                self._query(node['right'], left, right))