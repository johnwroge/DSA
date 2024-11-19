'''
Starting with the number 1 and moving to the right in a clockwise direction a 5 by 5 spiral is formed as follows:

21 22 23 24 25
20  7  8  9 10
19  6  1  2 11
18  5  4  3 12
17 16 15 14 13

It can be verified that the sum of the numbers on the diagonals (both) is 101.

What is the sum of the numbers on the diagonals in a 1001 by 1001 spiral formed in the same way?


'''

'''
solution:

numbers are diagonals 21, 7, 1, 3, 13 and 17, 5, 1, 9, 25

the pattern is numbers start with 1 and for each 4 directions are 2 apart 
 3,  5, 7,  9 (where amount is 2)
13, 17, 21, 25 (where amount is 4)
31, 37, 43, 49 (where amount is 6)


43 44 45 46 47 48 49
42 21 22 23 24 25 26
41 20  7  8  9 10 27
40 19  6  1  2 11 28
39 18  5  4  3 12 29
38 17 16 15 14 13 30
37 36 35 34 33 32 31 



'''

def Solution(n):
    i = 1
    total = 1
    curr = 2
    while i < n * n:
        for _ in range(4):
            i += curr
            total += i
        curr += 2
    return total

# print('Solution is', Solution(5), 'for a 5 by 5 square')

print('Solution is', Solution(1001), 'for a 1001 by 1001 square')

