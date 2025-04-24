# Sliding Window Approaches: A Comprehensive Guide

## Introduction
The sliding window technique is a powerful algorithmic pattern used to solve array, string, and subsequence problems with optimal time complexity. This guide outlines the most common sliding window approaches, with templates and example problems.

## Core Sliding Window Patterns

### 1. Fixed-Size Sliding Window
**Description**: Maintains a window of fixed size k, sliding it through the array.  
**Example Problems**: 
- LC 643: Maximum Average Subarray I
- LC 1343: Number of Sub-arrays of Size K and Average Greater than Threshold
- LC 567: Permutation in String

### 2. Variable-Size Sliding Window (Minimum Length)
**Description**: Finds the smallest subarray satisfying certain conditions.  
**Example Problems**:
- LC 209: Minimum Size Subarray Sum
- LC 76: Minimum Window Substring
- LC 1004: Max Consecutive Ones III

### 3. Sliding Window with Frequency Counter
**Description**: Uses a hash map to track element frequencies while sliding the window.  
**Example Problems**:
- LC 992: Subarrays with K Different Integers
- LC 2302: Count Subarrays With Score Less Than K
- LC 1248: Count Number of Nice Subarrays

### 4. Sliding Window for Finding Longest Substring/Subarray
**Description**: Finds the longest contiguous sequence that satisfies certain conditions.  
**Example Problems**:
- LC 3: Longest Substring Without Repeating Characters
- LC 159: Longest Substring with At Most Two Distinct Characters
- LC 424: Longest Repeating Character Replacement

### 5. Sliding Window for Finding All Valid Subarrays
**Description**: Counts or collects all valid subarrays that satisfy given conditions.  
**Example Problems**:
- LC 713: Subarray Product Less Than K
- LC 2461: Maximum Sum of Distinct Subarrays With Length K
- LC 1876: Substrings of Size Three with Distinct Characters

## Advanced Sliding Window Techniques

### 6. Two-Pointer Sliding Window
**Description**: Uses two pointers that move toward each other based on comparison.  
**Example Problems**:
- LC 11: Container With Most Water
- LC 42: Trapping Rain Water
- LC 845: Longest Mountain in Array

### 7. Sliding Window with Monotonic Queue/Stack
**Description**: Combines sliding window with a monotonic queue for efficient min/max queries.  
**Example Problems**:
- LC 239: Sliding Window Maximum
- LC 1438: Longest Continuous Subarray With Absolute Diff Less Than or Equal to Limit
- LC 862: Shortest Subarray with Sum at Least K

### 8. Sliding Window with Two Heaps
**Description**: Uses min and max heaps to efficiently track statistics like median in a sliding window.  
**Example Problems**:
- LC 480: Sliding Window Median
- LC 295: Find Median from Data Stream (variation)

### 9. Sliding Window for String Matching
**Description**: Specialized for pattern matching in strings.  
**Example Problems**:
- LC 28: Find the Index of the First Occurrence in a String
- LC 30: Substring with Concatenation of All Words

### 10. Sliding Window with Bit Manipulation
**Description**: Combines sliding window concept with bit operations.  
**Example Problems**:
- LC 1461: Check If a String Contains All Binary Codes of Size K
- LC 1310: XOR Queries of a Subarray

## Key Implementation Tips

1. **Window Boundaries**: Always track both left and right boundaries of your window
2. **Expansion and Contraction**: Know when to expand (right pointer) and when to contract (left pointer)
3. **State Tracking**: Use appropriate data structures to track window state (sets, maps, heaps)
4. **Efficiency**: Process each element at most twice for O(n) time complexity
5. **Edge Cases**: Handle empty arrays, single-element arrays, and other edge cases

## Conclusion

The sliding window technique is versatile and can be adapted to solve a wide range of problems efficiently. Understanding these patterns allows you to quickly recognize when to apply sliding window algorithms and which variation to use for specific problem constraints.