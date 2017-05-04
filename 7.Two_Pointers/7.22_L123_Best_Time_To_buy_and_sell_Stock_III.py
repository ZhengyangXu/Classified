"""
Description
_____________
Say you have an array for which the ith element is the price of a given stock on day i.

Design an algorithm to find the maximum profit. You may complete at most two transactions.

Note:
You may not engage in multiple transactions at the same time (ie, you must sell the stock before you buy again).


Approach
_______________
sicne we only allow two transactions and no overlap, the split can be any position
so form a forward, and backward, then find the maximum

See code

Complexity
_______________
Time - O(N)
Space - O(N)
"""
 

class Solution(object):

    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        if prices is None or len(prices) == 0:
            return 0
        n = len(prices)
        forward = [0] * n
        backward = [0] * n

        lowest = prices[0]
        max_sofar = 0
        for i in xrange(n):
            if prices[i] < lowest:
                lowest = prices[i]
            if prices[i] > lowest:
                max_sofar = max(prices[i] - lowest, max_sofar)
            forward[i] = max_sofar

        largest = prices[-1]
        max_sofar = 0
        for i in xrange(n - 1, -1, -1):
            if prices[i] > largest:
                largest = prices[i]
            if prices[i] < largest:
                max_sofar = max(largest - prices[i], max_sofar)
            backward[i] = max_sofar
        # print forward, backward
        return max([forward[i] + backward[i] for i in xrange(n)])
