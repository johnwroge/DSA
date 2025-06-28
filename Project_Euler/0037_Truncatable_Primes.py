'''
The number 3797 has an interesting property. Being prime itself, it is possible
to continuously remove digits from left to right, and remain prime at each stage:
3797, 797, 97, and 7. Similarly we can work from right to left: 3797, 379, 37, and 3.
Find the sum of the only eleven primes that are both truncatable from left to right
and right to left. NOTE: 2, 3, 5, and 7 are not considered to be truncatable primes.
'''

from math import floor


def is_prime(n):
    if n < 2:
        return False
    if n in {2, 3, 5, 7}:
        return True
    if n % 2 == 0 or n % 3 == 0 or n % 5 == 0:
        return False
    
    for i in range(7, floor(n ** 0.5) + 1, 2):
        if n % i == 0:
            return False
    return True


def is_truncatable(n):
    to_check = str(n)
    
    if not is_prime(n):
        return False
    
    for i in range(1, len(to_check)):
        right_to_left = int(to_check[:len(to_check) - i])  
        left_to_right = int(to_check[i:])  
        
        if not is_prime(right_to_left) or not is_prime(left_to_right):
            return False
    return True


def solution():
    answer = []
    n = 11  
    while len(answer) < 11:
        if is_truncatable(n):
            answer.append(n)
        n += 2 if n > 2 else 1  
    return sum(answer)
        

print(solution())