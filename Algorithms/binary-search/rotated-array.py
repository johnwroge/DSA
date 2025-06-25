"""
Binary Search on Rotated Array - Binary Search

LeetCode #33: Search in Rotated Sorted Array
LeetCode #153: Find Minimum in Rotated Sorted Array
LeetCode #154: Find Minimum in Rotated Sorted Array II

Core pattern: Identify which half of the array is sorted, then determine if target is in that half.
"""

def search_rotated(nums, target):
    left, right = 0, len(nums) - 1
    
    while left <= right:
        mid = left + (right - left) // 2
        
        if nums[mid] == target:
            return mid
        
        # Check if left half is sorted
        if nums[left] <= nums[mid]:
            # Check if target is in left half
            if nums[left] <= target < nums[mid]:
                right = mid - 1
            else:
                left = mid + 1
        # Right half is sorted
        else:
            # Check if target is in right half
            if nums[mid] < target <= nums[right]:
                left = mid + 1
            else:
                right = mid - 1
    
    return -1  # Not found

# Example usage
if __name__ == "__main__":
    nums = [4, 5, 6, 7, 0, 1, 2]
    target = 0
    print(search_rotated(nums, target))  # Output: 4