'''
Let d(n) be defined as the sum of proper divisors of n (numbers less than that divide evenly into n)

For example the proper divisors of 220 are 1, 2, 4, 5, 10, 11, 20, 22, 44, 55 and 110 -> d(220) -> 284

The proper divisors of 284 are 1, 2, 4, 71, and 142. so d(284) = 220

therefore d(220) = 284


'''

'''
find all numbers less than 10,000 that divide evenly into 10,000

add all these numbers up 

'''
def sum_of_divisors(n):
    total = 0
    for i in range(1, (n // 2) + 1):
        if n % i == 0:
            total += i
    return total    
    

# d(220) = 284, d(284) = 220 , they are amicable numbers
# sum: number
# {284: 220}
# is num in hashmap and hashmap 
    
'''
{220: 284, 284: 220}


for k, v in obj
    if obj[v] = k
        found amicable number

print(sum_of_divisors(8128)) -> 8128 not an amicable number because 8128 is perfect

from the question where d(a) = b and d(b) = a where a != b 


'''
def find_sum_of_numbers(n):
    hash_map = {}
    total = []
    for i in range(1, n):
        current = sum_of_divisors(i)
        if current != i:
            hash_map[i] = current
    for k, v in hash_map.items():
        if v in hash_map and hash_map[v] == k:
            total.append(k)
    return sum(total)


print(find_sum_of_numbers(10000))

'''
the main distinction is that amicable numbers cannot be perfect numbers because they always come in
 pairs of distinct numbers, while perfect numbers are single numbers equal to the sum of their own divisors.
'''


