"""
LeetCode Problems where Next Greater Element template can be applied:

496. Next Greater Element I
503. Next Greater Element II
556. Next Greater Element III
739. Daily Temperatures
901. Online Stock Span
1019. Next Greater Node In Linked List
1124. Longest Well-Performing Interval
1130. Minimum Cost Tree From Leaf Values
1475. Final Prices With a Special Discount in a Shop
1776. Car Fleet II
"""

def nextGreaterElement(nums):
    """
    Find next greater element for each element in array
    
    Time: O(n), Space: O(n)
    Returns array where result[i] = next greater element of nums[i], or -1 if none
    """
    n = len(nums)
    result = [-1] * n
    stack = []  # Store indices in decreasing order of values
    
    for i in range(n):
        # While current element is greater than stack top
        while stack and nums[i] > nums[stack[-1]]:
            idx = stack.pop()
            result[idx] = nums[i]
        
        stack.append(i)
    
    return result

def nextGreaterElementCircular(nums):
    """
    LeetCode 503: Next Greater Element II
    Find next greater element in circular array
    """
    n = len(nums)
    result = [-1] * n
    stack = []
    
    # Process array twice to handle circular nature
    for i in range(2 * n):
        actual_i = i % n
        
        while stack and nums[actual_i] > nums[stack[-1]]:
            idx = stack.pop()
            result[idx] = nums[actual_i]
        
        # Only add to stack in first pass
        if i < n:
            stack.append(actual_i)
    
    return result

def nextGreaterElementMapping(nums1, nums2):
    """
    LeetCode 496: Next Greater Element I
    Find next greater elements for nums1 elements in nums2
    """
    # Create mapping from nums2 to next greater elements
    next_greater = {}
    stack = []
    
    for num in nums2:
        while stack and num > stack[-1]:
            next_greater[stack.pop()] = num
        stack.append(num)
    
    # Map results for nums1
    return [next_greater.get(num, -1) for num in nums1]

def dailyTemperatures(temperatures):
    """
    LeetCode 739: Daily Temperatures
    Find how many days until warmer temperature
    """
    n = len(temperatures)
    result = [0] * n
    stack = []
    
    for i in range(n):
        while stack and temperatures[i] > temperatures[stack[-1]]:
            idx = stack.pop()
            result[idx] = i - idx  # Days difference
        
        stack.append(i)
    
    return result

class StockSpanner:
    """
    LeetCode 901: Online Stock Span
    Find span of stock prices (consecutive days with price <= today)
    """
    def __init__(self):
        self.stack = []  # (price, span)
    
    def next(self, price):
        span = 1
        
        # Merge with previous spans
        while self.stack and self.stack[-1][0] <= price:
            span += self.stack.pop()[1]
        
        self.stack.append((price, span))
        return span

def nextLargerNodes(head):
    """
    LeetCode 1019: Next Greater Node In Linked List
    Find next greater element in linked list
    """
    values = []
    curr = head
    
    # Convert linked list to array
    while curr:
        values.append(curr.val)
        curr = curr.next
    
    return nextGreaterElement(values)

def finalPrices(prices):
    """
    LeetCode 1475: Final Prices With a Special Discount
    Find next smaller or equal element (discount)
    """
    n = len(prices)
    result = prices[:]  # Copy original prices
    stack = []
    
    for i in range(n):
        # While current price can be discount for stack top
        while stack and prices[i] <= prices[stack[-1]]:
            idx = stack.pop()
            result[idx] -= prices[i]  # Apply discount
        
        stack.append(i)
    
    return result

def nextSmallerElement(nums):
    """
    Find next smaller element for each element
    (Variation of next greater element pattern)
    """
    n = len(nums)
    result = [-1] * n
    stack = []
    
    for i in range(n):
        while stack and nums[i] < nums[stack[-1]]:
            idx = stack.pop()
            result[idx] = nums[i]
        
        stack.append(i)
    
    return result

def previousGreaterElement(nums):
    """
    Find previous greater element for each element
    (Process array from left to right, but find previous)
    """
    n = len(nums)
    result = [-1] * n
    stack = []
    
    for i in range(n):
        # Remove smaller elements from stack
        while stack and nums[stack[-1]] <= nums[i]:
            stack.pop()
        
        # Previous greater element is current stack top
        if stack:
            result[i] = nums[stack[-1]]
        
        stack.append(i)
    
    return result

def previousSmallerElement(nums):
    """
    Find previous smaller element for each element
    """
    n = len(nums)
    result = [-1] * n
    stack = []
    
    for i in range(n):
        # Remove greater or equal elements from stack
        while stack and nums[stack[-1]] >= nums[i]:
            stack.pop()
        
        # Previous smaller element is current stack top
        if stack:
            result[i] = nums[stack[-1]]
        
        stack.append(i)
    
    return result

def longestWellPerformingInterval(hours):
    """
    LeetCode 1124: Longest Well-Performing Interval
    Convert to next greater element problem with prefix sums
    """
    n = len(hours)
    # Convert to +1 for >8 hours, -1 for <=8 hours
    transformed = [1 if h > 8 else -1 for h in hours]
    
    # Find longest subarray with positive sum using monotonic stack
    prefix = [0]
    for x in transformed:
        prefix.append(prefix[-1] + x)
    
    stack = []
    # Build decreasing stack of indices
    for i in range(len(prefix)):
        if not stack or prefix[i] < prefix[stack[-1]]:
            stack.append(i)
    
    max_len = 0
    # Process from right to left
    for i in range(len(prefix) - 1, -1, -1):
        while stack and prefix[i] > prefix[stack[-1]]:
            max_len = max(max_len, i - stack.pop())
    
    return max_len

# Generic template for monotonic stack problems
def monotonic_stack_template(nums, comparison_func, initial_value=-1):
    """
    Generic template for monotonic stack problems
    
    Args:
        nums: input array
        comparison_func: function(current, stack_top) -> bool
                        True if current should pop stack_top
        initial_value: default value when no element found
    """
    n = len(nums)
    result = [initial_value] * n
    stack = []
    
    for i in range(n):
        while stack and comparison_func(nums[i], nums[stack[-1]]):
            idx = stack.pop()
            result[idx] = nums[i]
        
        stack.append(i)
    
    return result

# Example usage of generic template
def next_greater_with_template(nums):
    return monotonic_stack_template(
        nums, 
        lambda curr, stack_top: curr > stack_top,
        -1
    )

def next_smaller_with_template(nums):
    return monotonic_stack_template(
        nums,
        lambda curr, stack_top: curr < stack_top,
        -1
    )