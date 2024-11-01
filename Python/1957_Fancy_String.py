'''
1957. Delete Characters to Make Fancy String

A fancy string is a string where no three consecutive characters are equal.

Given a string s, delete the minimum possible number of characters from s to make 
it fancy.

Return the final string after the deletion. It can be shown that the answer will always
be unique.

 

Example 1:

Input: s = "leeetcode"
Output: "leetcode"
Explanation:
Remove an 'e' from the first group of 'e's to create "leetcode".
No three consecutive characters are equal, so return "leetcode".
Example 2:

Input: s = "aaabaaaa"
Output: "aabaa"
Explanation:
Remove an 'a' from the first group of 'a's to create "aabaaaa".
Remove two 'a's from the second group of 'a's to create "aabaa".
No three consecutive characters are equal, so return "aabaa".
Example 3:

Input: s = "aab"
Output: "aab"
Explanation: No three consecutive characters are equal, so return "aab".
'''

# approach 1 - use sliding window and maintain dynamic count

class Solution:
    def makeFancyString(self, s: str) -> str:
        count = {}
        for i in range(0, min(len(s), 2)):
            count[s[i]] = count.get(s[i], 0) + 1
        letters = list(s)
        l = 0
        for j in range(2, len(s)):
            count[s[j]] = count.get(s[j], 0) + 1
            if count[s[j]] == 3:
                letters[j] = ''
            count[s[l]] -= 1
            l += 1
        return ''.join(letters)



# approach 2 - track previous character and use stack 

class Solution:
    def makeFancyString(self, s: str) -> str:
        prev = ''
        stack = []
        count = 1
        for c in s:
            if c != prev:
                count = 1
                stack.append(c)
            else:
                count += 1
                if count < 3:
                    stack.append(c)
            prev = c
        return ''.join(stack)