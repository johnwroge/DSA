'''
The Fibonacci sequence is defined by the recurrence relation:

Fn = Fn - 1 + Fn - 2 where F1 = 1 and F2 = 1

Hence the first 12 terms will be: 0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144

What is the index of the first term in the Fibonacci sequence to contain 1000 digits.

'''

'''
solution: 1000 digit fibonacci number is very large so I am not sure if brute force will work.
for very large numbers, there are other approaches that can be used. 
'''

def Solution():
    curr = '1'
    fib = [0,1,1]
    while len(curr) < 1000:
        next = fib[-1] + fib[-2]
        curr = str(next)
        fib.append(next)
    
    return len(fib) - 1

# print(Solution())




        

