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

singles = {0: 'zero', 1: 'one', 2: 'two', 3: 'three', 4: 'four', 5: 'five', 6: 'six', 7: 'seven', 8: 'eight', 9: 'nine'}
teens = {10: 'ten', 11: 'eleven', 12: 'twelve', 13: 'thirteen', 14: 'fourteen', 15: 'fifteen', 16: 'sixteen', 17: 'seventeen', 18: 'eighteen', 19: 'nineteen'}           
tens = {20: 'twenty', 30: 'thirty', 40: 'forty', 50: 'fifty', 60: 'sixty', 70: 'seventy', 80: 'eighty', 90: 'ninety', 100: 'hundred'}
           
words = []

def int_to_words(i):
    curr = []
    while int(i) != 0:
        prev = ''
        # 1000's
        if i // 1000 > 0:
            prev += 'one thousand'
            i -= 1000
        # 100's
        elif i // 100 > 0:
            prev += singles[i // 100] + ' hundred'
            i -= (i // 100) * 100
            if i != 0:
                prev += ' and'
        # 10's
        elif i // 10 > 0:
            if i in teens:
                prev += teens[i]
                i = 0
            elif i % 10 > 0:
                prev += singles[i % 10]
                i -= (i % 10)
            elif i in tens:
                prev += tens[i]
                i = i % 10
        # 1's
        elif i % 10:
           
            prev += singles[i % 10]
            i -= (i % 10)
        curr.append(prev)
    # return curr[::-1]
    return ' '.join(curr[::-1]).replace(' ','')
        

word_list = [] 
total = 0

for i in range(1, 1001):
    total += len(int_to_words(i))
# print(total)


# cleaned up solution 

def number_to_words(n):
    ones = ['', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine',
            'ten', 'eleven', 'twelve', 'thirteen', 'fourteen', 'fifteen', 'sixteen', 
            'seventeen', 'eighteen', 'nineteen']
    
    tens = ['', '', 'twenty', 'thirty', 'forty', 'fifty', 'sixty', 'seventy', 'eighty', 'ninety']
    
    if n == 1000:
        return 'onethousand'
        
    def under_100(n):
        if n < 20:
            return ones[n]
        return tens[n // 10] + ones[n % 10]
        
    def under_1000(n):
        if n < 100:
            return under_100(n)
        hundreds = ones[n // 100] + 'hundred'
        remainder = n % 100
        if remainder == 0:
            return hundreds
        return hundreds + 'and' + under_100(remainder)

    return under_1000(n)

print(sum(len(number_to_words(i)) for i in range(1, 1001)))