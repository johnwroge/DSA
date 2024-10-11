'''
The sum of the squares of the first ten natural numbers is,
1^2 + 2^2 + ... + 10^2 = 385

The square of the sum of the first ten natural numbers is,
(1 + 2 + ... + 10)^2 = 55^2 = 3025

(n(n + 1)/2)^2

Hence the difference between the sum of the squares of the first 
ten natural numbers and the square of the sum is 
.

3025 - 385 = 2640

Find the difference between the sum of the squares of the first one
 hundred natural numbers and the square of the sum.

 (1^2 + 2^2 + ...100^2) = 

 (1 + 2 + 3 + ... 100)^2

'''

def find_squares():
    num, num2 = 1, 1
    
    for i in range(1, 101):
        num += pow(i, 2)
        num2 += i
    result = pow(num2, 2)
    return result - num
print(find_squares())
    
    
    
        
25164150

25164149
