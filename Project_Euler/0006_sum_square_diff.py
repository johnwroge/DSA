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


def sum_square_difference():
    n = 100
    sum_of_squares = n * (n + 1) * (2*n + 1) // 6
    square_of_sum = (n * (n + 1) // 2) ** 2
    return square_of_sum - sum_of_squares
print(sum_square_difference())
    
    