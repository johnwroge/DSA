'''
A palindromic number reads the same both ways. The largest palindrome made from the product of two 
2 digit numbers is 
9009 = 91 x 99

Find the largest palindrome made from the product of two 3-digit numbers.
'''

def palindrome(string):
    return string[::-1] == string

def find_number():
    max_pal = -1
    for i in range(999, 99, -1):
        for j in range(i, 99, -1):
            num = i * j
            flag = palindrome(str(num))
            if num > max_pal and flag:
                max_pal = num
                
    return max_pal


            
print(find_number())