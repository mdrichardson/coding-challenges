# Say you have an array for which the ith element is the price of a given stock on day i.
#
# If you were only permitted to complete at most one transaction (i.e., buy one and sell one share of the stock), design an algorithm to find the maximum profit.
#
# Note that you cannot sell a stock before you buy one.
#
# Example 1:
#
# Input: [7,1,5,3,6,4]
# Output: 5
# Explanation: Buy on day 2 (price = 1) and sell on day 5 (price = 6), profit = 6-1 = 5.
#              Not 7-1 = 6, as selling price needs to be larger than buying price.
# Example 2:
#
# Input: [7,6,4,3,1]
# Output: 0
# Explanation: In this case, no transaction is done, i.e. max profit = 0.

# My notes:
#   Brute force approach would be for each item, find the best selling point and return the best profit. Can we optimize it more than that?
#       We could make it recursive, but that wouldn't really be faster
#   One way we could optimize is keep track of numbers we've already tried to use for the buy...then we're not using it again
#   This would still be too slow for a super long list, though
#       What if we run into like [100, 99, 98...1]
#           We need to somehow find the last possible place to sell by starting from the end and finding the first place where the next one backward is lower
#           That helps, but what if we run into a list that is huge, runs down, and then runs back up?
#               Like [9, 8, 7, 6, 5, 4, 3, 2, 3, 4, 5, 6, 7, 8, 9]
#           We could find the last selling point and then we find the first time we can make a profit and shorten the list to just that. THEN we iterate
#       Why don't we just do this in one pass?
#       We create a minimum price variable and set it at i = 0. As soon as we come across a lower price, that becomes the new min price
#       If we encounter an int greater than min price, we use that for the new profit if that profit is greater
#   For [7,1,5,3,6,4]
#   Min price is 7, then 1. First profit is 5-1=4. 3 isn't less than 1, so it's not the new min price and 3-1>4, so we skip. 6-1>4, so that's the new profit


test = [7,1,5,3,6,4]


def maxProfit(prices):
    """
    :type prices: List[int]
    :rtype: int
    """
    if len(prices) < 2:
        return 0
    profit = 0
    min_price = prices[0]
    for p in prices:
        if p < min_price:
            min_price = p
        elif p - min_price > profit:
            profit = p - min_price
    return profit


print(maxProfit(test))