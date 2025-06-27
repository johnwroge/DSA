# Monotonic Stack & Queue Algorithms

This repository contains implementations of three fundamental patterns using monotonic data structures: **Largest Rectangle in Histogram**, **Next Greater Element**, and **Maximum Sliding Window**.

## What are Monotonic Data Structures?

**Monotonic Stack/Queue**: A data structure where elements are arranged in either strictly increasing or decreasing order. When a new element violates this property, elements are removed until the property is restored.

Key insight: These structures help us efficiently find **relationships between elements** based on their relative order and position.

## Algorithm Overview

| Pattern | Data Structure | Time | Space | Key Use Case |
|---------|---------------|------|-------|--------------|
| **Next Greater Element** | Monotonic Stack | O(n) | O(n) | Find next/previous larger/smaller elements |
| **Largest Rectangle** | Monotonic Stack | O(n) | O(n) | Find optimal rectangles in histograms |
| **Sliding Window Maximum** | Monotonic Deque | O(n) | O(k) | Track extremum in moving windows |

## 1. Next Greater Element Pattern

### 🎯 Core Concept
Find the next greater/smaller element for each element in an array.

### ⚙️ How it Works
- Maintain a **decreasing stack** (for next greater)
- When current element is larger, it's the "next greater" for stack elements
- Pop smaller elements and record the relationship

### 📝 Common Variations
- **Next Greater**: Find next larger element
- **Previous Greater**: Find previous larger element  
- **Next/Previous Smaller**: Find next/previous smaller element
- **Circular Array**: Handle wrap-around cases

### 🎯 LeetCode Problems
- **496. Next Greater Element I** - Basic pattern with mapping
- **503. Next Greater Element II** - Circular array handling
- **739. Daily Temperatures** - Count days until warmer
- **901. Online Stock Span** - Count consecutive smaller/equal elements
- **1019. Next Greater Node In Linked List** - Apply to linked structures

### 💡 Key Recognition Patterns
```
"Find the next/previous larger/smaller element..."
"How many days until..."
"Count consecutive elements where..."
"Find the span/range where condition holds..."
```

## 2. Largest Rectangle in Histogram Pattern

### 🎯 Core Concept
Find the largest rectangle that can be formed in a histogram, or solve related area optimization problems.

### ⚙️ How it Works
- For each bar, find how far left and right the rectangle can extend
- Use monotonic stack to efficiently find boundaries
- Calculate area = height × width for each possible rectangle

### 📝 Common Variations
- **Single Row**: Basic histogram problem
- **Multiple Rows**: Convert 2D matrix to multiple histogram problems
- **Count Rectangles**: Count all valid rectangles instead of finding maximum
- **Custom Conditions**: Rectangle must satisfy additional constraints

### 🎯 LeetCode Problems
- **84. Largest Rectangle in Histogram** - Core pattern
- **85. Maximal Rectangle** - 2D extension using multiple histograms
- **1504. Count Submatrices With All Ones** - Count instead of maximize
- **1793. Maximum Score of a Good Subarray** - Rectangle with position constraint

### 💡 Key Recognition Patterns
```
"Largest rectangle/square in..."
"Maximum area of..."
"Count rectangles/submatrices where..."
"Find optimal subarray where min × length is maximized..."
```

## 3. Maximum Sliding Window Pattern

### 🎯 Core Concept
Efficiently track the maximum/minimum element in a sliding window of fixed or variable size.

### ⚙️ How it Works
- Use **monotonic deque** to store potential maximums/minimums
- Front of deque always contains the current extremum
- Remove elements outside window and maintain monotonic property

### 📝 Common Variations
- **Fixed Window**: Window size is constant
- **Variable Window**: Window size changes based on conditions
- **Min/Max Tracking**: Track both minimum and maximum simultaneously
- **Complex Conditions**: Window validity depends on multiple factors

### 🎯 LeetCode Problems
- **239. Sliding Window Maximum** - Core fixed window pattern
- **1438. Longest Continuous Subarray With Absolute Diff Less Than or Equal to Limit** - Variable window with min/max tracking
- **862. Shortest Subarray with Sum at Least K** - Monotonic deque with prefix sums
- **480. Sliding Window Median** - Track median instead of min/max

### 💡 Key Recognition Patterns
```
"Maximum/minimum in sliding window..."
"Longest subarray where max - min ≤ ..."
"Shortest subarray with sum ≥ ..."
"Find optimal window where condition holds..."
```

## When to Use Each Pattern

### 🔍 Pattern Selection Guide

| Problem Description | Pattern to Use | Key Indicator |
|-------------------|----------------|---------------|
| "Next/previous larger element" | Next Greater Element | Relationship between adjacent elements |
| "Largest rectangle/area" | Largest Rectangle | Area optimization in histogram-like data |
| "Maximum in sliding window" | Sliding Window Maximum | Extremum tracking in moving window |
| "Count valid subarrays" | Combination | May need multiple patterns |

### 🎯 Quick Decision Tree

```
Does the problem involve...

📊 Histogram or bar heights?
└── Use Largest Rectangle pattern

🔄 Finding next/previous relationships?
└── Use Next Greater Element pattern

🪟 Moving window with min/max tracking?
└── Use Sliding Window Maximum pattern

📈 Multiple patterns combined?
└── Break down into subproblems
```

## Implementation Strategies

### 1. Next Greater Element Strategy
```python
# Template for finding next greater elements
def nextGreaterElements(nums):
    result = [-1] * len(nums)
    stack = []
    
    for i, num in enumerate(nums):
        while stack and num > nums[stack[-1]]:
            result[stack.pop()] = num
        stack.append(i)
    
    return result
```

### 2. Largest Rectangle Strategy
```python
# Template for rectangle problems
def largestRectangle(heights):
    stack = []
    max_area = 0
    
    for i, h in enumerate(heights):
        while stack and h < heights[stack[-1]]:
            height = heights[stack.pop()]
            width = i if not stack else i - stack[-1] - 1
            max_area = max(max_area, height * width)
        stack.append(i)
    
    return max_area
```

### 3. Sliding Window Maximum Strategy
```python
# Template for sliding window extremum
def slidingWindowMaximum(nums, k):
    from collections import deque
    dq = deque()
    result = []
    
    for i, num in enumerate(nums):
        # Remove outside window
        while dq and dq[0] <= i - k:
            dq.popleft()
        
        # Maintain decreasing order
        while dq and num >= nums[dq[-1]]:
            dq.pop()
        
        dq.append(i)
        
        if i >= k - 1:
            result.append(nums[dq[0]])
    
    return result
```

## Common Pitfalls and Tips

### ⚠️ Common Mistakes
1. **Wrong Stack Order**: Using increasing instead of decreasing stack (or vice versa)
2. **Index vs Value**: Storing values instead of indices in stack
3. **Boundary Conditions**: Not handling empty arrays or single elements
4. **Window Maintenance**: Forgetting to remove elements outside sliding window
5. **Sentinel Values**: Not adding sentinel values when they simplify logic

### 💡 Pro Tips

1. **Always store indices** in monotonic structures (not values)
2. **Add sentinel values** (0 or infinity) to avoid edge cases
3. **Draw examples** to understand which monotonic order you need
4. **Process remaining stack** elements after main loop
5. **Use templates** and adapt them to specific problem constraints

## Problem-Solving Approach

### 🔄 Step-by-Step Process

1. **Identify the Pattern**
   - What relationship are you trying to find?
   - Is it about next/previous elements, rectangles, or sliding windows?

2. **Choose Monotonic Order**
   - Decreasing stack: for finding next greater elements
   - Increasing stack: for finding next smaller elements
   - Depends on what you want to "see" first

3. **Handle Edge Cases**
   - Empty arrays
   - Single elements
   - All increasing/decreasing sequences

4. **Optimize with Sentinels**
   - Add dummy elements to simplify boundary handling
   - Often eliminates need for separate edge case handling

## Advanced Applications

### 🚀 Real-World Uses
- **Financial Analysis**: Stock span calculation, trend analysis
- **Image Processing**: Finding largest rectangles in binary images
- **System Monitoring**: Tracking metrics in sliding time windows
- **Game Development**: Line-of-sight calculations, collision detection
- **Data Analytics**: Moving averages, outlier detection

### 🧠 Interview Strategy
1. **Recognize the pattern** quickly (practice makes perfect)
2. **Start with brute force** to show understanding
3. **Explain the optimization** using monotonic structures
4. **Code the template** and adapt to specific constraints
5. **Test with edge cases** and trace through examples

Choose the pattern that matches your problem's core requirements, and remember: monotonic structures excel at finding **relationships and boundaries** efficiently!