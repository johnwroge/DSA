"""
Merge Sort - Divide and Conquer

LeetCode #148: Sort List
LeetCode #315: Count of Smaller Numbers After Self
LeetCode #493: Reverse Pairs

Core pattern: Divide array into halves, sort each half, then merge sorted halves.
"""

def merge_sort(nums):
    if len(nums) <= 1:
        return nums
    
    # Divide array in half
    mid = len(nums) // 2
    left = merge_sort(nums[:mid])
    right = merge_sort(nums[mid:])
    
    # Merge sorted halves
    return merge(left, right)

def merge(left, right):
    result = []
    i = j = 0
    
    # Compare elements from both arrays and merge in sorted order
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
    
    # Add remaining elements
    result.extend(left[i:])
    result.extend(right[j:])
    return result

# Example usage
if __name__ == "__main__":
    nums = [38, 27, 43, 3, 9, 82, 10]
    print(merge_sort(nums))  # Output: [3, 9, 10, 27, 38, 43, 82]