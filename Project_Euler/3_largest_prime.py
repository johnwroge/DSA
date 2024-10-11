'''
The prime factors of 13195 a43 5, 7, 13, and 29. 

What is the largest prime factor of the number 600851475143
'''
import math
def largest_prime(num):
    i=2 # Smallest prime factor
    for k in range(0,num):
        if i >= num: # Prime factor of the number should not be greater than the number
            break
        elif num % i == 0: # Check if the number is evenly divisible by i
            num = num / i
        else:
            i= i + 1
            print(i)
    print ("biggest prime number is: "+str(num)) 
print(largest_prime(600851475143))



    

print(largest_prime(600851475143))