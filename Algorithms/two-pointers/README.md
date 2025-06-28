# Two Pointers Algorithms

This repository contains basic templates for the four main two-pointer patterns that can be adapted to solve most two-pointer problems.

## Algorithm Overview

| Pattern | Description | Time | Space | Common Use Cases |
|---------|-------------|------|-------|------------------|
| **Fast-Slow** | Two pointers moving at different speeds | O(n) | O(1) | Cycle detection, finding middle |
| **Left-Right** | Two pointers from opposite ends | O(n) | O(1) | Two sum, palindromes, containers |
| **Three Pointers** | One fixed + two moving pointers | O(n²) | O(1) | 3Sum, triplet problems |
| **Multiple Pointers** | Read/write or partitioning pointers | O(n) | O(1) | Array modification, partitioning |

## Quick Pattern Recognition

### 🐢🐰 Fast-Slow Pointers
**When to use**: 
- Linked list problems
- Cycle detection
- Finding middle elements
- Array problems where indices act as "pointers"

**Key insight**: Fast pointer moves 2 steps, slow moves 1 step

**Common patterns**:
```
"find cycle", "middle of linked list", "duplicate number"
"detect loop", "palindrome linked list"
```

### ⬅️➡️ Left-Right Pointers  
**When to use**:
- Sorted arrays
- Two sum problems
- Palindrome checking
- Container/area problems

**Key insight**: Start from both ends, move based on comparison

**Common patterns**:
```
"two sum", "container with most water", "valid palindrome"
"sorted array", "opposite ends", "squeeze towards middle"
```

### 🔢 Three Pointers
**When to use**:
- 3Sum, 4Sum problems
- Finding triplets
- Problems requiring one fixed + two moving pointers

**Key insight**: Fix one element, use two pointers for the rest

**Common patterns**:
```
"3sum", "triplets", "three numbers", "quadruplets"
"closest to target", "smaller than target"
```

### 📝 Multiple Pointers
**When to use**:
- Array modification in-place
- Partitioning arrays
- Removing/moving elements
- Separating different types of elements

**Key insight**: Often read pointer and write pointer

**Common patterns**:
```
"remove duplicates", "move zeros", "sort colors"
"in-place", "modify array", "partition"
```

## Decision Tree

```
What type of problem is it?

🔗 Linked List or Cycle Detection?
└── Use Fast-Slow Pointers

📊 Sorted Array with Target Sum?
└── Use Left-Right Pointers

🎯 Find Triplets or 3Sum-style?
└── Use Three Pointers

✏️ Modify Array In-Place?
└── Use Multiple Pointers

🪟 Fixed/Sliding Window?
└── Consider Sliding Window (not covered here)
```

## Basic Templates

### Fast-Slow Template
```python
def fast_slow_template(head):
    slow = fast = head
    
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
        
        if slow == fast:  # Cycle detected or other condition
            break
    
    return slow  # or process further
```

### Left-Right Template  
```python
def left_right_template(arr, target):
    left, right = 0, len(arr) - 1
    
    while left < right:
        current_sum = arr[left] + arr[right]
        
        if current_sum == target:
            return [left, right]
        elif current_sum < target:
            left += 1
        else:
            right -= 1
    
    return [-1, -1]
```

### Three Pointers Template
```python
def three_pointers_template(nums, target):
    nums.sort()
    result = []
    
    for i in range(len(nums) - 2):
        if i > 0 and nums[i] == nums[i-1]:
            continue
            
        left, right = i + 1, len(nums) - 1
        
        while left < right:
            current_sum = nums[i] + nums[left] + nums[right]
            
            if current_sum == target:
                result.append([nums[i], nums[left], nums[right]])
                left += 1
                right -= 1
            elif current_sum < target:
                left += 1
            else:
                right -= 1
    
    return result
```

### Multiple Pointers Template
```python
def multiple_pointers_template(nums):
    write_ptr = 0
    
    for read_ptr in range(len(nums)):
        if condition(nums[read_ptr]):  # Define your condition
            nums[write_ptr] = nums[read_ptr]
            write_ptr += 1
    
    return write_ptr
```

## Common Mistakes to Avoid

1. **Off-by-one errors**: Be careful with loop conditions and pointer updates
2. **Infinite loops**: Ensure pointers move in each iteration
3. **Duplicate handling**: Remember to skip duplicates in sorted arrays
4. **Null pointer**: Check for null/empty inputs
5. **Index bounds**: Ensure pointers stay within array bounds

## Practice Progression

1. **Start with basic two sum** (left-right pattern)
2. **Learn cycle detection** (fast-slow pattern)  
3. **Master 3sum** (three pointers pattern)
4. **Practice array modification** (multiple pointers)
5. **Combine patterns** for complex problems

## Key Tips

- **Always consider if array needs to be sorted first**
- **Two pointers usually gives O(n) or O(n²) time complexity**
- **Space complexity is typically O(1)**
- **Draw diagrams to visualize pointer movement**
- **Test with edge cases**: empty arrays, single elements, duplicates**

Choose the pattern that matches your problem structure and adapt the basic template as needed!