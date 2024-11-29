'''
The fraction 49/98 is a curious fraction, as an inexperienced mathematician in attempting to
simplify it may incorrectly believe that 49/98 = 4/8, which is correct, is obtained by
cancelling the 9s.

We shall consider fractions like, 30/50 = 3/5, to be trivial examples.

There are exactly four non-trivial examples of this type of fraction, less than one in
value, and containing two digits in the numerator and denominator.

If the product of these four fractions is given in its lowest common terms, find the
value of the denominator.
'''
from fractions import Fraction

def solution():
    candidates = {}
    numerator = 1
    denominator = 1
    for i in range(10, 100):
        for j in range(i + 1, 100):
            if i % 10 == 0 and j % 10 == 0:
                continue
            i_th = str(i)
            j_th = str(j)
            if i_th[1] == j_th[0]:
                top  = int(i_th[:1])
                bottom = int(j_th[1:])
                if bottom != 0: 
                    result = top/bottom
                if result == i/j:
                    numerator *= int(i_th)
                    denominator *= int(j_th)
    return Fraction(numerator, denominator)
     
# Optimized

from fractions import Fraction

def solution_2():
    product = Fraction(1, 1)
    # Only need to check first digit cancelation since problem states there are exactly 4 examples
    for numerator in range(10, 100):
        n_str = str(numerator)
        n_first, n_second = map(int, n_str)
        if n_second == 0:
            continue
            
        for denominator in range(numerator + 1, 100):
            d_str = str(denominator)
            d_first, d_second = map(int, d_str)
            if d_second == 0:
                continue
                
            if n_second == d_first and n_first/d_second == numerator/denominator:
                product *= Fraction(numerator, denominator)
                
    return product.denominator

print(solution())

print(solution_2())
