'''
680. Valid Palindrome II

Given a string s, return true if the s can be palindrome after deleting at most one character from it.

Example 1:

Input: s = "aba"
Output: true
Example 2:

Input: s = "abca"
Output: true
Explanation: You could delete the character 'c'.
Example 3:

Input: s = "abc"
Output: false


'''

'''
Solution 1: 

Use two pointers and continue to increment left and decrement right as long as they match. 
Otherwise, we found a character that has to be removed so we have two options, remove the left character and
check if the remaining string on the inside matches its reverse, or remove the right character and do the same. 
If they match, return true otherwise return false 

We don't need to worry about the characters we already checked, so the inner string is all that needs to be reversed. 
If neither of those cases are true you can return True because the word is a palindrome.
'''

class Solution:
    def validPalindrome(self, s: str) -> bool:
        left = 0
        right = len(s)-1
        while left < right:
            if s[left] != s[right]:
                return s[left+1:right+1] == s[left+1:right+1][::-1]  or s[left:right] == s[left:right][::-1] 
            left += 1
            right -= 1
        return True   
    

'''
Solution 2: similar approach as above except we use recursion and a boolean flag. We remove the character and change 
the boolean flag to true we explore all possible solutions removing a character if it doesn't match. if we find a 
second character that doesn't match return False for that possible solution. Otherwise if all characters are exhausted
we return True. 
'''

class Solution:
    def validPalindrome(self, s: str) -> bool:
        def isValid(l, r, deleted):
            while l < r:
                if s[l] != s[r]:
                    if not deleted:
                        return isValid(l + 1, r, True) or isValid(l, r - 1, True)
                    else:
                        return False
                else:
                    l += 1
                    r -= 1
            return True
        return isValid(0, len(s) - 1, False)
        