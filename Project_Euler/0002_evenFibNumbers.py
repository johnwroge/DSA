
def even_fib_numbers():
    cache = {0: 0, 1: 1, 2: 1}
    i = 3
    while i:
        total = cache[i - 1] + cache[i - 2]
        cache[i] = total
        i += 1
        if total > 4000000:
            break
    return sum([n for n in cache.values() if n % 2 == 0])
    
print(even_fib_numbers())
