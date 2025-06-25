"""
Binary Search on Answer Space - Binary Search

LeetCode #1011: Capacity To Ship Packages Within D Days
LeetCode #410: Split Array Largest Sum
LeetCode #875: Koko Eating Bananas

Core pattern: Use binary search to find a value that satisfies a condition, even when the array isn't sorted.
"""

def binary_search_answer(array, condition_func):
    left = min_possible_answer
    right = max_possible_answer
    
    while left < right:
        mid = left + (right - left) // 2
        
        if condition_func(mid):
            right = mid
        else:
            left = mid + 1
    
    return left

# Example: Find minimum eating speed to finish bananas within h hours
def min_eating_speed(piles, h):
    def can_finish(speed):
        hours_needed = sum((pile + speed - 1) // speed for pile in piles)
        return hours_needed <= h
    
    left, right = 1, max(piles)
    
    while left < right:
        mid = left + (right - left) // 2
        if can_finish(mid):
            right = mid
        else:
            left = mid + 1
    
    return left

# Example usage
if __name__ == "__main__":
    piles = [3, 6, 7, 11]
    h = 8
    print(min_eating_speed(piles, h))  # Output: 4