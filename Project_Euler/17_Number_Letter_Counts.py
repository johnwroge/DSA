'''
If the numbers 1 to 5 are written out in words: one, two, three, four, five, then there 
are 3 + 3 + 5 + 4 + 4 = 19 letters used in total.

If all the numbers from 1 to 1000 (one thousand) inclusive were written out in words,
 how many letters would be used?

NOTE: Do not count spaces or hyphens. For example, 342 (three hundred and forty-two) 
contains 23 letters and 115 (one hundred and fifteen) contains 20 letters. The use of 
"and" when writing out numbers is in compliance with British usage.
'''

'''
can account for individual digits using hash map. 
Need to determine how to convert numbers from 1 - 1000 to word 
1, 
50 fifty 
100 - one hundred
'''

words = {0: 1, 1: 3, 2: 3, 3: 5, 4: 4, 5: 4, 6: 3, 7: 5, 8: 5, 9: 4}

answer = 0
for i in range(1, 6):
    number_string = str(i)
    for c in number_string:
        answer += words[int(c)] 
print(answer)
