'''
541

Given a string s and an integer k, reverse the first k characters for every 2k characters
 counting from the start of the string.

If there are fewer than k characters left, reverse all of them. If there are less than 2k 
but greater than or equal to k characters, then reverse the first k characters and leave
 the other as original.


Example 1:

Input: s = "abcdefg", k = 2
Output: "bacdfeg"
Example 2:

Input: s = "abcd", k = 2
Output: "bacd"

'''

''' 
Strings are not mutable in python, so the best way to do this is convert the string to
a list and then perform the operations needed. 
'''


def reverseStr(s: str, k: int) -> str:
    list_string = list(s)
    for i in range(0, len(s), 2*k):
        print(i)
        list_string[i: i + k] = reversed(list_string[i: i + k])
    
    return ''.join(list_string)

print(reverseStr("abcd", 2))

            
