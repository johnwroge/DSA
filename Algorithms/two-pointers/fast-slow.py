"""
LeetCode Problems where Fast-Slow Pointers can be applied:

141. Linked List Cycle
142. Linked List Cycle II
876. Middle of the Linked List
143. Reorder List
234. Palindrome Linked List
457. Circular Array Loop
287. Find the Duplicate Number
202. Happy Number
"""

# Definition for singly-linked list
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def has_cycle(head):
    """
    LeetCode 141: Linked List Cycle
    Basic cycle detection using Floyd's algorithm
    
    Time: O(n), Space: O(1)
    """
    if not head or not head.next:
        return False
    
    slow = fast = head
    
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
        
        if slow == fast:
            return True
    
    return False

def detect_cycle(head):
    """
    LeetCode 142: Linked List Cycle II
    Find the start of the cycle
    
    Time: O(n), Space: O(1)
    """
    if not head or not head.next:
        return None
    
    # Phase 1: Detect cycle
    slow = fast = head
    
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
        
        if slow == fast:
            break
    else:
        return None  # No cycle
    
    # Phase 2: Find cycle start
    slow = head
    while slow != fast:
        slow = slow.next
        fast = fast.next
    
    return slow

def find_middle(head):
    """
    LeetCode 876: Middle of the Linked List
    Find middle node of linked list
    
    Time: O(n), Space: O(1)
    """
    if not head:
        return None
    
    slow = fast = head
    
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
    
    return slow

def is_palindrome(head):
    """
    LeetCode 234: Palindrome Linked List
    Check if linked list is palindrome
    
    Time: O(n), Space: O(1)
    """
    if not head or not head.next:
        return True
    
    # Find middle
    slow = fast = head
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
    
    # Reverse second half
    def reverse_list(node):
        prev = None
        while node:
            next_node = node.next
            node.next = prev
            prev = node
            node = next_node
        return prev
    
    second_half = reverse_list(slow)
    
    # Compare first half with reversed second half
    first_half = head
    while second_half:
        if first_half.val != second_half.val:
            return False
        first_half = first_half.next
        second_half = second_half.next
    
    return True

def reorder_list(head):
    """
    LeetCode 143: Reorder List
    Reorder list: L0 → L1 → … → Ln-1 → Ln to L0 → Ln → L1 → Ln-1 → L2 → Ln-2 → …
    
    Time: O(n), Space: O(1)
    """
    if not head or not head.next:
        return
    
    # Find middle
    slow = fast = head
    while fast.next and fast.next.next:
        slow = slow.next
        fast = fast.next.next
    
    # Split into two halves
    second_half = slow.next
    slow.next = None
    
    # Reverse second half
    def reverse_list(node):
        prev = None
        while node:
            next_node = node.next
            node.next = prev
            prev = node
            node = next_node
        return prev
    
    second_half = reverse_list(second_half)
    
    # Merge two halves
    first_half = head
    while second_half:
        temp1 = first_half.next
        temp2 = second_half.next
        
        first_half.next = second_half
        second_half.next = temp1
        
        first_half = temp1
        second_half = temp2

def find_duplicate(nums):
    """
    LeetCode 287: Find the Duplicate Number
    Find duplicate in array using cycle detection
    
    Time: O(n), Space: O(1)
    """
    # Phase 1: Detect cycle
    slow = fast = nums[0]
    
    while True:
        slow = nums[slow]
        fast = nums[nums[fast]]
        if slow == fast:
            break
    
    # Phase 2: Find entrance to cycle
    slow = nums[0]
    while slow != fast:
        slow = nums[slow]
        fast = nums[fast]
    
    return slow

def is_happy(n):
    """
    LeetCode 202: Happy Number
    Check if number is happy using cycle detection
    
    Time: O(log n), Space: O(1)
    """
    def get_sum_of_squares(num):
        total = 0
        while num > 0:
            digit = num % 10
            total += digit * digit
            num //= 10
        return total
    
    slow = fast = n
    
    while True:
        slow = get_sum_of_squares(slow)
        fast = get_sum_of_squares(get_sum_of_squares(fast))
        
        if fast == 1:
            return True
        if slow == fast:
            return False

def circular_array_loop(nums):
    """
    LeetCode 457: Circular Array Loop
    Check if array has a cycle
    
    Time: O(n), Space: O(1)
    """
    n = len(nums)
    
    def get_next(index):
        return (index + nums[index]) % n
    
    for i in range(n):
        if nums[i] == 0:
            continue
        
        # Check for single element cycle
        if get_next(i) == i:
            continue
        
        slow = fast = i
        
        # Check if all elements in cycle have same direction
        while (nums[fast] * nums[get_next(fast)] > 0 and 
               nums[slow] * nums[get_next(slow)] > 0):
            slow = get_next(slow)
            fast = get_next(get_next(fast))
            
            if slow == fast:
                return True
    
    return False

# Generic fast-slow template
def fast_slow_template(start_value, next_function, condition_function):
    """
    Generic template for fast-slow pointer problems
    
    Args:
        start_value: Starting value for both pointers
        next_function: Function to get next value
        condition_function: Function to check termination condition
    
    Returns:
        Result based on specific problem requirements
    """
    slow = fast = start_value
    
    # Phase 1: Move pointers until they meet or reach end
    while fast is not None and next_function(fast) is not None:
        slow = next_function(slow)
        fast = next_function(next_function(fast))
        
        if condition_function(slow, fast):
            break
    
    # Phase 2: Additional processing if needed
    # (e.g., finding cycle start, middle element, etc.)
    
    return slow  # or whatever the problem requires

# Array-based fast-slow (for problems like finding duplicate)
def array_fast_slow_template(nums):
    """
    Template for array-based fast-slow problems
    where indices are used as "pointers"
    """
    slow = fast = 0  # or nums[0] depending on problem
    
    # Phase 1: Detect cycle/meeting point
    while True:
        slow = nums[slow]
        fast = nums[nums[fast]]
        
        if slow == fast:
            break
    
    # Phase 2: Find specific position (cycle start, etc.)
    slow = 0  # Reset slow to beginning
    while slow != fast:
        slow = nums[slow]
        fast = nums[fast]
    
    return slow