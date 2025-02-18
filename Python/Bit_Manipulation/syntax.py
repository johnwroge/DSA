

n1 = 1
n2 = 1

# XOR 
n5 = n1 ^ n2
# print(n5)


# Shifts

'''
It's important to note that the behavior of right shift depends on the type of 
the value being shifted. For positive integers, it performs an arithmetic right 
shift, while for negative integers, it performs a logical right shift (which 
fills the leftmost bits with zeros). This behavior ensures that the sign of the
 number is preserved.
'''
number = 20
# print(bin(number))
# number <<= 1
# print(bin(number))
# number >>= 1
# print(bin(number))

# Application in Permission

NEU_READ = 0b1000
NEU_WRITE = 0b0100
NEU_EXEC = 0b0010
NEU_CHANGE = 0b0001

def myFunction(permission):
    print(bin(permission))
    return
# print(myFunction(NEU_WRITE | NEU_READ))

# a = 10
# b = 20

# a ^= b
# print(a)
# b ^= a
# print(b)
# a ^= b

# print(a)
# print(b)

# even or odd
somenumber = 372349

if somenumber & 1 == 0:
    print('even')
else:
    print('odd')


# Bitwise OR

'''
The bitwise OR operation compares each bit of the two operands.
If either bit is 1, the resulting bit is 1.
If both bits are 0, the resulting bit is 0.
'''

x = 5  # 0101 in binary
x |= 3  # 0011 in binary
print(x)

dict1 = {'a': 1, 'b': 2}
dict2 = {'b': 3, 'c': 4}

dict1 |= dict2
print(dict1)

# Calculate the maximum possible OR value
max_or_value = 0
for num in nums:
    max_or_value |= num