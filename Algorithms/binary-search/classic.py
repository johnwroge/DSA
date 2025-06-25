"""
Classic Binary Search - Binary Search

LeetCode #704: Binary Search
LeetCode #35: Search Insert Position
LeetCode #374: Guess Number Higher or Lower

Core pattern: Divide and conquer by repeatedly dividing the search interval in half.
"""

def binary_search(nums, target):
    left, right = 0, len(nums) - 1
    
    while left <= right:
        mid = left + (right - left) // 2
        
        if nums[mid] == target:
            return mid
        elif nums[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    
    return -1  # Not found

# Example usage
if __name__ == "__main__":
    nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    target = 7
    print(binary_search(nums, target))  # Output: 6