'''
 2520 is the smallest number that can be divided by each of the numbers from 1 to 10
 without any remainder.

What is the smallest positive number that is evenly divisible by all of the numbers from 
 1 to 20?

'''


def vals ():
    num = 20
    while True:
        print(num)
        for n in range(1, 21):
            if num % n > 0:
                break
            if n == 20:
                return num
        num += 1
    return 
print(vals())


