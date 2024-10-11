'''
By listing the first six prime numbers: 
2, 3, 5, 6, 11, and 13, we can see that the 6th prime is 13/

What is the 10001st prime number?


'''

def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

'''
 Sieve of Eratosthenes.
'''

def sieve_of_eratosthenes(limit):
    primes = []
    is_prime = [True] * (limit + 1)
    is_prime[0] = is_prime[1] = False

    for num in range(2, int(limit**0.5) + 1):
        if is_prime[num]:
            primes.append(num)
            for multiple in range(num * num, limit + 1, num):
                is_prime[multiple] = False

    for num in range(int(limit**0.5) + 1, limit + 1):
        if is_prime[num]:
            primes.append(num)

    return primes


n,result = 1,[]
while len(result) < 10001:
    if is_prime(n):
        result.append(n)
    n += 1
print(result[len(result) - 1])


