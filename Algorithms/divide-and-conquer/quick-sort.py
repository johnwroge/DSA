"""
Quick Sort - Divide and Conquer

LeetCode #215: Kth Largest Element in an Array
LeetCode #973: K Closest Points to Origin

Core pattern: Choose pivot, partition array around pivot, recursively sort subarrays.
"""

def quick_sort(nums, low=None, high=None):
    if low is None and high is None:
        low, high = 0, len(nums) - 1
    
    if low < high:
        # Partition the array and get pivot position
        pivot_idx = partition(nums, low, high)
        
        # Recursively sort elements before and after pivot
        quick_sort(nums, low, pivot_idx - 1)
        quick_sort(nums, pivot_idx + 1, high)
    
    return nums

def partition(nums, low, high):
    # Choose rightmost element as pivot
    pivot = nums[high]
    i = low - 1  # Index of smaller element
    
    for j in range(low, high):
        # If current element is smaller than or equal to pivot
        if nums[j] <= pivot:
            i += 1
            nums[i], nums[j] = nums[j], nums[i]
    
    # Place pivot in correct position
    nums[i + 1], nums[high] = nums[high], nums[i + 1]
    return i + 1

# Example usage
if __name__ == "__main__":
    nums = [10, 7, 8, 9, 1, 5]
    print(quick_sort(nums))  # Output: [1, 5, 7, 8, 9, 10]