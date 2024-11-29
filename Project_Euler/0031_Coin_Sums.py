

''' 
In England the currency is made up of pound, £, and pence, p, and there are eight coins in general circulation:

1p, 2p, 5p, 10p, 20p, 50p, £1 (100p) and £2 (200p).
It is possible to make £2 in the following way:

1×£1 + 1×50p + 2×20p + 1×5p + 1×2p + 3×1p
How many different ways can £2 be made using any number of coins?

'''

# Backtracking 
def combinationSum(candidates, target):
    def backtrack(start, target, path):
        if target == 0:
            result.append(list(path)) 
            return
        
        for i in range(start, len(candidates)):
            if candidates[i] > target:
                break
            path.append(candidates[i])
            backtrack(i, target - candidates[i], path)
            path.pop()  

    # candidates.sort() 
    result = []
    backtrack(0, target, [])
    return len(result)

# print(combinationSum([1,2,5,10,20,50,100,200], 200))

def coin_sum_2D_DP(coins, amount):
    table = [[0 for _ in range(len(coins))] for _ in range(amount + 1)]
    for i in range(len(table)):
        table[i][0] = 1
    # print(table)
    for i in range(len(table)):
        for j in range(1, len(table[0])):
            table[i][j] = table[i][j - 1]
            if (coins[j] <= i):
                table[i][j] += table[i - coins[j]][j]
    return table[len(table) - 1][len(table[0]) - 1]

# print(coin_sum_2D_DP([1,2,5,10,20,50,100,200], 200))

def coin_sum_1D_DP(coins, amount):
    table = [0 for _ in range(amount + 1)]
    table[0] = 1
    for i in range(len(coins)):
        for j in range(coins[i], amount + 1):
            table[j] += table[j - coins[i]]
    return table[amount]

# print(coin_sum_1D_DP([1,2,5,10,20,50,100,200], 200))
