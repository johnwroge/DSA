'''
670. Maximum Swap
Solved
Medium
Topics
Companies
You are given an integer num. You can swap two digits at most
 once to get the maximum valued number.

Return the maximum valued number you can get.


Example 1:

Input: num = 2736
Output: 7236
Explanation: Swap the number 2 and the number 7.
Example 2:

Input: num = 9973
Output: 9973
Explanation: No swap.
 

Constraints:

0 <= num <= 108

'''


class Solution:
    def maximumSwap(self, num: int) -> int:
        s = list(str(num))
        n = len(s)
        # find index where s[i] < s[i+1], meaning a chance to flip
        for i in range(n-1):                             
            if s[i] < s[i+1]: break
        # if nothing find, return num
        else: return num               
        # keep going right, find the maximum value index             
        max_idx, max_val = i+1, s[i+1]                      
        for j in range(i+1, n):
            if max_val <= s[j]: max_idx, max_val = j, s[j]
        left_idx = i 
         # going right from i, find most left value that is less than max_val                                      
        for j in range(i, -1, -1):    
            if s[j] < max_val: left_idx = j
        # swap maximum after i and most left less than max
        s[max_idx], s[left_idx] = s[left_idx], s[max_idx]  
        return int(''.join(s))  