from collections import Counter
'''
76. Minimum Window Substring
Solved
Hard
Topics
Companies
Hint
Given two strings s and t of lengths m and n respectively, return the minimum window 
substring
 of s such that every character in t (including duplicates) is included in the window.
   If there is no such substring, return the empty string "".

The testcases will be generated such that the answer is unique.

 

Example 1:

Input: s = "ADOBECODEBANC", t = "ABC"
Output: "BANC"
Explanation: The minimum window substring "BANC" includes 'A', 'B', and 'C' from string t.
Example 2:

Input: s = "a", t = "a"
Output: "a"
Explanation: The entire string s is the minimum window.
Example 3:

Input: s = "a", t = "aa"
Output: ""
Explanation: Both 'a's from t must be included in the window.
Since the largest window of s only has one 'a', return empty string.
 

Constraints:

m == s.length
n == t.length
1 <= m, n <= 105
s and t consist of uppercase and lowercase English letters.
 

Follow up: Could you find an algorithm that runs in O(m + n) time?


approach:

use a hashmap for smaller string s and t. initialize t hash to have initial counts
iterate over s while adding to s hash. check if both counts are eq
'''



class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if t == "":
            return "" 
        
        window, countT = {}, {}
        for c in t:
            countT[c] = countT.get(c,0) + 1

        have, need = 0, len(countT)
        minL, res = float("inf"), [-1, -1]
        l = 0
       
        for r in range(len(s)):
            c = s[r]
            window[c] = window.get(c,0) + 1 

            if c in countT and window[c] == countT[c]:
                have += 1   

            while have == need:
                if (r - l + 1) < minL:
                    res = [l, r]
                    minL = (r - l + 1)
                window[s[l]] -= 1
                if s[l] in countT and window[s[l]] < countT[s[l]]:
                    have -= 1
                l += 1
        l, r = res
        return s[l:r + 1] if minL != float("inf") else ""             
                
# s = "ADOBECODEBANC" 
s = "AdBeCabc"
t = "abc"
solution = Solution()
print(solution.minWindow(s,t))
