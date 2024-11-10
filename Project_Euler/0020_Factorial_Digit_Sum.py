'''
n! mean n x (n-1) x ... x 3 x 2 x 1

For example 10! = 10 x 9 x 8 x 7 x ... 2 x 1 = 3628800

and the sum of the digits is 27.

Find the sum of the digits in the number 100!
'''

def find_factorial(n):
    
    if n == 1:
        return 1

    return n * find_factorial(n - 1)

factorial = str(find_factorial(100))

answer = sum(int(n) for n in factorial)

print(answer)


        