'''
1593. Split a String Into the Max Number of Unique Substrings
Solved
Medium
Topics
Companies
Hint
Given a string s, return the maximum number of unique substrings that the given string 
can be split into.

You can split string s into any list of non-empty substrings, where the concatenation 
of the substrings forms the original string. However, you must split the substrings
 such that all of them are unique.

A substring is a contiguous sequence of characters within a string.

 

Example 1:

Input: s = "ababccc"
Output: 5
Explanation: One way to split maximally is ['a', 'b', 'ab', 'c', 'cc']. 
Splitting like ['a', 'b', 'a', 'b', 'c', 'cc'] is not valid as you have 
'a' and 'b' multiple times.
Example 2:

Input: s = "aba"
Output: 2
Explanation: One way to split maximally is ['a', 'ba'].
Example 3:

Input: s = "aa"
Output: 1
Explanation: It is impossible to split the string any further.
 



'''


class Solution:
    def maxUniqueSplit(self, s: str) -> int:
        # use a set to keep track of unique substrings
        seen = set()
        def backtrack(s, start, seen):
            # if start reaches 0, we've successfully split the entire string 
            # and no more substrings can be added so we return 0
            if start == len(s):
                return 0
            # initialize max count to 0 because we want to explore the max count from splitting
            # the string based on every position 
            max_count = 0

            # use a loop to explore next substring
            for end in range(start + 1, len(s) + 1):
                sub_string = s[start:end]
                if sub_string not in seen:
                    seen.add(sub_string)
                    max_count = max(max_count, 1 + backtrack(s, end, seen))
                    seen.remove(sub_string)

            # return the final max count
            return max_count
        
        return backtrack(s, 0, seen)



# optimized using pruning
class Solution:
    def maxUniqueSplit(self, s: str) -> int:
        seen = set()
        max_count = [0]
        def backtrack(self, s: str, start: int, seen: set, count: int, max_count: list):
            if count + (len(s) - start) <= max_count[0]:
                return
            
            if start == len(s):
                max_count[0] = max(max_count[0], count)
                return
            
            for end in range(start + 1, len(s) + 1):
                sub_string = s[start:end]
                if sub_string not in seen:
                    seen.add(sub_string)
                    self.backtrack(s, end, seen, count + 1, max_count)
                    seen.remove(sub_string)
            return
        self.backtrack(s, 0, seen, 0, max_count)
        return max_count[0]

    