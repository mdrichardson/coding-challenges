# Say you have an array for which the ith element is the price of a given stock on day i.
#
# Design an algorithm to find the maximum profit. You may complete as many transactions as you like
# (i.e., buy one and sell one share of the stock multiple times).
#
# Note: You may not engage in multiple transactions at the same time (i.e., you must sell the stock before you buy again).
#
# Example 1:
#
# Input: [7,1,5,3,6,4]
# Output: 7
# Explanation: Buy on day 2 (price = 1) and sell on day 3 (price = 5), profit = 5-1 = 4.
#              Then buy on day 4 (price = 3) and sell on day 5 (price = 6), profit = 6-3 = 3.
# Example 2:
#
# Input: [1,2,3,4,5]
# Output: 4
# Explanation: Buy on day 1 (price = 1) and sell on day 5 (price = 5), profit = 5-1 = 4.
#              Note that you cannot buy on day 1, buy on day 2 and sell them later, as you are
#              engaging multiple transactions at the same time. You must sell before buying again.
# Example 3:
#
# Input: [7,6,4,3,1]
# Output: 0
# Explanation: In this case, no transaction is done, i.e. max profit = 0.

# My notes:
#   We want to buy low/sell high. Must go buy/sell/buy/sell, so we'll need a can_buy boolean
#   You definitely want to sell at the highest point before the end, so that shortens the list quite a bit after that
#   Maybe we can mark each index as buy or sell by using i > i+1 = sell, i < i+1 = buy. Buy at the first buy that isn't followed by a sell,
#       sell at the first sell that isn't followed by a sell and repeat? Let's make a list with some edge cases
#   [7, 1, 5, 2, 3, 8, 7, 9, 8, 6, 1, 5, 2]
#    h, b, s, b, h, s, b, s, h, h, b, s, h
#   Buy when: we can buy AND i <= i + 1 AND we can sell later
#   Sell when: we can't buy bough AND i > i + 1
#   Else, we hold


test = [9,9,0,3,0,7,7,7,4,1,5,0,1,7]

def maxProfit(prices):
    """
    :type prices: List[int]
    :rtype: int
    """
    # Catch empty input
    if not prices:
        return 0
    # Initiate profit and next available action variables
    profit = 0
    next_action = 'buy'
    for i, p in enumerate(prices):
        # Handle the end of the list. No reason to buy. Sell if we can
        if i == len(prices) - 1:
            if next_action == 'sell':
                profit += prices[i]
            # We're done, so let's break
            break
        # Buy when: we can buy AND i <= i + 1 AND we can sell later
        if next_action == 'buy' and prices[i] <= prices [i + 1]:
            # Check to see if there are never more buy opportunities
            new_list = prices[i:]
            # Instantiate start and end index variables and one to force a break
            start = 0
            end = 1
            force_break = False
            # Loop through the rest of the list, looking for a buy opportunity
            while True:
                # Handle reaching the end of the list
                if end >= len(new_list):
                    force_break = True
                    break
                # Handle finding a buy opportunity
                if new_list[start] < new_list[end]:
                    break
                # Since we haven't found a buy opportunity, we need to move until we find it
                start += 1
                end += 1
            if force_break:
                break
            profit -= prices[i]
            next_action = 'sell'
        # Sell when: we can't buy bough AND i > i + 1
        elif next_action == 'sell' and prices[i] > prices[i + 1]:
            profit += prices[i]
            next_action = 'buy'
    return profit



print(maxProfit(test))