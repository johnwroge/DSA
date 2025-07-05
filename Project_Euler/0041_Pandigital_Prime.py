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

def p41():
	for m in range(7654321, 7123455, -1):
		if ''.join(sorted(str(m))) == "1234567" and is_prime(m):
			return m

print(p41())