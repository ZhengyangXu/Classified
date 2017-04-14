"""
Description
_____________
Say you have an array for which the ith element is the price of a given stock on day i.

Design an algorithm to find the maximum profit. You may complete as many transactions
as you like (ie, buy one and sell one share of the stock multiple times).
 However, you may not engage in multiple transactions at the same time
 (ie, you must sell the stock before you buy again).

Approach
_______________
Since unlimited transactions
add up all the gaps

Complexity
________________
Time - O(N)
Space - O(1)
"""


class Solution(object):

    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        max_profit = 0
        for i in xrange(1, len(prices)):
            if prices[i] > prices[i - 1]:
                max_profit += (prices[i] - prices[i - 1])
        return max_profit
