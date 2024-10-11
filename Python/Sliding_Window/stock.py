'''

 You are given an integer array prices where prices[i]
 is the price of a given stock on the ith day.
 
On each day, you can complete 1 transaction You may either:
1. Buy one share of stock at the current price
2. Sell as many of your current shares of stock as you wish, at the current price
3. Do nothing
 
 Input: prices = [7,1,5,3,6,4]

 Buy low sell high!

 explanation:
 Do nothing on 7.
 Buy 1 share on 1. Total profit -1, total shares 1
 Sell 1 share on 5. Total profit 4, total shares 0
 Buy 1 share on 3. Total profit 1, total shares 1
 Sell 1 share on 6. Total profit 7, total shares 0
 Do nothing on 4.
End total profit 7.

get the smallest price on left and maximum price at right

 '''
def stocks(prices):
    temp_max = 0
    max_to_right = [-1] * len(prices)
    profit = 0
    for i in range(len(prices) - 1, -1, -1):
        if temp_max < prices[i]:
            max_to_right[i] = prices[i]
            temp_max = prices[i]
    for r in range(len(prices)):
        if prices[r] >= max_to_right[r]:
            pass
        # buy
        elif max_to_right[r] == -1:
            profit -= prices[r]
        # sell
        else:
            profit += prices[r]

    return profit if profit != 0 else -1

prices = [7,1,5,3,6,4]
print(stocks(prices))

'''




'''

