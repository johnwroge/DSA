"""
LeetCode 992: Subarrays with K Different Integers
LeetCode 2302: Count Subarrays With Score Less Than K
LeetCode 1248: Count Number of Nice Subarrays (your original problem is similar to this category)
"""


def sliding_window_with_counter(arr):
    counter = {}
    left = 0
    result = 0
    
    for right in range(len(arr)):
        # Add current element to counter
        counter[arr[right]] = counter.get(arr[right], 0) + 1
        
        # Process window - when some condition is met
        while condition_is_met(counter):
            # Update result
            result += calculate_contribution(left, right, len(arr))
            
            # Shrink window from left
            counter[arr[left]] -= 1
            if counter[arr[left]] == 0:
                del counter[arr[left]]
            left += 1
    
    return result