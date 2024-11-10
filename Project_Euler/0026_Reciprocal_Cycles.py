'''
A unit fraction contains 1 in the numerator. The decimal representation
of the unit fractions with denominators 2 to 10 are given:

1/2 = 0.5
1/3 = 0.(3)
1/4 = 0.25
1/5 = 0.2
1/6 = 0.1(6)
1/7 = 0.(142857)
1/8 = 0.125
1/9 = 0.(1)
1/10 = 0.1

Where 0.1(6) means 0.166666..., and has a 1-digit recurring cycle.
It can be seen that 1/7 has a 6-digit recurring cycle.

Find the value of d < 1000 for which 1/d contains the longest recurring cycle
in its decimal fraction part.

'''
from decimal import Decimal, getcontext

def repeating_cycle_length(denominator: int) -> int:
    seen_remainders = {}
    numerator = 1
    position = 0

    while numerator != 0:
        if numerator in seen_remainders:
            # Cycle length is the difference in positions of the repeated remainder
            return position - seen_remainders[numerator]
        seen_remainders[numerator] = position
        numerator = (numerator * 10) % denominator
        position += 1

    return 0 

def find_longest_repeating_cycle(limit: int) -> int:
    max_cycle_length = 0
    result_denominator = 0
    for i in range(1, limit + 1):
        cycle_length = repeating_cycle_length(i)
        if cycle_length > max_cycle_length:
            max_cycle_length = cycle_length
            result_denominator = i
    return result_denominator

print(find_longest_repeating_cycle(1000))

num = longest = 1
for n in range(3, 1000, 2):
    if n % 5 == 0:
        continue

    p = 1

    while (10 ** p) % n != 1:
        p += 1

    if p > longest:
        num, longest = n, p

# print(num)

def recurring_cycle(n, d):
    # solve 10^s % d == 10^(s+t) % d
    # where t is length and s is start
    for t in range(1, d):
        if 1 == 10**t % d:
            return t
    return 0

longest = max(recurring_cycle(1, i) for i in range(2,1001))
# print([i for i in range(2,1001) if recurring_cycle(1, i) == longest][0])



