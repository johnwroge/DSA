'''
345. Reverse Vowels of a String


Given a string s, reverse only all the vowels in the string and return it.

The vowels are 'a', 'e', 'i', 'o', and 'u', and they can appear in both lower and upper cases, more than once.

 

Example 1:

Input: s = "IceCreAm"

Output: "AceCreIm"

Explanation:

The vowels in s are ['I', 'e', 'e', 'A']. On reversing the vowels, s becomes "AceCreIm".

Example 2:

Input: s = "leetcode"

Output: "leotcede"
'''

class Solution:
    def reverseVowels(self, s: str) -> str:
        found = []
        s = list(s)
        vowels = set(['a','A','i', 'I', 'o', 'O', 'u', 'U', 'e', 'E'])
        for i in range(len(s)):
            if s[i] in vowels:
                found.append(s[i])
        found.reverse()
        j = 0
        for i in range(len(s)):
            if s[i] in vowels:
                s[i] = found[j]
                j += 1
        return ''.join(s)