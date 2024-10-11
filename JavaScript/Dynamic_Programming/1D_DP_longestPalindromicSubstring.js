/*
5. Longest Palindromic Substring
Medium
24K
1.4K
Companies
Given a string s, return the longest 
palindromic substring in s.

Example 1:

Input: s = "babad"
Output: "bab"
Explanation: "aba" is also a valid answer.
Example 2:

Input: s = "cbbd"
Output: "bb"
 

Constraints:

1 <= s.length <= 1000
s consist of only digits and English letters.
*/

/**
 * @param {string} s
 * @return {string}
 */
 var longestPalindrome = function(s) {
    
};

var longestPalindrome = function(s) {
    let str="";

    for(let i=0;i<s.length;i++){
        for(let j=0;j<2;j++){
            let left=i;
            let right=left+j;
            while(s[left]&&s[left]===s[right]){
                left--;
                right++;
            }
            if(right-left-1>str.length){
                str=s.slice(left+1,right);
            }
        }
    }
    return str;
};

/*
647. Palindromic Substrings
Medium
8.7K
188
Companies
Given a string s, return the number of palindromic substrings in it.

A string is a palindrome when it reads the same backward as forward.

A substring is a contiguous sequence of characters within the string.

 

Example 1:

Input: s = "abc"
Output: 3
Explanation: Three palindromic strings: "a", "b", "c".
Example 2:

Input: s = "aaa"
Output: 6
Explanation: Six palindromic strings: "a", "a", "a", "aa", "aa", "aaa".
 

Constraints:

1 <= s.length <= 1000
s consists of lowercase English letters.
*/

/**
 * @param {string} s
 * @return {number}
 */
 var countSubstrings = function(s) {
    
};

var countSubstrings = function(S) {
    let len = S.length, ans = 0
    for (let i = 0; i < len; i++) {
        let j = i - 1, k = i
        while (k < len - 1 && S[k] === S[k+1]) k++
        ans += (k - j) * (k - j + 1) / 2, i = k++
        while (~j && k < len && S[k] === S[j]) j--, k++, ans++
    }
    return ans
};