
def multiples(n):
    # initialize a total
    total = 0
    # loop until n (1000)
    for i in range(n):
        # if n mod 3 is 0 or n mod 5 is 0
        if i % 3 == 0 or i % 5 == 0:
            total += i
            # add to total 
    # return the total
    return total
    
print(multiples(1000))