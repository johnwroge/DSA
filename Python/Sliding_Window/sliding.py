'''
Problem:
You are given an array of integers, and you need to find the length of the 
longest contiguous subarray where the difference between the maximum and minimum 
element is less than or equal to 1.

Example:
Input: [1, 3, 2, 2, 2, 1, 4, 2]
Output: 5
Explanation: The longest contiguous subarray where the difference between the max 
and min is ≤ 1 is [3, 2, 2, 2, 2].
'''


from collections import Counter

def sliding(arr):
    l = 0
    max_l = 0
    count = Counter()
    
    for r in range(len(arr)):
        count[arr[r]] += 1
        
        while max(count) - min(count) > 1:
            count[arr[l]] -= 1
            if count[arr[l]] == 0:
                del count[arr[l]]
            l += 1
        
        max_l = max(max_l, r - l + 1)
    
    return max_l


print(sliding([1, 3, 2, 2, 2, 1, 4, 2]))