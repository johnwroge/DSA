"""
LeetCode Problems where Multiple Pointers can be applied:

26. Remove Duplicates from Sorted Array
27. Remove Element
80. Remove Duplicates from Sorted Array II
283. Move Zeroes
75. Sort Colors
88. Merge Sorted Array
905. Sort Array By Parity
922. Sort Array By Parity II
"""

def remove_duplicates(nums):
    """
    LeetCode 26: Remove Duplicates from Sorted Array
    Remove duplicates in-place, return new length
    
    Time: O(n), Space: O(1)
    """
    if not nums:
        return 0
    
    write_ptr = 0
    
    for read_ptr in range(1, len(nums)):
        if nums[read_ptr] != nums[write_ptr]:
            write_ptr += 1
            nums[write_ptr] = nums[read_ptr]
    
    return write_ptr + 1

def remove_element(nums, val):
    """
    LeetCode 27: Remove Element
    Remove all instances of val in-place
    
    Time: O(n), Space: O(1)
    """
    write_ptr = 0
    
    for read_ptr in range(len(nums)):
        if nums[read_ptr] != val:
            nums[write_ptr] = nums[read_ptr]
            write_ptr += 1
    
    return write_ptr

def remove_duplicates_ii(nums):
    """
    LeetCode 80: Remove Duplicates from Sorted Array II
    Allow at most 2 duplicates
    
    Time: O(n), Space: O(1)
    """
    if len(nums) <= 2:
        return len(nums)
    
    write_ptr = 2
    
    for read_ptr in range(2, len(nums)):
        if nums[read_ptr] != nums[write_ptr - 2]:
            nums[write_ptr] = nums[read_ptr]
            write_ptr += 1
    
    return write_ptr

def move_zeroes(nums):
    """
    LeetCode 283: Move Zeroes
    Move all zeros to end while maintaining relative order
    
    Time: O(n), Space: O(1)
    """
    write_ptr = 0
    
    # Move all non-zero elements to front
    for read_ptr in range(len(nums)):
        if nums[read_ptr] != 0:
            nums[write_ptr] = nums[read_ptr]
            write_ptr += 1
    
    # Fill remaining positions with zeros
    while write_ptr < len(nums):
        nums[write_ptr] = 0
        write_ptr += 1

def sort_colors(nums):
    """
    LeetCode 75: Sort Colors (Dutch National Flag)
    Sort array of 0s, 1s, and 2s
    
    Time: O(n), Space: O(1)
    """
    left = 0      # Next position for 0
    right = len(nums) - 1  # Next position for 2
    current = 0   # Current element being processed
    
    while current <= right:
        if nums[current] == 0:
            nums[left], nums[current] = nums[current], nums[left]
            left += 1
            current += 1
        elif nums[current] == 2:
            nums[current], nums[right] = nums[right], nums[current]
            right -= 1
            # Don't increment current as we need to process swapped element
        else:  # nums[current] == 1
            current += 1

def merge_sorted_arrays(nums1, m, nums2, n):
    """
    LeetCode 88: Merge Sorted Array
    Merge nums2 into nums1 in-place
    
    Time: O(m + n), Space: O(1)
    """
    # Start from the end to avoid overwriting
    ptr1 = m - 1      # Last element in nums1
    ptr2 = n - 1      # Last element in nums2
    write_ptr = m + n - 1  # Last position in merged array
    
    while ptr2 >= 0:
        if ptr1 >= 0 and nums1[ptr1] > nums2[ptr2]:
            nums1[write_ptr] = nums1[ptr1]
            ptr1 -= 1
        else:
            nums1[write_ptr] = nums2[ptr2]
            ptr2 -= 1
        write_ptr -= 1

def sort_array_by_parity(nums):
    """
    LeetCode 905: Sort Array By Parity
    Move even numbers before odd numbers
    
    Time: O(n), Space: O(1)
    """
    write_ptr = 0
    
    for read_ptr in range(len(nums)):
        if nums[read_ptr] % 2 == 0:  # Even number
            nums[write_ptr], nums[read_ptr] = nums[read_ptr], nums[write_ptr]
            write_ptr += 1
    
    return nums

def sort_array_by_parity_ii(nums):
    """
    LeetCode 922: Sort Array By Parity II
    Arrange so even indices have even numbers, odd indices have odd numbers
    
    Time: O(n), Space: O(1)
    """
    even_ptr = 0  # Points to next even index
    odd_ptr = 1   # Points to next odd index
    
    while even_ptr < len(nums) and odd_ptr < len(nums):
        if nums[even_ptr] % 2 == 0:
            even_ptr += 2
        elif nums[odd_ptr] % 2 == 1:
            odd_ptr += 2
        else:
            # Swap misplaced elements
            nums[even_ptr], nums[odd_ptr] = nums[odd_ptr], nums[even_ptr]
            even_ptr += 2
            odd_ptr += 2
    
    return nums

def partition_array(nums, k):
    """
    Partition array: elements < k, elements = k, elements > k
    Three-way partitioning
    
    Time: O(n), Space: O(1)
    """
    less_ptr = 0           # Next position for elements < k
    equal_ptr = 0          # Current element being processed
    greater_ptr = len(nums) - 1  # Next position for elements > k
    
    while equal_ptr <= greater_ptr:
        if nums[equal_ptr] < k:
            nums[less_ptr], nums[equal_ptr] = nums[equal_ptr], nums[less_ptr]
            less_ptr += 1
            equal_ptr += 1
        elif nums[equal_ptr] > k:
            nums[equal_ptr], nums[greater_ptr] = nums[greater_ptr], nums[equal_ptr]
            greater_ptr -= 1
            # Don't increment equal_ptr as we need to process swapped element
        else:  # nums[equal_ptr] == k
            equal_ptr += 1
    
    return less_ptr, greater_ptr + 1  # Boundaries of equal section

def separate_even_odd_maintain_order(nums):
    """
    Separate even and odd numbers while maintaining their relative order
    
    Time: O(n), Space: O(1)
    """
    write_ptr = 0
    
    # First pass: move even numbers to front
    for read_ptr in range(len(nums)):
        if nums[read_ptr] % 2 == 0:
            # Shift elements to make space
            temp = nums[read_ptr]
            for i in range(read_ptr, write_ptr, -1):
                nums[i] = nums[i - 1]
            nums[write_ptr] = temp
            write_ptr += 1
    
    return nums

def move_elements_to_end(nums, target):
    """
    Move all instances of target to end while maintaining order of others
    
    Time: O(n), Space: O(1)
    """
    write_ptr = 0
    
    # Move non-target elements to front
    for read_ptr in range(len(nums)):
        if nums[read_ptr] != target:
            nums[write_ptr] = nums[read_ptr]
            write_ptr += 1
    
    # Fill remaining with target
    while write_ptr < len(nums):
        nums[write_ptr] = target
        write_ptr += 1
    
    return nums

# Generic multiple pointers template
def multiple_pointers_template(nums, condition_func):
    """
    Generic template for multiple pointer problems
    
    Args:
        nums: Input array
        condition_func: Function that determines which elements to keep/move
    
    Returns:
        Modified array or new length
    """
    write_ptr = 0
    
    for read_ptr in range(len(nums)):
        if condition_func(nums[read_ptr]):
            nums[write_ptr] = nums[read_ptr]
            write_ptr += 1
    
    return write_ptr

# Template for partitioning problems
def partition_template(nums, partition_func):
    """
    Generic partitioning template
    
    Args:
        nums: Input array
        partition_func: Function that returns partition key (0, 1, 2, etc.)
    
    Returns:
        Partitioned array
    """
    # Count elements in each partition
    counts = {}
    for num in nums:
        key = partition_func(num)
        counts[key] = counts.get(key, 0) + 1
    
    # Place elements in correct partitions
    write_ptr = 0
    for partition_key in sorted(counts.keys()):
        for read_ptr in range(len(nums)):
            if partition_func(nums[read_ptr]) == partition_key and read_ptr >= write_ptr:
                nums[write_ptr], nums[read_ptr] = nums[read_ptr], nums[write_ptr]
                write_ptr += 1
                if write_ptr - 1 >= counts[partition_key]:
                    break
    
    return nums

# Template for stable partitioning (maintaining relative order)
def stable_partition_template(nums, condition_func):
    """
    Stable partitioning template that maintains relative order
    
    Args:
        nums: Input array
        condition_func: Function that returns True for elements to move to front
    
    Returns:
        Stably partitioned array
    """
    # Extract elements that satisfy condition
    satisfying = [num for num in nums if condition_func(num)]
    not_satisfying = [num for num in nums if not condition_func(num)]
    
    # Combine results
    result = satisfying + not_satisfying
    
    # Copy back to original array if needed
    for i in range(len(nums)):
        nums[i] = result[i]
    
    return len(satisfying)  # Boundary index