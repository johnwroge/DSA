
'''
The decimal number, 585 = 10010010012 (binary), is palindromic in both bases.
Find the sum of all numbers, less than one million, which are palindromic in base 10 and base 2.
(Please note that the palindromic number, in either base, may not include leading zeros.)
'''

def solution():
    nums = []
    for i in range(1000000):
        curr = bin(i)[2:]
        index = str(i)
        if curr[::-1] == curr and index == index[::-1]:
            nums.append(i)
    return sum(nums)


print(solution())