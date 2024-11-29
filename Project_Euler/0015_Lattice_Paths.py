'''
15. Lattice Paths

Starting in the top left corner of a 2 x 2 grid, and only being able to move to the right and down, 
there are exactly routes to the bottom right corner.

'''

'''
solution: 
'''

def lattice_paths(n=20):
    # We need to choose n rights and n downs from total 2n moves
    # This is equivalent to C(2n,n)
    result = 1
    for i in range(n):
        result *= (2*n - i)
        result //= (i + 1)
    return result
print(lattice_paths())