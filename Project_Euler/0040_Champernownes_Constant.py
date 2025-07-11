"""
An irrational decimal fraction is created by concatenating the positive integers:

0.123456789101112131415161718192021…

It can be seen that the 12th digit of the fractional part is 1.

If dn represents the nth digit of the fractional part, find the value of the following expression.

d1 × d10 × d100 × d1000 × d10000 × d100000 × d1000000


"""

def p40():
	res = 1
	for x in range(7):
		c, n = 1, 10 ** x
		while True:
			if 9 * c * 10 ** (c-1) < n:
				n -= 9 * c * 10 ** (c-1)
				c += 1
			else:
				k = 10 ** (c-1) + (n-1) // c
				res *= int(str(k)[(n-1)%c])
				break
	return res
print(p40())