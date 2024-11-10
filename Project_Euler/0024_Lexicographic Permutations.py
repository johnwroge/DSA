
'''
24 Lexicographic Permutations

A permutation is an ordered arrangement of objects. For example, 3124 is one possible permutation
 of the digits 1, 2, 3 and 4. If all of the permutations are listed numerically or alphabetically,
   we call it lexicographic order. The lexicographic permutations of 0, 1 and 2 are:

012   021   102   120   201   210

What is the millionth lexicographic permutation of the digits 0, 1, 2, 3, 4, 5, 6, 7, 8 and 9?

'''
from typing import List
def permute(nums: List[int]) -> List[List[int]]:
        answer = []
        def backtrack(start):
            if start == len(nums):
                answer.append(nums.copy())
                return
            
            for i in range(start, len(nums)):
                nums[i], nums[start] = nums[start], nums[i]
                backtrack(start + 1)
                nums[i], nums[start] = nums[start], nums[i]         
        backtrack(0)
        return answer

permutations = permute([0, 1,2,3,4,5,6,7,8,9])
permutations.sort()

print(permutations[999999])