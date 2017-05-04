"""
Description
____________
Say you have an array for which the ith element is the price of a given stock on day i.

If you were only permitted to complete at most one transaction
(ie, buy one and sell one share of the stock), design an algorithm to find the maximum profit.

Example 1
_____________
Input: [7, 1, 5, 3, 6, 4]
Output: 5

max. difference = 6-1 = 5 (not 7-1 = 6, as selling price needs to be larger than buying price)
Example 2
________________
Input: [7, 6, 4, 3, 1]
Output: 0

In this case, no transaction is done, i.e. max profit = 0.

Approach
_________________
two pointers

maintain - lowest, max

one loop, update lowest, and update max = max(max, cur - lowest)
since high must cover after low
"""
 

class Solution(object):

    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        if prices is None or len(prices) == 0:
            return 0
        lowest = prices[0]
        max_profit = 0
        for i in prices:
            if i < lowest:
                lowest = i
            if i > lowest:
                max_profit = max(i - lowest, max_profit)
        return max_profit
