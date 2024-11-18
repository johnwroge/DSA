'''
Euler discovered the remarkable quadratic formula:

    n^2 + n + 41

It turns out that the formula will produce 40 primes for the consecutive values
n = 0 to 39. However, when n = 40, 40^2 + 40 + 41 = 40(40 + 1) + 41 is divisible
by 41, and certainly when n = 41, 41^2 + 41 + 41 is clearly divisible by 41.

The incredible formula  n^2 − 79n + 1601 was discovered, which produces
80 primes for the consecutive values n = 0 to 79. The product
of the coefficients, −79 and 1601, is −126479.

Considering quadratics of the form:

    n^2 + an + b, where |a| < 1000 and |b| < 1000

    where |n| is the modulus/absolute value of n
    e.g. |11| = 11 and |−4| = 4

Find the product of the coefficients, a and b, for the quadratic expression
that produces the maximum number of primes for consecutive values of n,
starting with n = 0.
'''

# ==== Problem 27 ====
import numpy as np

def is_prime(n: int) -> bool:
    if n <= 1:
        return False
    for i in range(2, int(np.sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True

def poly_loop(a: int, b:int) -> []:
    n = 1
    tmp = n**2 + a*n + b
    ls_sol=[]
    while is_prime(tmp) is True:
        ls_sol.append(tmp)
        n = n + 1
        tmp = n**2 + a*n + b

    return ls_sol

ls_tmp = []
length_ls = 0
ls_sol = [0, 0] # [a, b]

for a in range(0, 1000): # a
    for b in range(0, 1001): # b
        ls_tmp = poly_loop(a,b)
        if len(ls_tmp)>length_ls:
            length_ls = len(ls_tmp)
            ls_sol[0] = a
            ls_sol[1] = b
        ls_tmp = poly_loop(a, -b)
        if len(ls_tmp) > length_ls:
            length_ls = len(ls_tmp)
            ls_sol[0] = a
            ls_sol[1] = -b
        ls_tmp = poly_loop(-a, b)
        if len(ls_tmp) > length_ls:
            length_ls = len(ls_tmp)
            ls_sol[0] = -a
            ls_sol[1] = b
        ls_tmp = poly_loop(-a, -b)
        if len(ls_tmp) > length_ls:
            length_ls = len(ls_tmp)
            ls_sol[0] = -a
            ls_sol[1] = -b

print(f"Solution are a= {ls_sol[0]}, b= {ls_sol[1]}")