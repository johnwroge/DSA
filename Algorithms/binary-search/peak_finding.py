"""
Peak Finding - Binary Search

LeetCode #162: Find Peak Element
LeetCode #852: Peak Index in a Mountain Array
LeetCode #1095: Find in Mountain Array

Core pattern: Use property of peaks to navigate with binary search (compare mid with neighbors).
"""

def find_peak_element(nums):
    left, right = 0, len(nums) - 1
    
    while left < right:
        mid = left + (right - left) // 2
        
        # If mid is less than its right neighbor, peak is on the right side
        if nums[mid] < nums[mid + 1]:
            left = mid + 1
        # Otherwise, peak is on the left side or at mid
        else:
            right = mid
    
    # When left == right, we've found the peak
    return left

# Example usage
if __name__ == "__main__":
    nums = [1, 2, 3, 1]
    print(find_peak_element(nums))  # Output: 2