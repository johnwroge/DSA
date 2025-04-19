'''
1106. Parsing A Boolean Expression
Solved
Hard
Topics
Companies
Hint
A boolean expression is an expression that evaluates to either true or false.
 It can be in one of the following shapes:

't' that evaluates to true.
'f' that evaluates to false.
'!(subExpr)' that evaluates to the logical NOT of the inner expression subExpr.
'&(subExpr1, subExpr2, ..., subExprn)' that evaluates to the logical AND of the inner expressions subExpr1, subExpr2, ..., subExprn where n >= 1.
'|(subExpr1, subExpr2, ..., subExprn)' that evaluates to the logical OR of the inner expressions subExpr1, subExpr2, ..., subExprn where n >= 1.
Given a string expression that represents a boolean expression, return the evaluation of that expression.

It is guaranteed that the given expression is valid and follows the given rules.

 

Example 1:

Input: expression = "&(|(f))"
Output: false
Explanation: 
First, evaluate |(f) --> f. The expression is now "&(f)".
Then, evaluate &(f) --> f. The expression is now "f".
Finally, return false.
Example 2:

Input: expression = "|(f,f,f,t)"
Output: true
Explanation: The evaluation of (false OR false OR false OR true) is true.
Example 3:

Input: expression = "!(&(f,t))"
Output: true
Explanation: 
First, evaluate &(f,t) --> (false AND true) --> false --> f. The expression is now "!(f)".
Then, evaluate !(f) --> NOT false --> true. We return true.
 

Constraints:

1 <= expression.length <= 2 * 104
expression[i] is one following characters: '(', ')', '&', '|', '!', 't', 'f', and ','.

'''


class Solution:
    def parseBoolExpr(self, e: str) -> bool:
        stack = []
        ops = {"t": True, "f": False}
        for c in e:
            curr = []
            if c == ")":
                while stack and stack[-1] != "(":
                    curr.append(stack.pop())
                stack.pop()
                op = stack.pop()
                if op == "!":
                    if curr[-1] == "f":
                        stack.append('t')
                    else: 
                        stack.append('f')
                    curr.pop()
                    continue
                isTrue = True if curr[0] == "t" else False
                last = isTrue
                for b in curr:
                    if op == "&":
                        last = isTrue and ops[b]
                        isTrue = last
                        if last == False:
                            break
                    else:
                        last = isTrue or ops[b]
                        isTrue = last
                        if last == True:
                            break

                last = "t" if last == True else "f"
                stack.append(last)       
            else:
                if c != ",":
                    stack.append(c)
        return True if stack[0] == "t" else False