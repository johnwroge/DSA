

''' 
In England the currency is made up of pound, £, and pence, p, and there are eight coins in general circulation:

1p, 2p, 5p, 10p, 20p, 50p, £1 (100p) and £2 (200p).
It is possible to make £2 in the following way:

1×£1 + 1×50p + 2×20p + 1×5p + 1×2p + 3×1p
How many different ways can £2 be made using any number of coins?

'''


def coin_sum_leetcode(coins, amount):

    dp = [float('inf')] * (amount + 1)
    dp[0] = 0
    for coin in coins:
        for i in range(coin, amount + 1):
            dp[i] = max(dp[i], 1 + dp[i - coin])

    return dp[amount] if dp[amount] != float('inf') else -1

# print(coin_sum([1,2,5,10,20,50,100,200], 200))
# print(coin_sum([1,2,5], 11))
# print(coin_sum([1], 0))
# print(coin_sum([2], 1))

def coin_sum(coins, amount):
    dp = [0] * (amount + 1)
    dp[0] = 0
    for coin in coins:
        for i in range(coin, amount + 1):
            dp[i] = 1 + dp[i - coin]
    print(dp)
    return dp[amount] if dp[amount] != float('inf') else -1


print(coin_sum([1,2,5], 11))
print(coin_sum([1,2,5,10,20,50,100,200], 200))
