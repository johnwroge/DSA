import heapq
from typing import List, Optional

# =============================================================================
# KTH ELEMENT TEMPLATE
# =============================================================================

"""
LeetCode Problems that can be solved with this technique:
- 215. Kth Largest Element in an Array
- 347. Top K Frequent Elements
- 692. Top K Frequent Words
- 703. Kth Largest Element in a Stream
- 973. K Closest Points to Origin
- 1046. Last Stone Weight
- 295. Find Median from Data Stream (variation)
"""

def kth_largest_quickselect(nums: List[int], k: int) -> int:
    """Find kth largest element using quickselect - O(n) average"""
    def partition(left, right, pivot_idx):
        pivot = nums[pivot_idx]
        # Move pivot to end
        nums[pivot_idx], nums[right] = nums[right], nums[pivot_idx]
        
        store_idx = left
        for i in range(left, right):
            if nums[i] < pivot:
                nums[store_idx], nums[i] = nums[i], nums[store_idx]
                store_idx += 1
        
        # Move pivot to final position
        nums[right], nums[store_idx] = nums[store_idx], nums[right]
        return store_idx
    
    def select(left, right, k_smallest):
        if left == right:
            return nums[left]
        
        pivot_idx = left + (right - left) // 2
        pivot_idx = partition(left, right, pivot_idx)
        
        if k_smallest == pivot_idx:
            return nums[k_smallest]
        elif k_smallest < pivot_idx:
            return select(left, pivot_idx - 1, k_smallest)
        else:
            return select(pivot_idx + 1, right, k_smallest)
    
    return select(0, len(nums) - 1, len(nums) - k)

def kth_largest_heap(nums: List[int], k: int) -> int:
    """Find kth largest element using min heap - O(n log k)"""
    heap = []
    for num in nums:
        heapq.heappush(heap, num)
        if len(heap) > k:
            heapq.heappop(heap)
    return heap[0]

def top_k_frequent(nums: List[int], k: int) -> List[int]:
    """Find k most frequent elements"""
    from collections import Counter
    count = Counter(nums)
    
    # Use min heap of size k
    heap = []
    for num, freq in count.items():
        heapq.heappush(heap, (freq, num))
        if len(heap) > k:
            heapq.heappop(heap)
    
    return [num for freq, num in heap]
