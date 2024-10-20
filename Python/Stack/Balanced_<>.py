'''
Consider a string consisting of the characters < and > only.
The string is balanced if each < always appears before (to the left of)
a corresponding > character (they do not need to be adjacent). Moreover, each
< and > act as a unique pair of symbols and neither symbol can be 
considered as part of any other pair of symbols.

To balance a string any > character can be replaced with <>. Given an expression
and a maximum number of replacements, determine whether the string
can be balanced.

e.g.
expressions = ['<<>>', '<>', '<><>', '>>', '<<>', '><><']
maxReplacements = [0, 1, 2, 2, 2, 2]

-> [true, true, true, true, false, false]

l_stack = []

if the last char is a <, it's false

iterate over characters

    if < -> append to the stack
    if > and there are items in the l_stack -> remove from the l_stack

    # or if there are no items in l stack and its a >  
        and there are <= 0 maxreplacements return false
        subtract from max replacements

        
    
is the l_stack empty? return true otherwise false
'''

# pycharm

def balanced(arr, k):
    left_stack = []
    for c in arr:
        if c == "<":
            left_stack.append(c)
        elif c == ">" and left_stack:
            left_stack.pop()
        elif c == ">" and not left_stack:
            if k <= 0:
                return False
            k -= 1
    return len(left_stack) == 0     


expressions = ['<<>>', '<>', '<><>', '>>', '<<>', '><><']
maxReplacements = [0, 1, 2, 2, 2, 2]

# -> [true, true, true, true, false, false]

# for e, k in zip(expressions, maxReplacements):
#     print(balanced(e, k))