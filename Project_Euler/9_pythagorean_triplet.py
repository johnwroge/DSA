'''
A Pythagorean triplet is a set of three natural numbers, 
a < b < c, for which, a^2 + b^2 = c^2

For example, 
3^2 + 4^2 = 9 + 16 = 25 = 5^2

There exists exactly one Pythagorean triplet for which 
a + b + c = 1000

a^2 + b^2 = c^2

Find the product abc

'''

def is1000(n):
    return n == 1000

for i in range(1000):
    for j in range(i, 1000):
        product = pow(i,2) + pow(j,2)
        c = pow(product, 1/2)
        total = i + j + c
        if is1000(total):
            print(i, j, c)
            print(i*j*c)

