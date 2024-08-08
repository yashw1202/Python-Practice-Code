# Best Time to Buy and Sell Stock   

# You are given an array prices where prices[i] is the price of a given stock on the ith day.

# You want to maximize your profit by choosing a single day to buy one stock and choosing a different day in the future to sell that stock.

# Return the maximum profit you can achieve from this transaction. If you cannot achieve any profit, return 0.

import sys
def maxProfit(prices) :
    buyprice=prices[0]
    profit = 0 
    for i in prices[1:]:
        if i<buyprice:
            buyprice=i
        profit=max(profit,i-buyprice)
    return profit

test = int(input())
while test>0:
    test-=1
    prices = list(map(int,input().split()))
    print(maxProfit(prices))