"""
LeetCode Problems where Fenwick Tree (Binary Indexed Tree) can be applied:

307. Range Sum Query - Mutable
315. Count of Smaller Numbers After Self
327. Count of Range Sum
493. Reverse Pairs
1395. Count Number of Teams
1409. Queries on a Permutation With Key
1649. Create Sorted Array through Instructions
2179. Count Good Triplets in an Array
2321. Maximum Score Of Spliced Array
"""

class FenwickTree:
    """
    Fenwick Tree (Binary Indexed Tree) for efficient prefix sum queries and point updates
    
    Time Complexity:
    - Update: O(log n)
    - Query: O(log n)
    - Build: O(n log n)
    
    Space Complexity: O(n)
    """
    
    def __init__(self, n):
        """Initialize Fenwick tree with size n (1-indexed)"""
        self.size = n
        self.tree = [0] * (n + 1)
    
    def update(self, idx, delta):
        """Add delta to element at index idx (1-indexed)"""
        while idx <= self.size:
            self.tree[idx] += delta
            idx += idx & (-idx)  # Add last set bit
    
    def query(self, idx):
        """Get prefix sum from 1 to idx (inclusive, 1-indexed)"""
        result = 0
        while idx > 0:
            result += self.tree[idx]
            idx -= idx & (-idx)  # Remove last set bit
        return result
    
    def range_query(self, left, right):
        """Get sum from left to right (inclusive, 1-indexed)"""
        return self.query(right) - self.query(left - 1)

class FenwickTreeFromArray:
    """
    Fenwick Tree initialized from an existing array
    """
    
    def __init__(self, arr):
        """Initialize from 0-indexed array"""
        self.size = len(arr)
        self.tree = [0] * (self.size + 1)
        
        # Build tree efficiently
        for i in range(self.size):
            self.update(i + 1, arr[i])
    
    def update(self, idx, delta):
        """Add delta to element at 0-indexed position"""
        idx += 1  # Convert to 1-indexed
        while idx <= self.size:
            self.tree[idx] += delta
            idx += idx & (-idx)
    
    def query(self, idx):
        """Get prefix sum from 0 to idx (inclusive, 0-indexed)"""
        idx += 1  # Convert to 1-indexed
        result = 0
        while idx > 0:
            result += self.tree[idx]
            idx -= idx & (-idx)
        return result
    
    def range_query(self, left, right):
        """Get sum from left to right (inclusive, 0-indexed)"""
        if left == 0:
            return self.query(right)
        return self.query(right) - self.query(left - 1)

def numTeams(rating):
    """
    LeetCode 1395: Count Number of Teams
    Count triplets where rating[i] < rating[j] < rating[k] (i < j < k)
    """
    n = len(rating)
    
    # Coordinate compression
    sorted_ratings = sorted(set(rating))
    rank = {v: i + 1 for i, v in enumerate(sorted_ratings)}
    
    # Count ascending teams
    fenwick = FenwickTree(len(sorted_ratings))
    smaller_left = [0] * n
    
    # Count smaller elements to the left
    for i in range(n):
        smaller_left[i] = fenwick.query(rank[rating[i]] - 1)
        fenwick.update(rank[rating[i]], 1)
    
    # Count larger elements to the right
    fenwick = FenwickTree(len(sorted_ratings))
    ascending_teams = 0
    
    for i in range(n - 1, -1, -1):
        larger_right = fenwick.query(len(sorted_ratings)) - fenwick.query(rank[rating[i]])
        ascending_teams += smaller_left[i] * larger_right
        fenwick.update(rank[rating[i]], 1)
    
    # Count descending teams (similar logic with reversed comparisons)
    fenwick = FenwickTree(len(sorted_ratings))
    larger_left = [0] * n
    
    for i in range(n):
        larger_left[i] = fenwick.query(len(sorted_ratings)) - fenwick.query(rank[rating[i]])
        fenwick.update(rank[rating[i]], 1)
    
    fenwick = FenwickTree(len(sorted_ratings))
    descending_teams = 0
    
    for i in range(n - 1, -1, -1):
        smaller_right = fenwick.query(rank[rating[i]] - 1)
        descending_teams += larger_left[i] * smaller_right
        fenwick.update(rank[rating[i]], 1)
    
    return ascending_teams + descending_teams

def countSmaller(nums):
    """
    LeetCode 315: Count of Smaller Numbers After Self
    Count smaller elements to the right for each element
    """
    # Coordinate compression
    sorted_nums = sorted(set(nums))
    rank = {v: i + 1 for i, v in enumerate(sorted_nums)}
    
    fenwick = FenwickTree(len(sorted_nums))
    result = []
    
    # Process from right to left
    for i in range(len(nums) - 1, -1, -1):
        # Count smaller elements
        count = fenwick.query(rank[nums[i]] - 1)
        result.append(count)
        
        # Add current element to fenwick tree
        fenwick.update(rank[nums[i]], 1)
    
    return result[::-1]

def reversePairs(nums):
    """
    LeetCode 493: Reverse Pairs
    Count pairs (i, j) where i < j and nums[i] > 2 * nums[j]
    """
    # Coordinate compression with both original and doubled values
    all_values = set(nums + [2 * x for x in nums])
    sorted_values = sorted(all_values)
    rank = {v: i + 1 for i, v in enumerate(sorted_values)}
    
    fenwick = FenwickTree(len(sorted_values))
    count = 0
    
    # Process from right to left
    for i in range(len(nums) - 1, -1, -1):
        # Count how many j > i have nums[j] < nums[i] / 2
        # Equivalent to counting values < nums[i] / 2
        target = nums[i] / 2
        
        # Find largest value < target
        left, right = 0, len(sorted_values) - 1
        pos = -1
        while left <= right:
            mid = (left + right) // 2
            if sorted_values[mid] < target:
                pos = mid
                left = mid + 1
            else:
                right = mid - 1
        
        if pos >= 0:
            count += fenwick.query(pos + 1)
        
        # Add current number to fenwick tree
        fenwick.update(rank[nums[i]], 1)
    
    return count

class NumArray:
    """
    LeetCode 307: Range Sum Query - Mutable
    Support both point updates and range sum queries
    """
    
    def __init__(self, nums):
        self.nums = nums[:]
        self.fenwick = FenwickTreeFromArray(nums)
    
    def update(self, index, val):
        """Update element at index to val"""
        delta = val - self.nums[index]
        self.nums[index] = val
        self.fenwick.update(index, delta)
    
    def sumRange(self, left, right):
        """Return sum of elements from left to right"""
        return self.fenwick.range_query(left, right)

def createSortedArray(instructions):
    """
    LeetCode 1649: Create Sorted Array through Instructions
    Calculate cost of creating sorted array
    """
    MOD = 10**9 + 7
    
    # Coordinate compression
    sorted_vals = sorted(set(instructions))
    rank = {v: i + 1 for i, v in enumerate(sorted_vals)}
    
    fenwick = FenwickTree(len(sorted_vals))
    total_cost = 0
    
    for i, num in enumerate(instructions):
        # Count elements < num (left cost)
        left_cost = fenwick.query(rank[num] - 1)
        
        # Count elements > num (right cost)
        right_cost = i - fenwick.query(rank[num])
        
        # Add minimum cost
        total_cost = (total_cost + min(left_cost, right_cost)) % MOD
        
        # Add current element
        fenwick.update(rank[num], 1)
    
    return total_cost

# 2D Fenwick Tree for matrix operations
class FenwickTree2D:
    """
    2D Fenwick Tree for 2D range sum queries and point updates
    """
    
    def __init__(self, rows, cols):
        self.rows = rows
        self.cols = cols
        self.tree = [[0] * (cols + 1) for _ in range(rows + 1)]
    
    def update(self, row, col, delta):
        """Add delta to element at (row, col) - 1-indexed"""
        r = row
        while r <= self.rows:
            c = col
            while c <= self.cols:
                self.tree[r][c] += delta
                c += c & (-c)
            r += r & (-r)
    
    def query(self, row, col):
        """Get sum of rectangle from (1,1) to (row, col)"""
        result = 0
        r = row
        while r > 0:
            c = col
            while c > 0:
                result += self.tree[r][c]
                c -= c & (-c)
            r -= r & (-r)
        return result
    
    def range_query(self, r1, c1, r2, c2):
        """Get sum of rectangle from (r1,c1) to (r2,c2) - 1-indexed"""
        return (self.query(r2, c2) - 
                self.query(r1 - 1, c2) - 
                self.query(r2, c1 - 1) + 
                self.query(r1 - 1, c1 - 1))

# Template for inversion counting problems
def count_inversions_template(arr, comparison_func):
    """
    Generic template for counting inversions with custom comparison
    
    Args:
        arr: input array
        comparison_func: function(a, b) -> bool, True if (a, b) forms an inversion
    """
    # Coordinate compression
    sorted_vals = sorted(set(arr))
    rank = {v: i + 1 for i, v in enumerate(sorted_vals)}
    
    fenwick = FenwickTree(len(sorted_vals))
    count = 0
    
    for i in range(len(arr) - 1, -1, -1):
        # Count inversions based on comparison function
        # This is problem-specific and needs to be adapted
        
        # Add current element
        fenwick.update(rank[arr[i]], 1)
    
    return count