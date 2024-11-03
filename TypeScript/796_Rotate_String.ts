/*
'''
796. Rotate String

Given two strings s and goal, return true if and only if s can become goal after some number
of shifts on s.

A shift on s consists of moving the leftmost character of s to the rightmost position.

For example, if s = "abcde", then it will be "bcdea" after one shift.
 

Example 1:

Input: s = "abcde", goal = "cdeab"
Output: true
Example 2:

Input: s = "abcde", goal = "abced"
Output: false


'''

'''
Solution: 

You can use brute force to check every possible candidate, or you can advantage of string concatenation. 
If you concatenate s with itself its easy to check if goal is located within it. 
'''
*/

function rotateString(s: string, goal: string): boolean {
    
    return goal.length === s.length && (s + s).includes(goal)
    
};