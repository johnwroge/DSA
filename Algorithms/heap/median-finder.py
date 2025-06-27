import heapq
from typing import List, Optional


# =============================================================================
# MEDIAN FINDER TEMPLATE
# =============================================================================

"""
LeetCode Problems that can be solved with this technique:
- 295. Find Median from Data Stream
- 480. Sliding Window Median
- 4. Median of Two Sorted Arrays (variation)
"""

class MedianFinder:
    """
    Data structure to find median from data stream
    Uses two heaps: max_heap for smaller half, min_heap for larger half
    """
    
    def __init__(self):
        self.max_heap = []  # For smaller half (use negative values for max heap)
        self.min_heap = []  # For larger half
    
    def addNum(self, num: int) -> None:
        """Add number to data structure"""
        if not self.max_heap or num <= -self.max_heap[0]:
            heapq.heappush(self.max_heap, -num)
        else:
            heapq.heappush(self.min_heap, num)
        
        # Balance heaps
        if len(self.max_heap) > len(self.min_heap) + 1:
            val = -heapq.heappop(self.max_heap)
            heapq.heappush(self.min_heap, val)
        elif len(self.min_heap) > len(self.max_heap) + 1:
            val = heapq.heappop(self.min_heap)
            heapq.heappush(self.max_heap, -val)
    
    def findMedian(self) -> float:
        """Find median of all numbers added so far"""
        if len(self.max_heap) == len(self.min_heap):
            return (-self.max_heap[0] + self.min_heap[0]) / 2.0
        elif len(self.max_heap) > len(self.min_heap):
            return -self.max_heap[0]
        else:
            return self.min_heap[0]

def sliding_window_median(nums: List[int], k: int) -> List[float]:
    """Find median in sliding window of size k"""
    def get_median(window):
        sorted_window = sorted(window)
        n = len(sorted_window)
        if n % 2 == 1:
            return float(sorted_window[n // 2])
        else:
            return (sorted_window[n // 2 - 1] + sorted_window[n // 2]) / 2.0
    
    result = []
    window = []
    
    for i, num in enumerate(nums):
        window.append(num)
        
        if len(window) == k:
            result.append(get_median(window))
            window.pop(0)  # Remove first element
    
    return result

# Alternative implementation using two heaps for sliding window median
class SlidingWindowMedian:
    def __init__(self):
        self.max_heap = []  # smaller half
        self.min_heap = []  # larger half
    
    def medianSlidingWindow(self, nums: List[int], k: int) -> List[float]:
        result = []
        
        for i, num in enumerate(nums):
            self.add_num(num)
            
            if i >= k:
                self.remove_num(nums[i - k])
            
            if i >= k - 1:
                result.append(self.find_median())
        
        return result
    
    def add_num(self, num):
        if not self.max_heap or num <= -self.max_heap[0]:
            heapq.heappush(self.max_heap, -num)
        else:
            heapq.heappush(self.min_heap, num)
        self.balance()
    
    def remove_num(self, num):
        if num <= -self.max_heap[0]:
            self.max_heap.remove(-num)
            heapq.heapify(self.max_heap)
        else:
            self.min_heap.remove(num)
            heapq.heapify(self.min_heap)
        self.balance()
    
    def balance(self):
        if len(self.max_heap) > len(self.min_heap) + 1:
            val = -heapq.heappop(self.max_heap)
            heapq.heappush(self.min_heap, val)
        elif len(self.min_heap) > len(self.max_heap) + 1:
            val = heapq.heappop(self.min_heap)
            heapq.heappush(self.max_heap, -val)
    
    def find_median(self):
        if len(self.max_heap) == len(self.min_heap):
            return (-self.max_heap[0] + self.min_heap[0]) / 2.0
        elif len(self.max_heap) > len(self.min_heap):
            return float(-self.max_heap[0])
        else:
            return float(self.min_heap[0])
