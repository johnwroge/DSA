"""
LeetCode Problems where Three Pointers can be applied:

15. 3Sum
16. 3Sum Closest
18. 4Sum
259. 3Sum Smaller
923. 3Sum With Multiplicity
1477. Find Two Non-overlapping Sub-arrays Each With Target Sum
"""

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
                
                # Skip duplicates for second and third elements
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
            
            # Update closest if current sum is closer to target
            if abs(target - current_sum) < abs(target - closest_sum):
                closest_sum = current_sum
            
            if current_sum < target:
                left += 1
            elif current_sum > target:
                right -= 1
            else:
                return current_sum  # Exact match found
    
    return closest_sum

def four_sum(nums, target):
    """
    LeetCode 18: 4Sum
    Find all unique quadruplets that sum to target
    
    Time: O(n³), Space: O(1)
    """
    nums.sort()
    result = []
    n = len(nums)
    
    for i in range(n - 3):
        # Skip duplicates for first element
        if i > 0 and nums[i] == nums[i - 1]:
            continue
        
        for j in range(i + 1, n - 2):
            # Skip duplicates for second element
            if j > i + 1 and nums[j] == nums[j - 1]:
                continue
            
            left, right = j + 1, n - 1
            two_sum_target = target - nums[i] - nums[j]
            
            while left < right:
                current_sum = nums[left] + nums[right]
                
                if current_sum == two_sum_target:
                    result.append([nums[i], nums[j], nums[left], nums[right]])
                    
                    # Skip duplicates for third and fourth elements
                    while left < right and nums[left] == nums[left + 1]:
                        left += 1
                    while left < right and nums[right] == nums[right - 1]:
                        right -= 1
                    
                    left += 1
                    right -= 1
                elif current_sum < two_sum_target:
                    left += 1
                else:
                    right -= 1
    
    return result

def three_sum_smaller(nums, target):
    """
    LeetCode 259: 3Sum Smaller
    Count triplets with sum less than target
    
    Time: O(n²), Space: O(1)
    """
    nums.sort()
    n = len(nums)
    count = 0
    
    for i in range(n - 2):
        left, right = i + 1, n - 1
        
        while left < right:
            current_sum = nums[i] + nums[left] + nums[right]
            
            if current_sum < target:
                # All pairs (left, right-1), (left, right-2), ..., (left, left+1)
                # will also have sum < target
                count += right - left
                left += 1
            else:
                right -= 1
    
    return count

def three_sum_multiplicity(arr, target):
    """
    LeetCode 923: 3Sum With Multiplicity
    Count triplets with given sum (allowing duplicates)
    
    Time: O(n²), Space: O(1)
    """
    MOD = 10**9 + 7
    arr.sort()
    n = len(arr)
    count = 0
    
    for i in range(n - 2):
        left, right = i + 1, n - 1
        
        while left < right:
            current_sum = arr[i] + arr[left] + arr[right]
            
            if current_sum < target:
                left += 1
            elif current_sum > target:
                right -= 1
            else:
                # Found valid triplet
                if arr[left] == arr[right]:
                    # All elements between left and right are the same
                    count += (right - left + 1) * (right - left) // 2
                    break
                else:
                    # Count duplicates
                    left_count = 1
                    right_count = 1
                    
                    while left + 1 < right and arr[left] == arr[left + 1]:
                        left += 1
                        left_count += 1
                    
                    while right - 1 > left and arr[right] == arr[right - 1]:
                        right -= 1
                        right_count += 1
                    
                    count += left_count * right_count
                    left += 1
                    right -= 1
    
    return count % MOD

def three_sum_with_different_arrays(nums1, nums2, nums3, target):
    """
    Find triplets from three different arrays that sum to target
    
    Time: O(n₁ * n₂ * log n₃), Space: O(n₃)
    """
    # Convert third array to set for O(1) lookup
    nums3_set = set(nums3)
    triplets = []
    
    for num1 in nums1:
        for num2 in nums2:
            needed = target - num1 - num2
            if needed in nums3_set:
                triplets.append([num1, num2, needed])
    
    return triplets

def three_sum_range(nums, min_sum, max_sum):
    """
    Find all triplets with sum in range [min_sum, max_sum]
    
    Time: O(n²), Space: O(1)
    """
    nums.sort()
    n = len(nums)
    result = []
    
    for i in range(n - 2):
        if i > 0 and nums[i] == nums[i - 1]:
            continue
        
        left, right = i + 1, n - 1
        
        while left < right:
            current_sum = nums[i] + nums[left] + nums[right]
            
            if min_sum <= current_sum <= max_sum:
                result.append([nums[i], nums[left], nums[right]])
                
                # Skip duplicates
                while left < right and nums[left] == nums[left + 1]:
                    left += 1
                while left < right and nums[right] == nums[right - 1]:
                    right -= 1
                
                left += 1
                right -= 1
            elif current_sum < min_sum:
                left += 1
            else:
                right -= 1
    
    return result

# Generic three pointers template
def three_pointers_template(nums, target, operation='sum'):
    """
    Generic template for three pointer problems
    
    Args:
        nums: Input array
        target: Target value
        operation: 'sum', 'product', etc.
    
    Returns:
        Result based on specific problem requirements
    """
    nums.sort()
    n = len(nums)
    result = []
    
    for i in range(n - 2):
        # Skip duplicates for first element
        if i > 0 and nums[i] == nums[i - 1]:
            continue
        
        left, right = i + 1, n - 1
        
        while left < right:
            if operation == 'sum':
                current_value = nums[i] + nums[left] + nums[right]
            elif operation == 'product':
                current_value = nums[i] * nums[left] * nums[right]
            
            if current_value == target:
                result.append([nums[i], nums[left], nums[right]])
                
                # Skip duplicates
                while left < right and nums[left] == nums[left + 1]:
                    left += 1
                while left < right and nums[right] == nums[right - 1]:
                    right -= 1
                
                left += 1
                right -= 1
            elif current_value < target:
                left += 1
            else:
                right -= 1
    
    return result

# Template for k-sum problems (generalized)
def k_sum(nums, target, k):
    """
    Generic k-sum solver using recursion + two pointers
    
    Time: O(n^(k-1)), Space: O(k)
    """
    nums.sort()
    
    def k_sum_helper(nums, target, k, start_index):
        result = []
        
        if k == 2:
            # Base case: use two pointers
            left, right = start_index, len(nums) - 1
            
            while left < right:
                current_sum = nums[left] + nums[right]
                
                if current_sum == target:
                    result.append([nums[left], nums[right]])
                    
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
        else:
            # Recursive case
            for i in range(start_index, len(nums) - k + 1):
                if i > start_index and nums[i] == nums[i - 1]:
                    continue
                
                sub_results = k_sum_helper(nums, target - nums[i], k - 1, i + 1)
                for sub_result in sub_results:
                    result.append([nums[i]] + sub_result)
        
        return result
    
    return k_sum_helper(nums, target, k, 0)