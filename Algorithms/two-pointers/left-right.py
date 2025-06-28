"""
LeetCode Problems where Left-Right Pointers can be applied:

167. Two Sum II - Input Array Is Sorted
125. Valid Palindrome
344. Reverse String
11. Container With Most Water
15. 3Sum
42. Trapping Rain Water
16. 3Sum Closest
977. Squares of a Sorted Array
"""

def two_sum_sorted(numbers, target):
    """
    LeetCode 167: Two Sum II - Input Array Is Sorted
    Find two numbers that add up to target
    
    Time: O(n), Space: O(1)
    """
    left, right = 0, len(numbers) - 1
    
    while left < right:
        current_sum = numbers[left] + numbers[right]
        
        if current_sum == target:
            return [left + 1, right + 1]  # 1-indexed
        elif current_sum < target:
            left += 1
        else:
            right -= 1
    
    return [-1, -1]  # Not found

def is_palindrome(s):
    """
    LeetCode 125: Valid Palindrome
    Check if string is palindrome (alphanumeric only)
    
    Time: O(n), Space: O(1)
    """
    left, right = 0, len(s) - 1
    
    while left < right:
        # Skip non-alphanumeric characters
        while left < right and not s[left].isalnum():
            left += 1
        while left < right and not s[right].isalnum():
            right -= 1
        
        # Compare characters
        if s[left].lower() != s[right].lower():
            return False
        
        left += 1
        right -= 1
    
    return True

def reverse_string(s):
    """
    LeetCode 344: Reverse String
    Reverse string in-place
    
    Time: O(n), Space: O(1)
    """
    left, right = 0, len(s) - 1
    
    while left < right:
        s[left], s[right] = s[right], s[left]
        left += 1
        right -= 1

def max_area(height):
    """
    LeetCode 11: Container With Most Water
    Find maximum area between two vertical lines
    
    Time: O(n), Space: O(1)
    """
    left, right = 0, len(height) - 1
    max_water = 0
    
    while left < right:
        # Calculate current area
        width = right - left
        current_area = width * min(height[left], height[right])
        max_water = max(max_water, current_area)
        
        # Move pointer with smaller height
        if height[left] < height[right]:
            left += 1
        else:
            right -= 1
    
    return max_water

def three_sum(nums):
    """
    LeetCode 15: 3Sum
    Find all unique triplets that sum to zero
    
    Time: O(n²), Space: O(1)
    """
    nums.sort()
    result = []
    n = len(nums)
    
    for i in range(n - 2):
        # Skip duplicates for first element
        if i > 0 and nums[i] == nums[i - 1]:
            continue
        
        left, right = i + 1, n - 1
        target = -nums[i]
        
        while left < right:
            current_sum = nums[left] + nums[right]
            
            if current_sum == target:
                result.append([nums[i], nums[left], nums[right]])
                
                # Skip duplicates
                while left < right and nums[left] == nums[left + 1]:
                    left += 1
                while left < right and nums[right] == nums[right - 1]:
                    right -= 1
                
                left += 1
                right -= 1
            elif current_sum < target:
                left += 1
            else:
                right -= 1
    
    return result

def trap_rain_water(height):
    """
    LeetCode 42: Trapping Rain Water
    Calculate trapped rainwater
    
    Time: O(n), Space: O(1)
    """
    if not height:
        return 0
    
    left, right = 0, len(height) - 1
    left_max = right_max = 0
    water = 0
    
    while left < right:
        if height[left] < height[right]:
            if height[left] >= left_max:
                left_max = height[left]
            else:
                water += left_max - height[left]
            left += 1
        else:
            if height[right] >= right_max:
                right_max = height[right]
            else:
                water += right_max - height[right]
            right -= 1
    
    return water

def three_sum_closest(nums, target):
    """
    LeetCode 16: 3Sum Closest
    Find three numbers whose sum is closest to target
    
    Time: O(n²), Space: O(1)
    """
    nums.sort()
    n = len(nums)
    closest_sum = float('inf')
    
    for i in range(n - 2):
        left, right = i + 1, n - 1
        
        while left < right:
            current_sum = nums[i] + nums[left] + nums[right]
            
            # Update closest if current sum is closer
            if abs(target - current_sum) < abs(target - closest_sum):
                closest_sum = current_sum
            
            if current_sum < target:
                left += 1
            elif current_sum > target:
                right -= 1
            else:
                return current_sum  # Exact match
    
    return closest_sum

def sorted_squares(nums):
    """
    LeetCode 977: Squares of a Sorted Array
    Return squares of sorted array in sorted order
    
    Time: O(n), Space: O(n)
    """
    n = len(nums)
    result = [0] * n
    left, right = 0, n - 1
    pos = n - 1  # Fill result from end
    
    while left <= right:
        left_square = nums[left] ** 2
        right_square = nums[right] ** 2
        
        if left_square > right_square:
            result[pos] = left_square
            left += 1
        else:
            result[pos] = right_square
            right -= 1
        
        pos -= 1
    
    return result

def partition_array(nums, k):
    """
    Generic partition template
    Partition array around value k
    
    Time: O(n), Space: O(1)
    """
    left, right = 0, len(nums) - 1
    
    while left <= right:
        if nums[left] <= k:
            left += 1
        elif nums[right] > k:
            right -= 1
        else:
            nums[left], nums[right] = nums[right], nums[left]
            left += 1
            right -= 1
    
    return left  # Position where partition ends

def remove_duplicates(nums):
    """
    Generic remove duplicates template
    Remove duplicates from sorted array in-place
    
    Time: O(n), Space: O(1)
    """
    if not nums:
        return 0
    
    left = 0
    
    for right in range(1, len(nums)):
        if nums[right] != nums[left]:
            left += 1
            nums[left] = nums[right]
    
    return left + 1

# Generic left-right template
def left_right_template(arr, target_condition):
    """
    Generic template for left-right pointer problems
    
    Args:
        arr: Input array (usually sorted)
        target_condition: Function that determines movement direction
    
    Returns:
        Result based on specific problem requirements
    """
    left, right = 0, len(arr) - 1
    result = None
    
    while left < right:
        current_value = arr[left] + arr[right]  # or other operation
        
        if target_condition(current_value):
            result = (left, right)  # Found target
            break
        elif current_value < target:  # Need larger value
            left += 1
        else:  # Need smaller value
            right -= 1
    
    return result

# Template for finding pairs with specific property
def find_pairs_template(nums, target):
    """
    Template for finding pairs in sorted array
    """
    nums.sort()  # Ensure sorted
    left, right = 0, len(nums) - 1
    pairs = []
    
    while left < right:
        current_sum = nums[left] + nums[right]
        
        if current_sum == target:
            pairs.append([nums[left], nums[right]])
            left += 1
            right -= 1
            
            # Skip duplicates if needed
            while left < right and nums[left] == nums[left - 1]:
                left += 1
            while left < right and nums[right] == nums[right + 1]:
                right -= 1
                
        elif current_sum < target:
            left += 1
        else:
            right -= 1
    
    return pairs