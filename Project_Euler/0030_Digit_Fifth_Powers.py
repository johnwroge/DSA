'''
Surprisingly there are only three numbers that can be written as the sum of fourth powers of their digits:

1634 = 14 + 64 + 34 + 44
8208 = 84 + 24 + 04 + 84
9474 = 94 + 44 + 74 + 44
As 1 = 14 is not a sum it is not included.

The sum of these numbers is 1634 + 8208 + 9474 = 19316.

Find the sum of all the numbers that can be written as the sum of fifth powers of their digits.
'''


def find_cutoff(power):
    max_digit_sum = lambda d: d * (9 ** power)
    smallest_number = lambda d: 10 ** (d - 1)
    
    d = 1
    while max_digit_sum(d) >= smallest_number(d):
        d += 1

    return max_digit_sum(d - 1)

cutoff = find_cutoff(5)
print(f"The cutoff for 5th powers is: {cutoff}")

def is_valid(num):
    total = [int(n) ** 5 for n in list(str(num))]
    total = sum(total)
    return total == num, total

def find_candidates():
    result = []
    for j in range(2, 1000000):
        valid, total = is_valid(j)
        if valid:
            result.append(j)
    return sum(result)


print(find_candidates())
