
import heapq
from typing import List, Optional


# =============================================================================
# MERGE K SORTED TEMPLATE
# =============================================================================

"""
LeetCode Problems that can be solved with this technique:
- 23. Merge k Sorted Lists
- 264. Ugly Number II
- 313. Super Ugly Number
- 378. Kth Smallest Element in a Sorted Matrix
- 632. Smallest Range Covering Elements from K Lists
- 719. Find K-th Smallest Pair Distance
- 786. K-th Smallest Prime Fraction
"""

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def merge_k_sorted_lists(lists: List[Optional[ListNode]]) -> Optional[ListNode]:
    """Merge k sorted linked lists using min heap"""
    if not lists:
        return None
    
    # Custom comparison for ListNode
    ListNode.__lt__ = lambda self, other: self.val < other.val
    
    heap = []
    # Initialize heap with first node from each list
    for i, head in enumerate(lists):
        if head:
            heapq.heappush(heap, head)
    
    dummy = ListNode(0)
    current = dummy
    
    while heap:
        # Get minimum node
        node = heapq.heappop(heap)
        current.next = node
        current = current.next
        
        # Add next node from same list
        if node.next:
            heapq.heappush(heap, node.next)
    
    return dummy.next

def merge_k_sorted_arrays(arrays: List[List[int]]) -> List[int]:
    """Merge k sorted arrays using min heap"""
    heap = []
    result = []
    
    # Initialize heap with first element from each array
    for i, arr in enumerate(arrays):
        if arr:
            heapq.heappush(heap, (arr[0], i, 0))  # (value, array_idx, element_idx)
    
    while heap:
        val, arr_idx, elem_idx = heapq.heappop(heap)
        result.append(val)
        
        # Add next element from same array
        if elem_idx + 1 < len(arrays[arr_idx]):
            next_val = arrays[arr_idx][elem_idx + 1]
            heapq.heappush(heap, (next_val, arr_idx, elem_idx + 1))
    
    return result

def kth_smallest_in_matrix(matrix: List[List[int]], k: int) -> int:
    """Find kth smallest element in sorted matrix"""
    n = len(matrix)
    heap = []
    
    # Initialize heap with first column
    for i in range(min(k, n)):
        heapq.heappush(heap, (matrix[i][0], i, 0))
    
    for _ in range(k):
        val, row, col = heapq.heappop(heap)
        if col + 1 < len(matrix[row]):
            heapq.heappush(heap, (matrix[row][col + 1], row, col + 1))
    
    return val
