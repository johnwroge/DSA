"""
Maximum Subarray - Divide and Conquer

LeetCode #53: Maximum Subarray
LeetCode #918: Maximum Sum Circular Subarray

Core pattern: Divide array, find max subarray within each half and crossing the middle.
"""

def max_subarray(nums):
    return _max_subarray(nums, 0, len(nums) - 1)

def _max_subarray(nums, left, right):
    # Base case: single element
    if left == right:
        return nums[left]
    
    # Divide array in half
    mid = (left + right) // 2
    
    # Find max subarray in left half, right half, and crossing the middle
    left_max = _max_subarray(nums, left, mid)
    right_max = _max_subarray(nums, mid + 1, right)
    cross_max = max_crossing_subarray(nums, left, mid, right)
    
    # Return maximum of the three
    return max(left_max, right_max, cross_max)

def max_crossing_subarray(nums, left, mid, right):
    # Find maximum subarray crossing to the left of mid
    left_sum = 0
    left_max_sum = float('-inf')
    for i in range(mid, left - 1, -1):
        left_sum += nums[i]
        left_max_sum = max(left_max_sum, left_sum)
    
    # Find maximum subarray crossing to the right of mid
    right_sum = 0
    right_max_sum = float('-inf')
    for i in range(mid + 1, right + 1):
        right_sum += nums[i]
        right_max_sum = max(right_max_sum, right_sum)
    
    # Return sum of the two
    return left_max_sum + right_max_sum

# Example usage
if __name__ == "__main__":
    nums = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
    print(max_subarray(nums))  # Output: 6 (from subarray [4, -1, 2, 1])