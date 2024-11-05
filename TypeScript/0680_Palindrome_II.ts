

/*
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
 

Constraints:

1 <= s.length <= 105
s consists of lowercase English letters.
*/

var validPalindrome = function(s: string) {

    const search = (l: number, r: number, removed: boolean): boolean => {
        while (l < r){
            if (s[l] != s[r]){
                if (removed) return false;
                removed = true;
                return search(l + 1, r, true) || search(l, r - 1, true);
            }
            l += 1;
            r -= 1;
        }
        return true

    }

   return search(0, s.length - 1, false);
};