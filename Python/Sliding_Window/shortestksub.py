from collections import Counter
'''
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
                
              

       
        return res
# s = "ADOBECODEBANC" 
s = "AdBeCabc"
t = "abc"
solution = Solution()
print(solution.minWindow(s,t))
