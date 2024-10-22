
'''
Work out the first ten digits of the sum of the following one-hundred 50-digit numbers

'''

import os

file_path = os.path.abspath('./Project_Euler/input/13.txt')

with open(file_path) as f:
    commands = f.readlines()

numbers = []
for line in commands:
    line = line.replace('\n','')
    numbers.append(int(line))



now = 0
for i in range(len(numbers)): 
    now += numbers[i]
    if len(str(now)) == 10:
        break

print(int(str(now)[:10]))






