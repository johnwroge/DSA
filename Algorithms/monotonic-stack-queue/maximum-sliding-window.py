"""
LeetCode Problems where Maximum Sliding Window template can be applied:

239. Sliding Window Maximum
862. Shortest Subarray with Sum at Least K
1438. Longest Continuous Subarray With Absolute Diff Less Than or Equal to Limit
918. Maximum Sum Circular Subarray
1499. Max Value of Equation
480. Sliding Window Median
159. Longest Substring with At Most Two Distinct Characters
340. Longest Substring with At Most K Distinct Characters
992. Subarrays with K Different Integers
"""

from collections import deque
import heapq

def maxSlidingWindow(nums, k):
    """
    LeetCode 239: Sliding Window Maximum
    Find maximum in each sliding window of size k
    
    Time: O(n), Space: O(k)
    Uses monotonic deque to maintain potential maximums
    """
    if not nums or k == 0:
        return []
    
    dq = deque()  # Store indices in decreasing order of values
    result = []
    
    for i in range(len(nums)):
        # Remove indices outside current window
        while dq and dq[0] <= i - k:
            dq.popleft()
        
        # Remove smaller elements from back (they can never be maximum)
        while dq and nums[i] >= nums[dq[-1]]:
            dq.pop()
        
        dq.append(i)
        
        # Add result when window is complete
        if i >= k - 1:
            result.append(nums[dq[0]])
    
    return result

def minSlidingWindow(nums, k):
    """
    Find minimum in each sliding window of size k
    (Variation of maximum sliding window)
    """
    if not nums or k == 0:
        return []
    
    dq = deque()  # Store indices in increasing order of values
    result = []
    
    for i in range(len(nums)):
        # Remove indices outside current window
        while dq and dq[0] <= i - k:
            dq.popleft()
        
        # Remove larger elements from back
        while dq and nums[i] <= nums[dq[-1]]:
            dq.pop()
        
        dq.append(i)
        
        if i >= k - 1:
            result.append(nums[dq[0]])
    
    return result

def longestSubarray(nums, limit):
    """
    LeetCode 1438: Longest Continuous Subarray With Absolute Diff Less Than or Equal to Limit
    Find longest subarray where max - min <= limit
    """
    max_dq = deque()  # Decreasing order (for maximum)
    min_dq = deque()  # Increasing order (for minimum)
    
    left = 0
    max_len = 0
    
    for right in range(len(nums)):
        # Update max deque
        while max_dq and nums[right] >= nums[max_dq[-1]]:
            max_dq.pop()
        max_dq.append(right)
        
        # Update min deque
        while min_dq and nums[right] <= nums[min_dq[-1]]:
            min_dq.pop()
        min_dq.append(right)
        
        # Shrink window if difference exceeds limit
        while nums[max_dq[0]] - nums[min_dq[0]] > limit:
            if max_dq[0] == left:
                max_dq.popleft()
            if min_dq[0] == left:
                min_dq.popleft()
            left += 1
        
        max_len = max(max_len, right - left + 1)
    
    return max_len

def shortestSubarray(nums, k):
    """
    LeetCode 862: Shortest Subarray with Sum at Least K
    Find shortest subarray with sum >= k (handles negative numbers)
    """
    n = len(nums)
    prefix = [0]
    
    # Build prefix sum array
    for num in nums:
        prefix.append(prefix[-1] + num)
    
    dq = deque()  # Store indices in increasing order of prefix sums
    min_len = float('inf')
    
    for i in range(len(prefix)):
        # Check if we can form a valid subarray
        while dq and prefix[i] - prefix[dq[0]] >= k:
            min_len = min(min_len, i - dq.popleft())
        
        # Maintain increasing order of prefix sums
        while dq and prefix[i] <= prefix[dq[-1]]:
            dq.pop()
        
        dq.append(i)
    
    return min_len if min_len != float('inf') else -1

def findMaxValueOfEquation(points, k):
    """
    LeetCode 1499: Max Value of Equation
    Find max value of yi + yj + |xi - xj| where |xi - xj| <= k
    Since points are sorted by x, this becomes yi + yj + xj - xi
    """
    # We want to maximize (yi - xi) + (yj + xj) for each j
    dq = deque()  # Store indices in decreasing order of (y - x)
    max_val = float('-inf')
    
    for j in range(len(points)):
        xj, yj = points[j]
        
        # Remove points outside range
        while dq and xj - points[dq[0]][0] > k:
            dq.popleft()
        
        # Calculate max value if deque not empty
        if dq:
            xi, yi = points[dq[0]]
            max_val = max(max_val, (yi - xi) + (yj + xj))
        
        # Maintain decreasing order of (y - x)
        while dq and (yj - xj) >= (points[dq[-1]][1] - points[dq[-1]][0]):
            dq.pop()
        
        dq.append(j)
    
    return max_val

class SlidingWindowMedian:
    """
    LeetCode 480: Sliding Window Median
    Find median in each sliding window (uses heaps instead of deque)
    """
    def __init__(self):
        self.max_heap = []  # Left half (negated for max heap)
        self.min_heap = []  # Right half
    
    def medianSlidingWindow(self, nums, k):
        result = []
        
        for i in range(len(nums)):
            # Add current number
            self.addNumber(nums[i])
            
            # Remove number going out of window
            if i >= k:
                self.removeNumber(nums[i - k])
            
            # Add median when window is complete
            if i >= k - 1:
                result.append(self.getMedian())
        
        return result
    
    def addNumber(self, num):
        if not self.max_heap or num <= -self.max_heap[0]:
            heapq.heappush(self.max_heap, -num)
        else:
            heapq.heappush(self.min_heap, num)
        
        self.rebalance()
    
    def removeNumber(self, num):
        if num <= -self.max_heap[0]:
            self.max_heap.remove(-num)
            heapq.heapify(self.max_heap)
        else:
            self.min_heap.remove(num)
            heapq.heapify(self.min_heap)
        
        self.rebalance()
    
    def rebalance(self):
        if len(self.max_heap) > len(self.min_heap) + 1:
            heapq.heappush(self.min_heap, -heapq.heappop(self.max_heap))
        elif len(self.min_heap) > len(self.max_heap) + 1:
            heapq.heappush(self.max_heap, -heapq.heappop(self.min_heap))
    
    def getMedian(self):
        if len(self.max_heap) == len(self.min_heap):
            return (-self.max_heap[0] + self.min_heap[0]) / 2.0
        elif len(self.max_heap) > len(self.min_heap):
            return float(-self.max_heap[0])
        else:
            return float(self.min_heap[0])

def lengthOfLongestSubstringKDistinct(s, k):
    """
    LeetCode 340: Longest Substring with At Most K Distinct Characters
    Use sliding window with character frequency tracking
    """
    if k == 0:
        return 0
    
    from collections import defaultdict
    char_count = defaultdict(int)
    left = 0
    max_len = 0
    
    for right in range(len(s)):
        # Expand window
        char_count[s[right]] += 1
        
        # Shrink window if too many distinct characters
        while len(char_count) > k:
            char_count[s[left]] -= 1
            if char_count[s[left]] == 0:
                del char_count[s[left]]
            left += 1
        
        max_len = max(max_len, right - left + 1)
    
    return max_len

# Generic sliding window template with monotonic deque
def sliding_window_extremum(nums, k, comparison_func):
    """
    Generic template for finding extremum in sliding windows
    
    Args:
        nums: input array
        k: window size
        comparison_func: function(current, deque_back) -> bool
                        True if current should replace deque_back
    """
    if not nums or k == 0:
        return []
    
    dq = deque()
    result = []
    
    for i in range(len(nums)):
        # Remove indices outside window
        while dq and dq[0] <= i - k:
            dq.popleft()
        
        # Maintain monotonic property
        while dq and comparison_func(nums[i], nums[dq[-1]]):
            dq.pop()
        
        dq.append(i)
        
        # Add result when window is complete
        if i >= k - 1:
            result.append(nums[dq[0]])
    
    return result

# Example usage of generic template
def max_sliding_window_generic(nums, k):
    return sliding_window_extremum(
        nums, k, 
        lambda curr, back: curr >= back
    )

def min_sliding_window_generic(nums, k):
    return sliding_window_extremum(
        nums, k,
        lambda curr, back: curr <= back
    )