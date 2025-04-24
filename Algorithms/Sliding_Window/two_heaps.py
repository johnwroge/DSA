"""
LeetCode 480: Sliding Window Median
LeetCode 295: Find Median from Data Stream (variation)
"""

import heapq

def sliding_window_with_two_heaps(nums, k):
    n = len(nums)
    result = []
    # Max heap for elements <= median
    small = []  # (values negated for max-heap)
    # Min heap for elements > median
    large = []
    # Hash map to keep track of invalid numbers
    removed = {}
    
    def add_num(num):
        if not small or -small[0] >= num:
            heapq.heappush(small, -num)
        else:
            heapq.heappush(large, num)
        
        # Rebalance heaps
        balance()
    
    def balance():
        # Ensure size difference is at most 1
        while len(small) > len(large) + 1:
            heapq.heappush(large, -heapq.heappop(small))
        while len(large) > len(small):
            heapq.heappush(small, -heapq.heappop(large))
    
    def remove_num(num):
        removed[num] = removed.get(num, 0) + 1
        
        # Lazy removal - actual removal happens during find_median
        # Balance only if removal would make heaps imbalanced
        if num <= -small[0]:
            if num == -small[0]:
                clean_heap(small, removed)
            balance()
        else:
            if num == large[0]:
                clean_heap(large, removed)
            balance()
    
    def clean_heap(heap, removed_map):
        # Remove elements that have been removed from the window
        while heap and removed_map.get(-heap[0] if heap is small else heap[0], 0) > 0:
            removed_map[-heap[0] if heap is small else heap[0]] -= 1
            heapq.heappop(heap)
    
    def find_median():
        clean_heap(small, removed)
        clean_heap(large, removed)
        
        if not small and not large:
            return 0
        
        # If odd number of elements
        if len(small) > len(large):
            return -small[0]
        # If even number of elements
        return (-small[0] + large[0]) / 2
    
    # Process the first k-1 elements
    for i in range(k - 1):
        add_num(nums[i])
    
    # Slide the window
    for i in range(k - 1, n):
        # Add new element
        add_num(nums[i])
        
        # Calculate median
        result.append(find_median())
        
        # Remove the leftmost element
        remove_num(nums[i - (k - 1)])
    
    return result